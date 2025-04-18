import string
import sys


def main():
    """
    This is the main function that drives the program.
    """

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1 or sys.argv[1] in [None, ""]:
            try:
                line = input("What is the text to count?\n")
            except Exception as e:
                print("No text found! " + str(e))
                sys.exit(0)
        else:
            line = sys.argv[1]

        print(f"The text contains {len(line)} characters:")
        print(f"{sum(1 for char in line if char.isupper())} upper letters")
        print(f"{sum(1 for char in line if char.islower())} lower letters")
        punc = sum(1 for char in line if char in string.punctuation)
        print(f"{punc} punctuation marks")
        print(f"{sum(1 for char in line if char.isspace())} spaces")
        print(f"{sum(1 for char in line if char.isdigit())} digits")
    except AssertionError as msg:
        print("AssertionError: ", msg)


if __name__ == "__main__":
    main()
