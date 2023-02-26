import pandas as pd
import numpy as np


def create_random_data(row_count=20_000):
    """
    Creates a dataframe of random generated values

    Args:
        row_count: int,
            Default 20_000, determines how many rows we want in dataFrame

    Returns: pandas.core.frame.DataFrame,
        DataFrame generated

    """

    df = pd.DataFrame()
    size = row_count
    # size = 200_000  # High memory usage
    # size = 20_000  # Low memory usage
    df["racer_id"] = np.arange(start=0, stop=size, step=1)
    df["shoes"] = np.random.choice(["model_a", "model_b", "model_c", "model_x", "model_y", "model_z"], size)
    df["height"] = np.random.randint(170, 190, size)  # cm
    df["weight"] = np.random.randint(60, 90, size)  # kg
    df["prob"] = np.random.uniform(0, 1, size)
    df["previous_races_count"] = np.random.randint(1, 10, size)
    df["next_round"] = np.random.choice([True, False], size)
    # df.shape
    # df.head()
    # df.info(memory_usage="deep")
    return df
