import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """
    Writes the dimensions of the data set
    Returns it
    """
    try:
        df = pd.read_csv(path, index_col=0)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print("Error: " + str(e))
        return None
