#####################################################################
#####################################################################

#                nlargest and nsmallest

#####################################################################
#####################################################################

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


df = sns.load_dataset("titanic")
df.head()

df.nsmallest(3, "age")  # Youngest 3 passengers
df.nlargest(3, "age")   # Oldest 3 passengers

