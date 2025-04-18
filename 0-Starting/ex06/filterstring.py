import sys
from ft_filter import ft_filter


def main():
    """
    A program that accepts two arguments: a string(S), and an integer(N).
    Outputs a list of words from S that have a length greater than N.
    """

    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].isdigit(), "the arguments are bad"
        strs = sys.argv[1].split()
        N = int(sys.argv[2])
        print([w for w in ft_filter(lambda string: len(string) > N, strs)])
    except AssertionError as e:
        print("AssertionError: " + str(e))


if __name__ == "__main__":
    main()
