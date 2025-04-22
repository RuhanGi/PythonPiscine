def square(x: int | float) -> int | float:
    """Calculates square of a number"""
    try:
        return x**2
    except Exception as e:
        print("Error: " + str(e))


def pow(x: int | float) -> int | float:
    """Calculates number raised to itself"""
    try:
        return x**x
    except Exception as e:
        print("Error: " + str(e))


def outer(x: int | float, function) -> object:
    """Returns the inner function"""
    count = 0

    def inner() -> float:
        """Iterable inner function"""
        nonlocal count, x
        count += 1
        x = function(x)
        return x

    return inner
