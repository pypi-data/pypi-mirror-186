# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from math import ceil
from os.path import isfile, isdir
import os
import numpy as np
from timeit import default_timer
from argparse import ArgumentParser
from pathlib import Path

try:
    from base64 import decodebytes
except ImportError:
    from base64 import decodestring as decodebytes

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


class ModelClient:
    """
    The ModelClient class is responsible for all interactions
    with the modelrunner application through Python.
    """

    # The default quantization parameters for inputs are based on the
    # assumption that models will typically normalize their inputs [-1..1]
    default_input_quant_scale = 1. / 128.
    default_input_zero_point = 128

    # The default quantization parameters for outputs are based on the
    # assumption that models will typically have softmax output [0..1]
    default_output_quant_scale = 1. / 256.
    default_output_zero_point = 0

    def __init__(self, uri, rtm=None, timeout=100, callback=print, upload_here=True):
        """Initializes the ModelClient class. If given an rtm it attempts to
        load it at the given URI, where a modelrunner application
        should be running.

        @param uri A string that contains the URI.
        @param rtm A string, bytearray, or Path that represents the actual
        rtm model or a path to a .rtm file (default=None)."""

        from requests import Session
        from requests.exceptions import Timeout
        from requests.adapters import HTTPAdapter
        from requests.packages.urllib3.util.retry import Retry

        self.uri = uri
        self.rtm = rtm
        self.put_time = None
        self.post_time = None
        self.eval_time = None
        self.raw_time = None

        self.decode_time = None
        self.input_time = None
        self.output_time = None

        self.timeout = timeout
        self.callback = callback
        self.session = Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.tensor_dtype = {
            'INT8': np.int8,
            'UINT8': np.uint8,
            'INT16': np.int16,
            'UINT16': np.uint16,
            'INT32': np.int32,
            'UINT32': np.uint32,
            'INT64': np.int64,
            'UINT64': np.uint64,
            'FLOAT16': np.float16,
            'FLOAT32': np.float32,
            'FLOAT64': np.float64,
        }

        self.input_quant_scale = ModelClient.default_input_quant_scale
        self.input_zero_point = ModelClient.default_input_zero_point
        self.output_quant_scale = ModelClient.default_output_quant_scale
        self.output_zero_point = ModelClient.default_output_zero_point
        self.stop_uploading_model = False

        if rtm is None:
            return

        if upload_here:
            self.load_model(callback=callback, rtm=rtm, timeout=timeout)

    def upload_model(self):
        self.load_model(callback=self.callback, rtm=self.rtm, timeout=self.timeout)

    def stop_uploading(self):
        self.stop_uploading_model = True

    @property
    def uri(self):
        """Returns the current URI that the ModelClient is trying
        to communicate with."""

        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the URI with which the ModelClient will attempt to communicate.

        @param uri A string containing the new URI."""

        self._uri = uri
        if self._uri[self._uri.rfind('/'):self._uri.rfind('/') + 2] != '/v':
            self._uri += '/v1'

    def get_model_name(self):
        """Returns the name of the current model,
        if one exists, at the given URI."""

        if self.uri is None:
            return None

        r = self.session.get(self.uri + '/model')
        try:
            data = r.json()
        except JSONDecodeError:
            raise RuntimeError('ModelRunner Error: %s' % r.text)

        return data['model_name']

    def get_layers(self):
        """Returns all layer information of the current model,
        if one exists, at the current URI."""

        if self.uri is None:
            return None

        r = self.session.get(self.uri + '/model')
        try:
            data = r.json()
        except JSONDecodeError:
            raise RuntimeError('ModelRunner Error: %s' % r.text)

        return data['layers']

    def get_io_quantization(self):
        if self.uri is None:
            return None

        r = self.session.get(self.uri + '/model')
        try:
            data = r.json()
        except JSONDecodeError:
            raise RuntimeError('ModelRunner Error: %s' % r.text)

        quant_info = {}
        for node in data['inputs']:
            quant_info[node['name']] = {}
            if node['datatype'] == 'FLOAT32':
                quant_info[node['name']]['datatype'] = np.float32
                continue
            elif node['datatype'] == 'UINT8':
                quant_info[node['name']]['datatype'] = np.uint8
            elif node['datatype'] == 'INT8':
                quant_info[node['name']]['datatype'] = np.int8

            quant_info[node['name']]['quant_scale'] = node['scale']
            quant_info[node['name']]['zero_point'] = node['zero_point']

            if quant_info[node['name']]['quant_scale'] == 0:
                quant_info[node['name']]['quant_scale'] = \
                    self.input_quant_scale
                quant_info[node['name']]['zero_point'] = self.input_zero_point
                if node['datatype'] == 'INT8':
                    quant_info[node['name']]['zero_point'] -= 128

        for node in data['outputs']:
            quant_info[node['name']] = {}
            if node['datatype'] == 'FLOAT32':
                quant_info[node['name']]['datatype'] = np.float32
                continue
            elif node['datatype'] == 'UINT8':
                quant_info[node['name']]['datatype'] = np.uint8
            elif node['datatype'] == 'INT8':
                quant_info[node['name']]['datatype'] = np.int8

            quant_info[node['name']]['quant_scale'] = node['scale']
            quant_info[node['name']]['zero_point'] = node['zero_point']

            if quant_info[node['name']]['quant_scale'] == 0:
                quant_info[node['name']]['quant_scale'] = \
                    self.output_quant_scale
                quant_info[node['name']]['zero_point'] = self.output_zero_point
                if node['datatype'] == 'INT8':
                    quant_info[node['name']]['zero_point'] -= 128
        return quant_info

    def get_labels(self, id=None):
        r = self.session.get(self.uri)
        try:
            data = r.json()
        except JSONDecodeError:
            raise RuntimeError('ModelRunner Error: %s' % r.text)

        if 'labels' not in data['model']:
            print("There are no labels in this model")
        if id:
            return data['model']['labels'][id]
        return data['model']['labels']

    def get_layer_timing_info(self):
        if self.uri is None:
            return None

        r = self.session.get(self.uri + '/model')
        try:
            data = r.json()
        except JSONDecodeError:
            raise RuntimeError('ModelRunner Error: %s' % r.text)

        layers = data['layers']
        layer_timing = {}
        for layer in layers:
            if layer['type'] in ['constant', 'input']:
                continue
            seconds = 0.0
            if 'timing' in layer['tensor']:
                seconds = layer['tensor']['timing'] / 1e9
            layer_timing[layer['name']] = seconds

        return layer_timing

    def get_op_timing_info(self):
        """Returns the timing information for all layer types that exist
        within the current model, if one exists, at the current URI.

        @return A dictionary where the keys are the names of the operations
        within the model and the value is a list of
        [avg_time, total_time, number of layers of the given type]."""

        if self.uri is None:
            return None

        r = self.session.get(self.uri + '/model')
        try:
            data = r.json()
        except JSONDecodeError:
            raise RuntimeError('ModelRunner Error: %s' % r.text)

        layers = data['layers']
        op_timing = {}
        for layer in layers:
            seconds = 0.0
            if 'timing' in layer['tensor']:
                seconds = layer['tensor']['timing'] / 1e9
            if layer['type'] not in op_timing:
                op_timing[layer['type']] = [seconds, seconds, 1]
            else:
                op_timing[layer['type']][1] += seconds
                op_timing[layer['type']][2] += 1
                op_timing[layer['type']][0] = op_timing[layer['type']][1] \
                                              / op_timing[layer['type']][2]

        op_timing.pop('constant', None)
        op_timing.pop('input', None)
        return op_timing

    def get_timing_info(self):
        """Returns the timing information regarding how long it took
        to send the most recent rtm to the modelrunner application, the total
        time to run the model (includes the post request and evaluation), and
        the time it took for the modelrunner application to run the model."""

        return self.put_time, self.post_time, self.eval_time

    def get_runner_timings(self):
        """
        Returns the timings values from modelruuner/v1/model {timings key}
        these thre values make reference to the image decode time, input time and output time
        """
        return self.decode_time, self.input_time, self.output_time

    def load_model(self, rtm, uri=None, timeout=100, callback=print):
        """Attempts to load a given rtm to the modelrunner application at
        the given URI, or the current URI if none is provided.

        @param rtm A string, bytearray, or Path that represents the actual
        rtm model or a path to a .rtm file.
        @param uri A string that contains the URI (default=None)."""

        if uri is not None:
            self.uri = uri
        if isinstance(rtm, bytes) or isinstance(rtm, bytearray):
            self.rtm = bytearray(rtm)
        elif isinstance(rtm, Path):
            with open(rtm, 'rb') as f:
                self.rtm = bytearray(f.read())
        elif isfile(rtm):
            with open(rtm, 'rb') as f:
                self.rtm = bytearray(f.read())

        else:
            raise ValueError("The given RTM cannot be supported, filepaths"
                             " and bytearrays of the model are accepted")

        # try:
        #     assert(self.rtm[4:8].decode('ascii') == 'RTMx'), \
        #         "Invalid RTM file"
        # except AttributeError:
        #     raise FileNotFoundError("The file %s does not exist." % self.rtm)

        # model = ffi.from_buffer(self.rtm)
        # assert lib.nn_model_validate(model, len(model)) == 0, \
        #     "The RTM model is invalid."

        start_time = default_timer()
        hostresp = self.session.get(self.uri)
        if not hostresp:
            callback('ModelRunner Error:', hostresp.text)
            return
        hostinfo = hostresp.json()
        block_size = hostinfo['model_limits']['block_size']
        block_count = int(ceil(len(self.rtm) / block_size))
        r = self.session.put(self.uri, files={
            'block_count': block_count
        })
        try:
            assert r.json()['reply'] == 'success'
        except JSONDecodeError:
            raise RuntimeError('ModelRunner Error: %s' % r.text)

        i = 1
        for block in range(block_count):
            if self.stop_uploading_model:
                raise ValueError("upload_aborted_by_user")

            chunk = self.rtm[block * block_size:(block + 1) * block_size]
            if block == block_count - 1:
                callback("\r Upload: %.4f" % (float(block + 1) / block_count * 100))
            else:
                callback("\r Upload: %.4f" %
                         (float(block + 1) / block_count * 100), end='')
            try:
                r = self.session.put(self.uri, files={
                    'block_content': chunk
                }, timeout=timeout)
            except Timeout as e:
                raise RuntimeError("Timeout Error: %s" % str(e))

            try:
                resp_json = r.json()
                if i != block_count:
                    if 'block' not in resp_json:
                        print(resp_json)
                        raise ValueError(
                            "block key does not exist in the response.")
                    if resp_json['block'] != i:
                        raise ValueError('Block received does not match block sent: ' +
                                         str(resp_json['block']) + ' != ' + str(i))
                else:
                    if 'reply' not in resp_json:
                        print(resp_json)
                        raise ValueError(
                            "reply key does not exist in the response.\n" + r.text + '\n' + str(resp_json))
                    assert (resp_json['reply'] == 'success'), \
                        'Invalid server response sending model: %s' % r.text
            except JSONDecodeError:
                print('\n Error Message \n')
                raise RuntimeError('ModelRunner Error: %s' % r.text)
            i += 1
        self.put_time = default_timer() - start_time

    def __tensor_multipart(self, tensor):
        return (','.join(map(str, tensor.shape)),
                tensor.astype(tensor.dtype,
                              order='C',
                              casting='unsafe',
                              copy=False).tobytes(),
                'application/vnd.deepview.tensor.float32')

    def run(self, inputs=None, outputs=None, timeout=None, headers=None, params=None):
        """Attempts to run the model that is currently loaded into the
        modelrunner application at the current URI, using the inputs
        provided.

        @param inputs A dictionary of inputs that correspond to tensors
        within the model.
        @param outputs A list of tensor names that exist within the model
        that the user wants to have returned as tensors from the modelrunner.
        @param timeout A timeout value to provide to the post request.
        @return Given that outputs is not None, a dictionary of the tensor
        names and their associated tensors."""

        runner_outs = {}
        if self.uri is None:
            raise RuntimeError('No URI is specified for the ModelClient')
        if inputs is None:
            if outputs:
                params['output'] = outputs
            if not headers:
                headers = {'Accept': 'application/json'}
            start_time = default_timer()
            if 'run' not in params or params['run'] == 0:
                r = self.session.post(self.uri, params=params, headers=headers,
                                      timeout=180)
            else:
                r = self.session.post(self.uri, params=params, headers=headers,
                                      timeout=params['run'] * 180)
            try:
                data = r.json()
            except JSONDecodeError:
                raise RuntimeError('ModelRunner Error: %s' % r.text)

            self.post_time = (default_timer() - start_time)
            if 'timing' in data:
                self.raw_time = data['timing']
                self.eval_time = data['timing'] / 1e9
            else:
                self.eval_time = 0.0

            if 'timings' in data:
                self.decode_time = data['timings'].get('decode', 0)
                self.input_time = data['timings'].get('input', 0)
                self.output_time = data['timings'].get('output', 0)
            else:
                self.decode_time = 0
                self.input_time = 0
                self.output_time = 0

        elif isinstance(inputs, dict):
            for key, val in inputs.items():
                inputs[key] = self.__tensor_multipart(val)

            if not params:
                params = {'run': 1}
            if outputs:
                params['output'] = outputs
            if not headers:
                headers = {'Accept': 'application/json'}

            start_time = default_timer()
            try:
                if 'run' not in params or params['run'] == 0:
                    r = self.session.post(self.uri, files=inputs, params=params,
                                          headers=headers, timeout=180)
                else:
                    r = self.session.post(self.uri, files=inputs, params=params,
                                          headers=headers, timeout=120 * params['run'] * 1.5)
            except Timeout as e:
                raise RuntimeError("Timeout Error: %s" % str(e))
            try:
                data = r.json()
            except JSONDecodeError:
                raise RuntimeError('ModelRunner Error: %s' % r.text)

            if 'timings' in data:
                self.decode_time = data['timings'].get('decode', 0)
                self.input_time = data['timings'].get('input', 0)
                self.output_time = data['timings'].get('output', 0)
            else:
                self.decode_time = 0
                self.input_time = 0
                self.output_time = 0

        elif isinstance(inputs, str):
            if not params:
                params = {'run': 1, 'imgproc': 'normalize'}
            if outputs:
                params['output'] = outputs
            if not headers:
                headers = {'Content-Type': 'image/jpg',
                           'Accept': 'application/json'}
            if not isfile(inputs):
                raise FileNotFoundError(
                    "%s is not a valid path to an image" % inputs)
            if 'Accept' not in headers:
                raise KeyError(
                    "Please specify an acceptance type ('application/json', 'text/plain')")
            if headers['Accept'] not in ['application/json', 'text/plain']:
                raise ValueError(
                    "The Accept header must be one of ('application/json', 'text/plain')")

            data = open(inputs, 'rb').read()
            start_time = default_timer()
            try:
                r = self.session.post(self.uri, data=data, params=params,
                                      headers=headers, timeout=120 * params['run'] * 1.5)
            except Timeout as e:
                raise RuntimeError("Timeout Error: %s" % str(e))
            if headers['Accept'] == 'text/plain':
                self.post_time = (default_timer() - start_time)
                m = self.session.get(self.uri + '/model')
                try:
                    data = m.json()
                except JSONDecodeError:
                    raise RuntimeError('ModelRunner Error: %s' % m.text)
                if 'timing' in data:
                    self.raw_time = data['timing']
                    self.eval_time = data['timing'] / 1000000000
                else:
                    self.eval_time = 0.0

                if 'timings' in data:
                    self.decode_time = data['timings'].get('decode', 0)
                    self.input_time = data['timings'].get('input', 0)
                    self.output_time = data['timings'].get('output', 0)
                else:
                    self.decode_time = 0
                    self.input_time = 0
                    self.output_time = 0

                return r.text

            try:
                data = r.json()
            except JSONDecodeError:
                raise RuntimeError('ModelRunner Error: %s' % r.text)

        self.post_time = (default_timer() - start_time)
        if 'timing' in data:
            self.raw_time = data['timing']
            self.eval_time = data['timing'] / 1000000000
        else:
            self.eval_time = 0.0

        if 'outputs' in data:
            for output in data['outputs']:
                if 'data' in output:
                    d = decodebytes(output['data'].encode('utf-8'))
                    t = np.frombuffer(
                        d, dtype=self.tensor_dtype[output['datatype']])

                    if 'shape' in output:
                        runner_outs[output['name']] = t.reshape(
                            output['shape'])
                    else:
                        runner_outs[output['name']] = t

        return runner_outs


def main():
    parser = ArgumentParser(description='DeepView ModelClient')
    parser.add_argument(
        'uri', help='URI of target where modelrunner is being executed')
    parser.add_argument('--model', '-m', help='Filepath to RTM/tflite file')
    parser.add_argument('--images', help='Path to image files or folder')
    parser.add_argument('--imgproc', default='normalize',
                        help='The normalization method to use for each image. Use none for quant models')
    parser.add_argument(
        '--labels', '-l', help='Labels txt for tflite models. RTMs will use embedded labels')
    parser.add_argument('--input-quant-scale',
                        help='Input quantization scale to use when not provided by the model (default: %.6f)' %
                             ModelClient.default_input_quant_scale)
    parser.add_argument('--input-zero-point',
                        help='Input quantization zero point, for signed integer input this value will be reduced by 128 (default: %d)' %
                             ModelClient.default_input_zero_point)
    parser.add_argument('--output-quant-scale',
                        help='Output quantization scale to use when not provided by the model (default: %.6f)' %
                             ModelClient.default_output_quant_scale)
    parser.add_argument('--output-zero-point',
                        help='Output quantization zero point, for signed integer output this value will be reduced by 128 (default: %d)' %
                             ModelClient.default_output_zero_point)
    args = parser.parse_args()

    if args.images:
        images = args.images.split(',')
    else:
        images = args.images

    if args.uri[-3:] != '/v1':
        args.uri = args.uri + '/v1'

    if args.model and not isfile(args.model):
        print("Please enter a valid RTM/tflite file")
        return

    if args.model:
        client = ModelClient(args.uri, args.model)
    else:
        client = ModelClient(args.uri)

    if args.input_quant_scale:
        client.input_quant_scale = args.input_quant_scale
    if args.input_zero_point:
        client.input_zero_point = args.input_zero_point

    if args.output_quant_scale:
        client.output_quant_scale = args.output_quant_scale
    if args.output_zero_point:
        client.output_zero_point = args.output_zero_point

    if not args.model.endswith('.rtm'):
        if args.labels is not None:
            output = client.run(inputs=args.labels, headers={
                'Content-Type': 'labels/txt', 'Accept': 'text/plain'})
            if output == 'Success':
                print("Uploaded labels to tflite runner")
        else:
            print("Please provide labels for tflite model")
            return

    total_eval_time = 0.0
    num_runs = 0

    if images:
        for image in images:
            try:
                if isfile(image):
                    label = client.run(image, headers={'Content-Type': 'image/jpg', 'Accept': 'text/plain'},
                                       params={'run': 1, 'imgproc': args.imgproc})
                    print("%s gives the output label: %s" % (image, label))
                    put_time, post_time, eval_time = client.get_timing_info()
                    total_eval_time = eval_time
                    num_runs = 1
                elif isdir(image):
                    ims = [f.path for f in os.scandir(image) if f.is_file()]
                    for im in ims:
                        label = client.run(im, headers={'Content-Type': 'image/jpg', 'Accept': 'text/plain'},
                                           params={'run': 1, 'imgproc': args.imgproc})
                        print("%s gives the output label: %s" % (im, label))
                        put_time, post_time, eval_time = client.get_timing_info()
                        total_eval_time = total_eval_time + eval_time
                        num_runs = num_runs + 1
                else:
                    print("%s is not a valid directory or file for images" % image)
            except RuntimeError as e:
                print("%s was unable to run due to error %s" % (image, str(e)))
        print("Average Model runtime: %.4fms" %
              (total_eval_time / num_runs * 1000.0))


if __name__ == '__main__':
    main()
