from typing import List, Optional, Tuple

import numpy
from ..tensor import Tensor
from ..context import Context
from ..errors import check_error
from ..librt import ffi, lib
import math

ANCHOR_CORNER = 0
ANCHOR_CENTROID = 1
ANCHOR_VARIANCE = 2



Bounding_Box_Coordinate = Tuple[float, float, float, float]
"""
The normalized coordinates of the bounding box of a detection. The coordinates are given as 
`(corner0.x, corner0.y, corner2.x, corner2.y)`, where corner0 is the top left, and corner2 is the bottom right.
"""

Detection = Tuple[str, Bounding_Box_Coordinate, float]
"""
A single detection of an ssd detection model. Contains the label (`str`), bounding box coordinates 
(`tuple(float, float, float, float)`), and score (`float`)
"""

def get_bounding_box(context:Context, anchor_type:Optional[int]=None, iou=0.5, max_boxes=50, threshold=0.5)-> List[Detection]:
    """
    Retrieves the detections from an SSD image detection model, parses the results and returns it as a list

    Parameters:
    ----------
    context: Context
        The DeepViewRT Context to get the bounding box detections for. It should already have
        an SSD detection model loaded, with image data loaded into the input tensor and inference with
        `Context.run()`

    anchor_type: Optional[int]
        The expected SSD anchor type of the model loaded in the DeepViewRT Context. If `None`, the anchor
        type will be automatically calculated

    iou: float
        The IoU threshold for NMS in the range 0..1

    max_boxes: int
        The maximum number of bounding boxes

    threshold: float
        Threshold for valid boxes in the range of 0..1

    Returns:
    ----------
    results: List[Detection]
        The results are returned as list of Detections.

        The Detection tuple is (label, bbox_coordinates, score).

        The bounding box coordinates are normalized between 0 to 1. The coordinates are given as 
        `(corner0.x, corner0.y, corner2.x, corner2.y)`, where `corner0` is the top left, and `corner2`
        is the bottom right.
    """
    import sys
    results = []

    # The SSD anchor box definitions are expected to be in a tensor named
    # ssd_anchor_boxes 
    anchor = context.tensor("ssd_anchor_boxes")
    if anchor is None:
        raise ValueError('Did not find "ssd_anchor_boxes" tensor')

    cache_tensor = context.cache_tensor()

    # If using an engine plugin, get a seperate cache for the box decoding
    # This is because the model's cache tensor is on the NPU when using an
    # engine plugin, but box decoding runs on the CPU
    if context.engine:
        cache_tensor = Tensor(shape = (context.cache_size,), dtype=numpy.uint8)

    # Calculate the anchor type. If the provided anchor type is different
    # than the calculated type, warn the user
    if anchor_type is None:
        anchor_type = calculate_anchor_type(context, anchor)
    else:
        if anchor_type != calculate_anchor_type(context, anchor):
            print(f"WARNING: Provided anchor type may be incorrect", file=sys.stderr)
    set_anchor_type(anchor, anchor_type)

    # Corner and centroid models have 2 outputs, one for the bounding box, and another for scores.
    # Output shapes should be used to determine ordering. Edge case when the number of classes is 4
    # requires manually swapping the tensors
    output_indices = context.outputs
    if anchor_type == ANCHOR_CORNER or anchor_type == ANCHOR_CENTROID:
        if len(output_indices) != 2:
            raise ValueError('anchor_type incorrect. This model type should have 2 outputs')
        trans_tensor = context.tensor(output_indices[0])
        score_tensor = context.tensor(output_indices[1])
        if not trans_tensor:
            raise ValueError('anchor_type incorrect. Could not find trans output tensor')
        if not score_tensor:
            raise ValueError('anchor_type incorrect. Could not find score output tensor')

        # swapping tensors when number of classes is 4
        if score_tensor.dims == 4 or score_tensor.shape[2] == 4:
            swap = score_tensor
            score_tensor = trans_tensor
            trans_tensor = swap
        if score_tensor.shape[2] == trans_tensor.shape[2]:
            print(f"WARNING: Unable to determine output tensors for decoding, results may be incorrect", file=sys.stderr)

        n_classes = score_tensor.shape[2]

    # Variance models (these are created by eIQ Portal) have 1 combined output, which is created by
    # concatenating the trans and score tensors.
    elif anchor_type == ANCHOR_VARIANCE:
        if len(output_indices) != 1:
            raise ValueError('anchor_type incorrect. This model type should have 1 output')
        prediction_tensor = context.tensor(output_indices[0])
        if not prediction_tensor:
            raise ValueError('anchor_type incorrect. Could not find prediction output tensor')
        n_classes = prediction_tensor.shape[2] - 4
    else:
        raise ValueError("anchor_type invalid")


    # Decode the output and get the bounding boxes based on the anchor type.
    # The boxes tensor holds the information about the bounding boxes detected,
    # and the classed_found tensor contains the number of detections of each class
    # Based on the anchor type we call different decoders
    if anchor_type == ANCHOR_CORNER or anchor_type == ANCHOR_CENTROID:
        boxes, classes_found = decode_nms_standard_bbx(
            score_tensor,
            trans_tensor,
            anchor,
            cache_tensor,
            n_classes,
            threshold,
            iou,
            max_boxes
        )
    elif anchor_type == ANCHOR_VARIANCE:
        boxes, classes_found = decode_nms_variance_bbx(
            prediction_tensor,
            anchor,
            cache_tensor,
            n_classes,
            threshold,
            iou,
            max_boxes,
        )

    # The decoders store the results in a `data_score_out` auxiliary object.
    # Here we read the data to later print out
    box_scores = boxes.get_aux_object("data_score_out", ntype = "float")
    boxes_data = boxes.map_read("float")
    classes_found_data = classes_found.map_read("int")


    label_offset = calculate_label_offset(context, anchor_type)

    start =  1 if anchor_type == ANCHOR_VARIANCE else 0 
    end =  n_classes - (0 if anchor_type == ANCHOR_VARIANCE else 1)

    # The detections are organized by class. the classes_found_data stores the number of detections 
    # for each class. The data is arranged in continuous sections, and the offset for each detection
    # is computed with the tensor_offset function.

    # For each detection, the boxes_data holds the (ymin, xmin, ymax, xmax) data, in that order. It
    # is reorganized to be (xmin, ymin, xmax, ymax) here.
    # The score is computed from the overlap.
    for k in range(start, end):

        # Get the class label, if embedded in the model. Otherwise just use the index
        if k+label_offset < context.label_count():
            class_label = context.labels()[k+label_offset]
        else:
            class_label = str(k+label_offset)

        # Iterate through the results for the class
        for j in range(classes_found_data[k]):
            offset = boxes.tensor_offset(3, k, j, 0)
            score = 1.0 / (1.0 + math.exp(-1.0 * box_scores[j + k * max_boxes]))
            # Append the decoded result into the results list
            results.append( 
                (
                    class_label,
                    (
                        boxes_data[offset + 1],
                        boxes_data[offset + 0],
                        boxes_data[offset + 3],
                        boxes_data[offset + 2]
                    ),
                    score
                ))
    return results


def decode_nms_standard_bbx(score_tensor:Tensor, trans_tensor:Tensor, anchor_tensor:Tensor, cache_tensor:Tensor, n_classes:int, threshold=0.5, iou=0.5, max_boxes=50) -> Tuple[Tensor, Tensor]:
    """
    Decodes the results for a standard anchor type SSD model.

    Returns
    ----------
        boxes tensor: Tensor
            holds the information about the bounding boxes detected,
        classes_found: Tensor
            contains the number of detections of each class
    """
    boxes = Tensor(shape=[n_classes, max_boxes, 4])
    classes_found = Tensor(shape=[n_classes, 1])

    err = lib.nn_ssd_decode_nms_standard_bbx(
        score_tensor.ptr,
        trans_tensor.ptr,
        anchor_tensor.ptr,
        cache_tensor.ptr,
        math.log(threshold/(1.0-threshold)),
        iou,
        max_boxes,
        boxes.ptr,
        classes_found.ptr
        )
    if err:
        check_error(err)
    return boxes, classes_found

def decode_nms_variance_bbx(prediction_tensor:Tensor, anchor_tensor:Tensor, cache_tensor:Tensor, n_classes:int, threshold=0.5, iou=0.5, max_boxes=50) -> Tuple[Tensor, Tensor]:
    """
    Decodes the results for a variance anchor type SSD model.

    Returns
    ----------
        boxes tensor: Tensor
            holds the information about the bounding boxes detected,
        classes_found: Tensor
            contains the number of detections of each class
    """
    boxes = Tensor(shape=[n_classes, max_boxes, 4])
    classes_found = Tensor(shape=[n_classes, 1])
    err = lib.nn_ssd_decode_nms_variance_bbx(
        prediction_tensor.ptr,
        anchor_tensor.ptr,
        cache_tensor.ptr,
        math.log(threshold/(1.0-threshold)),
        iou,
        max_boxes,
        boxes.ptr,
        classes_found.ptr
    )
    if err:
        check_error(err)
    return boxes, classes_found

def calculate_anchor_type(context:Context, anchors:Tensor):
    """
    Returns
    ----------
        anchor_type: int
            the calculated anchor type for the Context
    """
    num_anchors = anchors.shape[0]
    num_outputs = len(context.outputs)

    anc_type = ANCHOR_VARIANCE
    # TF 1.x v1/v2 and TF 2.x v2_300x300
    if num_anchors == 1917:
        anc_type = ANCHOR_CORNER
    # eIQ SSD
    elif num_outputs == 1:
        anc_type = ANCHOR_VARIANCE
    # TF 1.x v3 and other TF 2.x SSD
    else:
        anc_type = ANCHOR_CENTROID
    return anc_type


def set_anchor_type(anchor:Tensor, anc_type:int):
    """
    Sets the aux object "anchor_type" to the type given
    """
    anchor.set_aux_object("anchor_type", [anc_type], "int32_t")


def calculate_label_offset(context:Context, anchor_type):
    if anchor_type == ANCHOR_CENTROID:
        if 0 < len(context.labels()):
            label = context.labels()[0]
            return 1 if label == 'Background' else 0
    return 0

def c_str(py_str:str):
    return py_str.encode("ASCII")

def py_str(c_str):
    try:
        return ffi.string(c_str).decode("ASCII")
    except:
        return None