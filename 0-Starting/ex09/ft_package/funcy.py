def count_in_list(lst, item):
    """
    Count items in lst
    """
    return lst.count(item)


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    i = 0
    n = len(lst)
    for i, c in enumerate(lst):
        p = int(i / n * 100)
        bar = (p//2 * '█') + ((50-p//2) * ' ')
        print(f"\r {p}%|{bar}| {i}/{n}", end="")
        yield c
    print("\r100%|" + 50*'█' + f"| {n}/{n}", end="")


def ft_filter(function, iterable):
    """
ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    if function is None:
        return (a for a in iterable if a)
    return (a for a in iterable if function(a))


def NULL_not_found(object: any) -> int:
    """
    Check NULL type
    """
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
