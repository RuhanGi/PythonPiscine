import sys


def isInt(num: str) -> bool:
    if num[0] == '-':
        return num[1:].isdigit()
    return num.isdigit()


try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if len(sys.argv) == 2:
        assert isInt(sys.argv[1]), "argument is not an integer"
        n = int(sys.argv[1])
        print("I'm Odd." if n % 2 else "I'm Even.")
except AssertionError as msg:
    print("AssertionError:", msg)
