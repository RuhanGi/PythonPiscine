import numpy as np


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculates statistics"""

    args = np.array(args)
    for metric in kwargs.values():
        try:
            assert len(args) != 0
            match metric.lower():
                case 'mean':
                    print("mean : " + str(np.mean(args)))
                case 'median':
                    print("median : " + str(np.median(args)))
                case 'quartile':
                    print(
                        "quartile : [" + str(np.quantile(args, 0.25)) +
                        ", " + str(np.quantile(args, 0.75)) + "]"
                    )
                case 'std':
                    print("std : " + str(np.std(args)))
                case 'var':
                    print("var : " + str(np.var(args)))
        except Exception:
            print("ERROR")
