#####################################################################
#####################################################################

#                Filtering Data With .query() Method

#####################################################################
#####################################################################

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


df = sns.load_dataset("titanic")
df.head()
df["embark_town"].unique()  # ['Southampton', 'Cherbourg', 'Queenstown', nan]
embark_towns = ["Southampton", "Queenstown"]  # Only want to select these towns

df.query("age>21 & fare>250 & embark_town==@embark_towns").head()
