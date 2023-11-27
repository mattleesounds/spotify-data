import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Base path where the files are located (adjust as needed)
base_path = "updatedCharts"

# List of file names for each month (adjust file names as needed)
file_names = ["december-22.csv", "january-23.csv", "february-23.csv", "march-23.csv",
              "april-23.csv", "may-23.csv", "june-23.csv", "july-23.csv",
              "august-23.csv", "september-23.csv", "october-23.csv", "november-23.csv"]

# Initialize a list to store DataFrames
dfs = []

# Loop through each file and append DataFrame to the list
for file_name in file_names:
    file_path = os.path.join(base_path, file_name)
    monthly_data = pd.read_csv(file_path)
    
    # Bins and labels for artist popularity ranges
    bins = list(range(0, 101, 10))
    labels = [f"{i}-{i+9}" for i in range(0, 90, 10)] + ["90-100"]
    monthly_data['popularity_range'] = pd.cut(monthly_data['artist_popularity'], bins=bins, labels=labels)

    dfs.append(monthly_data)

# Consolidate all DataFrames in the list into a single DataFrame
consolidated_data = pd.concat(dfs, ignore_index=True)

# Replace genre name with newline character for 'canadian contemporary r&b'
consolidated_data['artist_genre'] = consolidated_data['artist_genre'].replace('canadian contemporary r&b', 'canadian\ncontemporary r&b')

# Identify the top 10 genres
top_genres = consolidated_data['artist_genre'].value_counts().head(10).index

# Filter data to include only the top 10 genres
filtered_data = consolidated_data[consolidated_data['artist_genre'].isin(top_genres)]

# Group by genre and popularity range, then count the occurrences
grouped_data = filtered_data.groupby(['artist_genre', 'popularity_range']).size().reset_index(name='song_count')

# Pivot the data for heatmap, converting values to integers
pivot_data = grouped_data.pivot_table(index="artist_genre", columns="popularity_range", values="song_count", fill_value=0, aggfunc='sum')

# Creating the heatmap
plt.figure(figsize=(15, 10))
sns.heatmap(pivot_data, annot=True, cmap="Greens", fmt="d")
plt.title("Relationship Between Genre and Artist Popularity (Top 10 Genres)")
plt.xlabel("Artist Popularity Range")
plt.ylabel("Genre")
plt.xticks(rotation=45)
plt.yticks(rotation=0)  # Adjust rotation if genre labels overlap
plt.show()
