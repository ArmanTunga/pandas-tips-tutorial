#############################################################################
#############################################################################

#                Conversion of Data Types To Save Memory and Speed Up

#############################################################################
#############################################################################

import pandas as pd
from create_random_data import create_random_data  # Creates a dataframe of random generated values

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
df = create_random_data(1_000_000)
df.head()

# Check the memory usage of the DataFrame before conversion
print("Before Conversion:")
print(df.info(memory_usage='deep'))  # memory usage: 84.9 MB

columns_to_convert = ["prob", "previous_races_count", "next_round"]
df[columns_to_convert] = df[columns_to_convert].astype("int8")
df["height", "weight"] = df["height"].astype("int16")

# Check the memory usage of the DataFrame after conversion
print("\nAfter Conversion:")
print(df.info(memory_usage='deep'))  # memory usage: 72.5 MB
