import os


def uninstall():
    """
    Cleans the package folders and uninstalls it
    """
    os.system("rm -rf build dist ft_package.egg-info ft_package/__pycache__")
    os.system("pip3 uninstall -y ft_package")


if __name__ == "__main__":
    uninstall()
