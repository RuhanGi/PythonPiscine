from load_image import ft_load
import matplotlib.pyplot as plt


def zoom(img):
    """
    Zooms in and grayscales it
    """
    final = img[100:500, 450:850, 0:3]
    h, w, c = final.shape
    print(f"New shape after slicing: ({h}, {w}, {c})")
    return final


def main():
    """
    Loads the image "animal.jpeg", prints some information
    Display it after "zooming".
    """

    try:
        img = ft_load("animal.jpeg")
        print(img)
        final = zoom(img)
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
