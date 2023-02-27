#################################################################
#################################################################

#                Avoid using inplace

#################################################################
#################################################################

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = pd.read_csv("datasets/salary-dataset.csv")
df.head()

# DON'T
# df.drop(0, inplace=True)

# DO
df = df.drop(0)
# df = df.drop(0).reset_index()

df.head()
