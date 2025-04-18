import sys


def check(line):
    return all(c.isalnum() or c.isspace() for c in line)


def main():
    """
    A program that takes a string as an argument and encodes it into Morse Code
    - Supports space and alphanumeric characters
    - Complete morse characters are separated by a single space
    - A space character is represented by a slash /
    """

    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        line = sys.argv[1]
        assert check(line), "the arguments are bad"
        line = line.upper()
        print(*[NESTED_MORSE[c] for c in line])
    except AssertionError as e:
        print("AssertionError: " + str(e))


if __name__ == "__main__":
    main()
