import numpy as np


def ft_invert(array) -> list:
    """
    Inverts the color of the image received.
    """
    result = array.copy()
    result[:, :, :] = 255 - array[:, :, :]
    return result


def ft_red(array) -> list:
    """
    Extracts the red color of the image received.
    """
    result = array.copy()
    result[:, :, 1:3] = 0
    return result


def ft_green(array) -> list:
    """
    Extracts the green color of the image received.
    """
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 2] = 0
    return result


def ft_blue(array) -> list:
    """
    Extracts the blue color of the image received.
    """
    result = array.copy()
    result[:, :, 0:2] = 0
    return result


def ft_grey(array) -> list:
    """
    Takes the grayscale of the image received.
    """
    gray = array.mean(axis=2).astype(np.uint8)
    h, w = gray.shape
    out = np.zeros((h, w, 3), dtype=np.uint8)
    out[:, :, 0] = gray
    out[:, :, 1] = gray
    out[:, :, 2] = gray
    return out
