#####################################################################
#####################################################################

#                Using df.cut Method

#####################################################################
#####################################################################

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = sns.load_dataset("titanic")
df.head()

# Child - 0 to 9 years
# Teen - 10-19 years
# Young - 19 to 24 years
# Adult - 25 to 59
# Elderly >59

# bins = [-float('inf'), 10, 19, 24, 59, float('inf')]
bins = [0, 10, 19, 24, 59, float('inf')]
labels = ["Child", "Teen", "Young", "Adult", "Elderly"]
df["age"].hist()
plt.show()
df["age_category"] = pd.cut(df["age"], bins=bins, labels=labels)
sorted_df = df.sort_values(by="age_category")
sorted_df["age_category"].hist()
plt.show()
