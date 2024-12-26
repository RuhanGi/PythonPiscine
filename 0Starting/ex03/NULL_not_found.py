def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} <class 'NoneType'>")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} <class 'float'>")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} <class 'bool'>")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} <class 'int'>")
    elif isinstance(object, str) and object == '':
        print("Empty: <class 'str'>")
    else:
        print("Type not Found")
        return 1
    return 0
