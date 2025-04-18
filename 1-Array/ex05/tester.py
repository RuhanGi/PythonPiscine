from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


def plotArr(arr):
    """
    plots image
    """
    plt.imshow(arr)
    plt.gcf().canvas.mpl_connect(
        'key_press_event',
        lambda event: plt.close() if event.key == 'escape' else None
    )
    plt.show()


array = ft_load("landscape.jpg")
plotArr(ft_invert(array))
plotArr(ft_red(array))
plotArr(ft_green(array))
plotArr(ft_blue(array))
plotArr(ft_grey(array))
print(ft_invert.__doc__)
