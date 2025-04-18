import os


def make():
    os.system("python setup.py sdist bdist_wheel > /dev/null 2>&1")
    os.system("pip3 install ./dist/ft_package-0.0.1.tar.gz >\
                  /dev/null 2>&1")


if __name__ == "__main__":
    make()
