def isNum(lst: list[int | float]) -> bool:
    """
    Checks that all items are either int or float
    """
    return all(isinstance(c, (int, float)) for c in lst)


def give_bmi(height: list[int | float], weight: list[int | float]) \
 -> list[int | float]:
    """
    Takes 2 lists of integers or floats in input
    Returns a list of BMI values
    """
    try:
        assert len(height) == len(weight), "lists not the same size"
        assert isNum(height) and isNum(weight), "non-numerical list"
        return [w/h**2 for h, w in zip(height, weight)]
    except AssertionError as e:
        print("AssertionError: " + str(e))
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Accepts a list of integers or floats and an integer representing
    a limit as parameters and returns booleans above limit or not
    """
    try:
        assert isNum(bmi), "non-numerical list"
        return [b > limit for b in bmi]
    except AssertionError as e:
        print("AssertionError: " + str(e))
        return []
