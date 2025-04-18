from matplotlib.image import imread


def ft_load(path: str) -> list:
    """
    Loads an image, prints its format, and its pixels
    content in RGB format.
    """
    try:
        img = imread(path)
        if img is not None:
            h, w, c = img.shape
            print(f"The shape of image is: ({h}, {w}, {c})")
        return img
    except Exception as e:
        print("Error: " + str(e))
        return []
