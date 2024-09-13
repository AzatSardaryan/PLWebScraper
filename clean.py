import pandas as pd

# Load the CSV file with the correct headers already set
df_cleaned = pd.read_csv("stats.csv")

# Strip any leading/trailing spaces from column names, just in case
df_cleaned.columns = df_cleaned.columns.str.strip()

# Remove rows where 'Player' starts with 'Squad Total' or 'Opponent Total'
df_cleaned = df_cleaned[~df_cleaned['Player'].str.contains('Squad Total|Opponent Total', na=False)]

# Columns to keep
columns_to_keep = ['Player', 'Nation', 'Pos', 'Age', 'MP', 'Starts', 'Min', 'Gls', 'Ast', 'xG', 'xAG', 'xG+xAG', 'npxG', 'npxG+xAG', 'Team']

# Select only the important columns
df_cleaned = df_cleaned[columns_to_keep]

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_data.csv', index=False)
