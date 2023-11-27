import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Mapping full month names to abbreviations
month_map = {
    "december": "Dec", "january": "Jan", "february": "Feb", "march": "Mar",
    "april": "Apr", "may": "May", "june": "Jun", "july": "Jul",
    "august": "Aug", "september": "Sep", "october": "Oct", "november": "Nov"
}

# List of file names for each month in correct order
file_names = ["december-22.csv", "january-23.csv", "february-23.csv", "march-23.csv",
              "april-23.csv", "may-23.csv", "june-23.csv", "july-23.csv",
              "august-23.csv", "september-23.csv", "october-23.csv", "november-23.csv"]

# Base path where the files are located (adjust as needed)
base_path = "updatedCharts"

# Initialize a list to store DataFrames
dfs = []

# Loop through each file and append DataFrame to the list
for file_name in file_names:
    file_path = os.path.join(base_path, file_name)
    monthly_data = pd.read_csv(file_path)
    month_name = file_name.split("-")[0]  # Extract month from file name
    monthly_data["Month"] = month_map[month_name.lower()]  # Map to abbreviated month name
    dfs.append(monthly_data)

# Consolidate all DataFrames in the list into a single DataFrame
consolidated_data = pd.concat(dfs, ignore_index=True)

# Group by month and genre, then count the occurrences
grouped_data = consolidated_data.groupby(['Month', 'artist_genre']).size().reset_index(name='song_count')

# Pivot the data for heatmap, converting values to integers
pivot_data = grouped_data.pivot_table(index="Month", columns="artist_genre", values="song_count", fill_value=0, aggfunc='sum')

# Ensure all values in the pivot table are integers
pivot_data = pivot_data.astype(int)

# Filter for top N genres
top_genres = consolidated_data['artist_genre'].value_counts().head(10).index  # Adjust the number as needed
pivot_data = pivot_data[top_genres]

# Ensure the months are in the correct order
pivot_data = pivot_data.reindex(["Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"])

# Creating the heatmap with adjusted size
plt.figure(figsize=(35, 30))  # Adjust the size as needed
sns.heatmap(pivot_data, annot=True, cmap="Greens", fmt="d")
plt.title("Count of Songs by Genre Per Month (Top Genres)")
plt.xlabel("Genre")
plt.ylabel("Month")

plt.xticks(rotation=45, ha='right')
#plt.tight_layout()
plt.show()
