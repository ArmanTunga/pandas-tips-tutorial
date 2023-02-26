#################################################################
#################################################################

#                Avoid unnecessary apply

#################################################################
#################################################################

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# SPACE RACING
data = {
    'space_ship': ['X-wing', 'TIE Fighter', 'Millennium Falcon', 'The Ghost', 'Jedi Starfighter'],
    'galaxy': ['Andromeda', 'Milky Way', 'Triangulum', 'Centaurus', 'Whirlpool'],
    'speed': [100, 200, 150, 180, 120],
    'maneuverability': [4.5, 3.7, 4.2, 3.9, 4.1],
    'pilot_skill': [8, 6, 9, 7, 8.5],
    'resource_management': [7.5, 6, 8, 7.5, 7]
}

# Create a Pandas DataFrame from the data dictionary
df = pd.DataFrame(data)
df.head()

# Calculate the win probability element-wise for each row using the specified formula
df['win_prob'] = (df['speed'] * df['maneuverability'] * df['pilot_skill']) / df['resource_management']

"""
# ----------- APPROACH WITH .apply()
# Define a function to calculate the win probability
def calculate_win_prob(row):
    return (row['speed'] * row['maneuverability'] * row['pilot_skill']) / row['resource_management']


# Apply the calculate_win_prob function to each row and store the result in a new column called "win_prob"
df['win_prob'] = df.apply(calculate_win_prob, axis=1)
"""
