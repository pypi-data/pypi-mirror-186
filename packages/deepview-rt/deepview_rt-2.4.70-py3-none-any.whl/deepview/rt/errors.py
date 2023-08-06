# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from .librt import lib
from .common import strerror


class Error(Exception):
    """
    Error provides the base Exception class for DeepViewRT.  All common errors
    subclass this class to provide specific NNError to Python Exception maps.
    The underlying NNError code can be read from Error.code() and the human
    readable string can be read using Error.error_string().
    """

    def __init__(self, code=lib.NN_ERROR_INTERNAL, message=None):
        if message is None:
            message = strerror(code)
        super(Error, self).__init__(message)
        self.code = code

    def error_string(self):
        return strerror(self.code)


class InternalError(Error):
    def __init__(self, message=None):
        super(InternalError,
              self).__init__(lib.NN_ERROR_INTERNAL, message)


class InvalidHandleError(Error):
    def __init__(self, message=None):
        super(InvalidHandleError,
              self).__init__(lib.NN_ERROR_INVALID_HANDLE, message)


class OutOfMemoryError(Error):
    def __init__(self, message=None):
        super(OutOfMemoryError,
              self).__init__(lib.NN_ERROR_OUT_OF_MEMORY, message)


class OutOfResourcesError(Error):
    def __init__(self, message=None):
        super(OutOfResourcesError,
              self).__init__(lib.NN_ERROR_OUT_OF_RESOURCES, message)


class NotImplementedError(Error):
    def __init__(self, message=None):
        super(NotImplementedError,
              self).__init__(lib.NN_ERROR_NOT_IMPLEMENTED, message)


class InvalidParameterError(Error):
    def __init__(self, message=None):
        super(InvalidParameterError,
              self).__init__(lib.NN_ERROR_INVALID_PARAMETER, message)


class TypeMismatchError(Error):
    def __init__(self, message=None):
        super(TypeMismatchError,
              self).__init__(lib.NN_ERROR_TYPE_MISMATCH, message)


class ShapeMismatchError(Error):
    def __init__(self, message=None):
        super(ShapeMismatchError,
              self).__init__(lib.NN_ERROR_SHAPE_MISMATCH, message)


class InvalidShapeError(Error):
    def __init__(self, message=None):
        super(InvalidShapeError,
              self).__init__(lib.NN_ERROR_INVALID_SHAPE, message)


class InvalidOrderError(Error):
    def __init__(self, message=None):
        super(InvalidOrderError,
              self).__init__(lib.NN_ERROR_INVALID_ORDER, message)


class InvalidAxisError(Error):
    def __init__(self, message=None):
        super(InvalidAxisError,
              self).__init__(lib.NN_ERROR_INVALID_AXIS, message)


class MissingResourceError(Error):
    def __init__(self, message=None):
        super(MissingResourceError,
              self).__init__(lib.NN_ERROR_MISSING_RESOURCE, message)


class InvalidEngineError(Error):
    def __init__(self, message=None):
        super(InvalidEngineError,
              self).__init__(lib.NN_ERROR_INVALID_ENGINE, message)


class TensorNoDataError(Error):
    def __init__(self, message=None):
        super(TensorNoDataError,
              self).__init__(lib.NN_ERROR_TENSOR_NO_DATA, message)


class KernelMissingError(Error):
    def __init__(self, message=None):
        super(KernelMissingError,
              self).__init__(lib.NN_ERROR_KERNEL_MISSING, message)


class TensorTypeUnsupportedError(Error):
    def __init__(self, message=None):
        super(TensorTypeUnsupportedError,
              self).__init__(lib.NN_ERROR_TENSOR_TYPE_UNSUPPORTED, message)


class TooManyInputs(Error):
    def __init__(self, message=None):
        super(TooManyInputs,
              self).__init__(lib.NN_ERROR_TOO_MANY_INPUTS, message)


class ShapePropagationError(Exception):
    """
    Traces up to last known node for each unknown node and stores the nodes
    in a dict of dicts. Key for outer dict is the failed shape prop node
    name and the value is a dict containing that node's inputs (probably
    unknown nodes) Key for inner dict is the unknown node's name and the
    value is that node's info. e.g. if shape prop fails on node y,
    then node_traceback[y] will be a dict containing y's inputs, say x_1,
    x_2, ... if x_i is an unknown node, then node_traceback[x_i] will be
    x_i's inputs and so on until there is a known layer
    """

    def __init__(self, nxgraph, node_name, get_subgraph=False,
                 draw_subgraph=True):
        """
        Constructor
        :param nxgraph: Graph containing model up to the error point
        :param node_name: Name of node where shape propagation error occured
        :param get_subgraph: Boolean to get subgraph of unknown nodes
        :param draw_subgraph: Boolean to plot graph of unknown nodes
        """
        import networkx as nx
        self.node_traceback = {}
        self.unknown_nodes = [node_name]
        self.subgraph = nx.OrderedDiGraph()

        if get_subgraph or draw_subgraph:
            self.get_subgraph(nxgraph, node_name)
            if draw_subgraph:
                self.draw_subgraph(nxgraph)

        print("Printing traceback to last known node:")
        self.find_known_node(nxgraph, node_name)

    def draw_subgraph(self, nxgraph):
        """
        Draws subgraph of unknown nodes using matplotlib
        :param nxgraph: Subgraph of unknown nodes
        :return:
        """
        try:
            import matplotlib.pyplot as plt
        except ModuleNotFoundError:
            raise UserWarning("Install matplotlib to see graph error visualization")
        import networkx as nx

        colors = []
        # Assign colors for each node in subgraph
        for i, (node, data) in enumerate(self.subgraph.nodes(data=True)):
            data = data['attr_dict']
            if i == 0:  # Node where failure occurs
                colors.append('r')
            elif 'op' in data and data['op'] == 'unknown':  # Unknown node
                colors.append('black')
            else:  # Other nodes
                colors.append('b')

        ops = {}
        for nodes in self.subgraph:
            if 'op' in nxgraph.nodes[nodes]:
                ops[nodes] = nxgraph.nodes[nodes]['op']
        pos = nx.spring_layout(self.subgraph)
        nx.draw_networkx(self.subgraph, pos=pos, node_color=colors,
                         font_color='orange')
        for val in pos.values():
            val[1] += 0.1
        nx.draw_networkx_labels(self.subgraph, pos=pos, labels=ops)
        plt.show()

    def get_subgraph(self, nxgraph, node_name):
        """
        Generates subgraph of unknown nodes recursively
        :param nxgraph: Graph of entire model up to failure point
        :param node_name: Name of failure node
        :return:
        """
        pred = nxgraph.predecessors(node_name)

        self.subgraph.add_node(node_name, attr_dict=nxgraph.nodes[node_name])
        for pred_name in pred:
            pred_node = nxgraph.nodes[pred_name]
            self.subgraph.add_node(pred_name, attr_dict=pred_node)
            self.subgraph.add_edge(pred_name, node_name)

        pred = nxgraph.predecessors(node_name)
        recurse_nodes = []
        for pred_name in pred:
            pred_node = nxgraph.nodes[pred_name]
            if 'op' in pred_node and pred_node['op'] == 'unknown':
                recurse_nodes.append(pred_name)

        for node in recurse_nodes:
            self.get_subgraph(nxgraph, node)

    def find_known_node(self, nxgraph, node_name):
        """
        Generate dict recursively from failure node to last known node
        :param nxgraph: Graph of entire model up to failure point
        :param node_name: Name of failure node
        :return:
        """
        pred = nxgraph.predecessors(node_name)

        nodes = {}
        for pred_name in pred:
            pred_node = nxgraph.nodes[pred_name]
            nodes[pred_name] = pred_node
        self.node_traceback[node_name] = nodes
        print(self.node_traceback[node_name])

        pred = nxgraph.predecessors(node_name)
        for pred_name in pred:
            pred_node = nxgraph.nodes[pred_name]
            if 'op' in pred_node and pred_node['op'] == 'unknown':
                self.unknown_nodes += pred_name
                self.find_known_node(nxgraph, pred_name)


def check_error(code, message=None):
    if code == lib.NN_SUCCESS:
        return None

    raise {
        1: InternalError(message),
        2: InvalidHandleError(message),
        3: OutOfMemoryError(message),
        4: OutOfResourcesError(message),
        5: NotImplementedError(message),
        6: InvalidParameterError(message),
        7: TypeMismatchError(message),
        8: ShapeMismatchError(message),
        9: InvalidShapeError(message),
        10: InvalidOrderError(message),
        11: InvalidAxisError(message),
        12: MissingResourceError(message),
        13: InvalidEngineError(message),
        14: TensorNoDataError(message),
        15: KernelMissingError(message),
        16: TensorTypeUnsupportedError(message),
        17: TooManyInputs(message)
    }[code]
