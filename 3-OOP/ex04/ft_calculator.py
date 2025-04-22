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

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Your docstring for dotproduct"""
        try:
            assert len(V1) == len(V2), "vectors not same size"
            print("Dot product is: ", end="")
            print(sum([i * j for i, j in zip(V1, V2)]))
        except Exception as e:
            print("Error: " + str(e))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Your docstring for addition of vectors"""
        try:
            assert len(V1) == len(V2), "vectors not same size"
            print("Add Vector is : " + str([i + j for i, j in zip(V1, V2)]))
        except Exception as e:
            print("Error: " + str(e))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Your docstring for subtraction of vectors"""
        try:
            assert len(V1) == len(V2), "vectors not same size"
            print("Sous Vector is: " + str([i - j for i, j in zip(V1, V2)]))
        except Exception as e:
            print("Error: " + str(e))
