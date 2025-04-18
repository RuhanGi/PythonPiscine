from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def trans(img):
    """
    Zooms in and grayscales it
    """
    img = img[100:500, 450:850]
    h, w, c = img.shape

    transpose = np.zeros((w, h, c), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            transpose[j, i, :] = img[i, j, :]

    print(f"New shape after Transpose: ({h}, {w}, {c})")
    return transpose


def main():
    """
    Loads the image "animal.jpeg", prints some information
    Display it after "zooming".
    """

    try:
        img = ft_load("animal.jpeg")
        print(img)
        final = trans(img)
        print(final)
        plt.imshow(final)
        plt.gcf().canvas.mpl_connect(
            'key_press_event',
            lambda event: plt.close() if event.key == 'escape' else None
        )
        plt.show()
    except Exception as e:
        print("Error: " + str(e))


if __name__ == "__main__":
    main()
