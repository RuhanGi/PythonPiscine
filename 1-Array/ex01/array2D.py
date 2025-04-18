def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes as parameters a 2D array, prints its shape
    Returns a truncated version of the array
    """
    try:
        assert family, "Empty Array"
        rows = len(family)
        assert all(isinstance(row, list) for row in family), "1D array found"
        cols = len(family[0])
        assert all(len(c) == cols for c in family), "mismatch"

        print(f"My shape is : ({rows}, {cols})")
        x = family[slice(start, end)]
        print(f"My new shape is : ({len(x)}, {cols})")
        return x
    except AssertionError as e:
        print("AssertionError: " + str(e))
        return []
