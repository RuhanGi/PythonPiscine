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
