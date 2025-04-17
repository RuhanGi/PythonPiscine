from ft_filter import ft_filter 
import sys

def myFunc(x):
    if x < 0:
        return False
    else:
        return True

def main():
    """
    This is the main function that drives the program.
    """

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        print(filter(myFunc, [1,-1,0,2,-4]))
    except AssertionError as msg:
        print("AssertionError: ", msg)


if __name__ == "__main__":
    main()
