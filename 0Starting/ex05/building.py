import sys

def main():
    """
    This is the main function that drives the program.
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        string = sys.argv[1] if len(sys.argv) == 2 else input("What is the text to count?\n")
        print(f"The text contains {len(string)} characters:")
        print(f"{sum(1 for char in string if char.isupper())} upper letters")
        print(f"{sum(1 for char in string if char.islower())} lower letters")
        punc = "!\"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"
        print(f"{sum(1 for char in string if char in punc)} punctuation marks")
        print(f"{sum(1 for char in string if char.isspace())} spaces")
        print(f"{sum(1 for char in string if char.isdigit())} digits")
    except AssertionError as msg:
        print("AssertionError:", msg)

if __name__ == "__main__":  
    main()