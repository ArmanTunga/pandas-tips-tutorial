#####################################################################
#####################################################################

#                Chaining

#####################################################################
#####################################################################

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = pd.read_csv("datasets/netflix-tv-shows-and-movies.csv")
df.head()

df_updated = (df
              .query("release_year>2018")  # Get movies and shows only released after 2018
              .loc[:, ["title", "release_year", "duration"]]  # Get only these columns
              # Create new column called over_three_hours depending on duration > 180
              .assign(over_three_hours=lambda dataframe: np.where(dataframe["duration"] > 180, "Yes", "No"))
              .groupby(by=["release_year", "over_three_hours"])  # Group by given columns
              .count()  # Get count of movies by release_year and over_three_hours
              )
df_updated
