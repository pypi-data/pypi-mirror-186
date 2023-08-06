import numpy as np


def cal_area_of_boxes(boxes, is_sorted=True):
    """
        计算体积
    """
    if boxes is not None:
        if not is_sorted:
            boxes = np.sort(boxes, axis=1)
        area = sum([(box[1] - box[0]).prod() for box in boxes])
    else:
        area = 0
    return area
