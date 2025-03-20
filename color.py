import numpy as np
import cv2

color_ranges = {
    "Red": [(0, 120, 70), (10, 255, 255)],
    "Green": [(40, 40, 40), (80, 255, 255)],
    "Blue": [(100, 150, 0), (140, 255, 255)],
    "Yellow": [(20, 100, 100), (30, 255, 255)],
    "Orange": [(10, 100, 100), (20, 255, 255)],
    "Purple": [(130, 50, 50), (160, 255, 255)],
    "White": [(0, 0, 200), (180, 30, 255)],
    "Black": [(0, 0, 0), (180, 255, 30)]
}

def get_color_name(hsv_pixel):
    """Determine the color name based on HSV value."""
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        if cv2.inRange(np.array([[hsv_pixel]], dtype=np.uint8), lower, upper):
            return color
    return "Unknown"