from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    """
    Loads an image, prints its format, and its pixels
    content in RGB format.
    """
    try:
        img = Image.open(path)
        if img is not None:
            h, w = img.size
            modech = {
                "1": 1,        # 1-bit pixels, black and white
                "L": 1,        # 8-bit pixels, grayscale
                "RGB": 3,      # Red, Green, Blue
                "RGBA": 4,     # RGB + Alpha
                "CMYK": 4,     # Cyan, Magenta, Yellow, Black
                "YCbCr": 3,    # Luminance, Chrominance
            }
            c = modech[img.mode]
            print(f"The shape of image is: ({h}, {w}, {c})")
        return np.asarray(img)
    except Exception as e:
        print("Error: " + str(e))
        return []
