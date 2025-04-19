import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """
    Returns dataset
    """
    try:
        df = pd.read_csv(path, index_col=0)
        return df
    except Exception as e:
        print("Error: " + str(e))
        return None
