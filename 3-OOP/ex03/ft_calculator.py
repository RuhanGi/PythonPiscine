import sys


class calculator:
    """Calculator docstring"""
    def __init__(self, vec):
        """Your docstring for Constructor"""
        self.vec = vec

    def __add__(self, object) -> None:
        """Your docstring for addition"""
        try:
            self.vec = [i + object for i in self.vec]
            print(self.vec)
        except Exception as e:
            print("Error: " + str(e))
            sys.exit(1)

    def __mul__(self, object) -> None:
        """Your docstring for multiplication"""
        try:
            self.vec = [i * object for i in self.vec]
            print(self.vec)
        except Exception as e:
            print("Error: " + str(e))
            sys.exit(1)

    def __sub__(self, object) -> None:
        """Your docstring for subtraction"""
        try:
            self.vec = [i - object for i in self.vec]
            print(self.vec)
        except Exception as e:
            print("Error: " + str(e))
            sys.exit(1)

    def __truediv__(self, object) -> None:
        """Your docstring for subtraction"""
        try:
            self.vec = [i / object for i in self.vec]
            print(self.vec)
        except Exception as e:
            print("Error: " + str(e))
            sys.exit(1)
