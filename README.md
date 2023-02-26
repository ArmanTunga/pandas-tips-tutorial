# 7 Simple Tips That Will Make You A Pandas Pro

This is the repository of [my Medium article:](https://medium.com/@armantunga/7-simple-tips-that-will-make-you-a-pandas-pro-52072d377ba6) **7 Simple Tips That Will Make You A Pandas Pro**


Pandas is one of the most popular and widely used libraries for data analysis in Python. Its power and versatility make
it a must-have tool for anyone working with data. Whether you're a beginner or an experienced user, there's always room
for improvement in your Pandas skills. Here are a few tips to help you take your Pandas skills to the next level.

## 1. Chaining:

Chaining is a powerful feature in Pandas that allows you to perform multiple operations in a single line of
code. This not only makes your code more concise and readable but also improves the performance of your code by
reducing the number of intermediate objects created.

```python
import pandas as pd
import numpy as np

df = pd.read_csv("datasets/netflix-tv-shows-and-movies.csv")
df.head()

df_updated = (df
              .query("release_year>2018")  # Get movies and shows only released after 2018
              .loc[:, ["title", "release_year", "duration"]]  # Get only these
              .assign(over_three_hours=lambda dataframe: np.where(dataframe["duration"] > 180, "Yes",
                                                                  "No"))  # Create new column called over_three_hours depending on duration > 180
              .groupby(by=["release_year", "over_three_hours"])  # Group by given columns
              .count()  # Get count of movies by release_year and over_three_hours
              )
df_updated

"""
########## RESULT ##########
                               title  duration
release_year over_three_hours                 
2019         No                  995       995
             Yes                   1         1
2020         No                  867       867
             Yes                   1         1
2021         No                   31        31
"""
``` 

You see! That's as easy as that to read and understand how we get df_updated.

## 2. nlargest and nsmallest:

Instead of using sort_values to find the largest or smallest values in your data, consider
using nlargest and nsmallest. These functions are faster and more memory-efficient, making them a great choice for
large datasets.

````python
import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset("titanic")

df.nsmallest(3, "age")  # Youngest 3 passengers
df.nlargest(3, "age")  # Oldest 3 passengers

"""
########## RESULTS ##########
########## nsmallest ##########
     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
803         1       3    male  0.42  ...   NaN    Cherbourg    yes  False
755         1       2    male  0.67  ...   NaN  Southampton    yes  False
469         1       3  female  0.75  ...   NaN    Cherbourg    yes  False

########## nlargest ##########
     survived  pclass   sex   age  ...  deck  embark_town  alive alone
630         1       1  male  80.0  ...     A  Southampton    yes  True
851         0       3  male  74.0  ...   NaN  Southampton     no  True
96          0       1  male  71.0  ...     A    Cherbourg     no  True
"""
````

## 3. Filtering Data With .query() Method:

Pandas' query function allows you to filter your data using logical expressions.
You can also use @ symbols to refer to variables in your query, making it a convenient and powerful tool for
filtering data.

````python
df["embark_town"].unique()  # ['Southampton', 'Cherbourg', 'Queenstown', nan]

embark_towns = ["Southampton", "Queenstown"]  # Only want to select these towns
df.query("age>21 & fare>250 & embark_town==@embark_towns").head()

"""
########## RESULT ##########
     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
88          1       1  female  23.0  ...     C  Southampton    yes  False
341         1       1  female  24.0  ...     C  Southampton    yes  False
438         0       1    male  64.0  ...     C  Southampton     no  False
[3 rows x 15 columns]
"""
````

## 4. Using df.cut Method:

The cut function is a useful tool for binning your data into discrete categories. This can be
useful for visualizing your data or for transforming continuous variables into categorical ones.

````python
# Child - 0 to 9 years
# Teen - 10-19 years
# Young - 19 to 24 years
# Adult - 25 to 59
# Elderly > 59

# bins = [-float('inf'), 10, 19, 24, 59, float('inf')]
bins = [0, 10, 19, 24, 59, float('inf')]
labels = ["Child", "Teen", "Young", "Adult", "Elderly"]
df["age"].hist()
plt.show()
df["age_category"] = pd.cut(df["age"], bins=bins, labels=labels)
sorted_df = df.sort_values(by="age_category")
sorted_df["age_category"].hist()
plt.show()
````

## 5. Conversion of Data Types To Save Memory and Speed Up:

Pandas uses the int128 data type by default for integers, but
in some cases, it may be necessary to convert them to int64, int32… in order to save memory.
We can check the mininum and maximum values of integers by simply doing np.iinfo().

```python  
np.iinfo("int32")  # iinfo(min=-2147483648, max=2147483647, dtype=int32)
np.iinfo("int16")  # iinfo(min=-32768, max=32767, dtype=int16)
np.iinfo("int8")  # iinfo(min=-128, max=127, dtype=int8)
```

This represents that int16is between -237689 and 32768 while int8is only between -129 and 128. So this means we can
save some memory by converting some of the columns. For example in Titanic Dataset, we can convert survived and
pclass to int8 because values of those columns will always be between -127 and 127. Let's create a sample dataset,
convert some columns to int8 and look at the difference of memory usage. Let's create a sample dataset, convert some
columns to int8 and look at the difference of memory usage.

````python
# Creates a dataframe of random generated values
from create_random_data import create_random_data

df = create_random_data(1_000_000)  # Create a df with 1M rows
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
````

We saved 10+ Mbs converting only 5 columns of int32 to int8 and int16.
Imagine converting 10 columns of int64 to int8 and int16, we would save at least 50 Mbs and speed up our data processes.

## 6. Avoid using inplace:

The inplace parameter in Pandas allows you to perform operations directly on your dataframe, but
it can be dangerous to use, as it can make your code harder to read and debug. Instead, try to use the standard
method of assigning the result of your operation to a new object.

````python
# using inplace to remove the first row of the DataFrame directly

# DON'T
# df.drop(0, inplace=True) 

# DO
df = df.drop(0)
````

## 7. Avoid unnecessary apply:

The apply function can be a powerful tool, but it can also be slow and memory-intensive.
Try to avoid using apply when there are direct, faster and more efficient ways to accomplish your goal.

````python
columns = ['space_ship', 'galaxy', 'speed',
           'maneuverability', 'pilot_skill', 'resource_management']

# Calculate the win probability element-wise for each row using the specified formula
df['win_prob'] = (df['speed'] * df['maneuverability'] * df['pilot_skill']) / df['resource_management']

# ------------------
# Using .apply()
# df['win_prob'] = df.apply(lambda row: (row['speed'] * row['maneuverability'] * row['pilot_skill']) / row['resource_management'], axis=1)
````

## 8. BONUS! Master Aggregation:

We need to master aggregation to gain deeper insights into our data by summarizing it in
meaningful ways. Aggregations allow for efficient and effective analysis of large datasets, enabling us to answer
complex questions quickly. This can help us make informed decisions based on the data and drive more successful
outcomes.

### In conclusion

These tips are just the beginning of what you can do to improve your Pandas skills. Remember to always
seek out new knowledge and techniques, and practice. With these tips and some hard work, you'll be on your way to
becoming a Pandas pro in no time.