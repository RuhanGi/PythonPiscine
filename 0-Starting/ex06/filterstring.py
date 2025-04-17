import sys


def main():
    """
    This is the main function that drives the program.
    """

    try:
        assert len(sys.argv) == 3, "more two arguments required"
        assert N = sys.argv[2], "second argument must be an integer"
        
        strs = sys.argv[1].split()
        checkLen = lambda string, n: len(string) > n
        print(a for a in strs if checkLen(a, N))
        
    except AssertionError as msg:
        print("AssertionError: ", msg)


if __name__ == "__main__":
    main()
