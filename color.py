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