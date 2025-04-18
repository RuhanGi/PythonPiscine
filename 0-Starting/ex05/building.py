import string
import sys


def main():
    """
    Takes a single string argument and displays the sums of its upper-case
    characters, lower-case characters, punctuation characters, digits, spaces.
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

        upp = sum(1 for char in line if char.isupper())
        low = sum(1 for char in line if char.islower())
        pun = sum(1 for char in line if char in string.punctuation)
        spa = sum(1 for char in line if char.isspace())
        dig = sum(1 for char in line if char.isdigit())
        print(f"The text contains {upp+low+pun+spa+dig} characters:")
        print(f"{upp} upper letters")
        print(f"{low} lower letters")
        print(f"{pun} punctuation marks")
        print(f"{spa} spaces")
        print(f"{dig} digits")
    except AssertionError as msg:
        print("AssertionError: ", msg)


if __name__ == "__main__":
    main()
