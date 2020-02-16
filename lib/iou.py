__all__ = ['get_iou']


# Format of box pts: (xMin, yMin, xMax, yMax)

def _intersection(boxA_pts, boxB_pts):
    xMin_A, yMin_A, xMax_A, yMax_A = boxA_pts
    xMin_B, yMin_B, xMax_B, yMax_B = boxB_pts
    assert xMin_A <= xMax_A and yMin_A <= yMax_A, 'boxA_pts is wrong.'
    assert xMin_B <= xMax_B and yMin_B <= yMax_B, 'boxB_pts is wrong.'
    
    x = max(xMin_A, xMin_B)
    y = max(yMin_A, yMin_B)
    w = min(xMax_A, xMax_B) - x
    h = min(yMax_A, yMax_B) - y
    
    area_intersection = (w * h) if (w >= 0 and h >= 0) else 0.0
    return float(area_intersection)


def _union(boxA_pts, boxB_pts):
    xMin_A, yMin_A, xMax_A, yMax_A = boxA_pts
    xMin_B, yMin_B, xMax_B, yMax_B = boxB_pts
    assert xMin_A <= xMax_A and yMin_A <= yMax_A, 'boxA_pts is wrong.'
    assert xMin_B <= xMax_B and yMin_B <= yMax_B, 'boxB_pts is wrong.'
    
    area_A = (xMax_A - xMin_A) * (yMax_A - yMin_A)
    area_B = (xMax_B - xMin_B) * (yMax_B - yMin_B)
    
    area_union = (area_A + area_B) - _intersection(boxA_pts, boxB_pts)
    return float(area_union)


def get_iou(boxA_pts, boxB_pts, epsilon=True):
    e = 1e-8 if epsilon else 0.0
    
    area_intersection = _intersection(boxA_pts, boxB_pts)
    area_union = _union(boxA_pts, boxB_pts)

    iou = area_intersection / (area_union + e)
    return float(iou)
