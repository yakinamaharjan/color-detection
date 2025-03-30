import numpy as np
import pandas as pd
import cv2

df = pd.read_csv("color_names.csv")

df = df[['Name', 'Red (8 bit)', 'Green (8 bit)', 'Blue (8 bit)']]

def get_color_name(r, g, b):
    """Find the closest color from the dataset."""
    distances = np.sqrt((df['Red (8 bit)'] - r) ** 2 +
                        (df['Green (8 bit)'] - g) ** 2 +
                        (df['Blue (8 bit)'] - b) ** 2)
    return df.loc[distances.idxmin(), 'Name']


# def get_color_name(hsv_pixel):
#     """Determine the color name based on HSV value."""
#     hsv_pixel = np.array(hsv_pixel, dtype=np.uint8)  # Ensure it's a NumPy array
#     for color, (lower, upper) in color_ranges.items():
#         lower = np.array(lower, dtype=np.uint8)
#         upper = np.array(upper, dtype=np.uint8)
#         if all(lower <= hsv_pixel) and all(hsv_pixel <= upper):  # Fix condition check
#             return color
#     return "Unknown"