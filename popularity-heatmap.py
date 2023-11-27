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
    # Categorize artist popularity into ranges
    bins = list(range(0, 101, 10))
    labels = [f"{i}-{i+9}" for i in range(0, 90, 10)] + ["90-100"]
    monthly_data['popularity_range'] = pd.cut(monthly_data['artist_popularity'], bins=bins, labels=labels)
    dfs.append(monthly_data)

# Consolidate all DataFrames in the list into a single DataFrame
consolidated_data = pd.concat(dfs, ignore_index=True)

# Group by month and popularity range, then count the occurrences
grouped_data = consolidated_data.groupby(['Month', 'popularity_range']).size().reset_index(name='song_count')

# Pivot the data for heatmap, converting values to integers
pivot_data = grouped_data.pivot_table(index="Month", columns="popularity_range", values="song_count", fill_value=0, aggfunc='sum')

# Ensure the months are in the correct order
pivot_data = pivot_data.reindex(["Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"])

# Creating the heatmap
plt.figure(figsize=(15, 10))
sns.heatmap(pivot_data, annot=True, cmap="Greens", fmt="d")
plt.title("Count of Songs by Artist Popularity Range Per Month")
plt.xlabel("Artist Popularity Range")
plt.ylabel("Month")
plt.xticks(rotation=45)
plt.show()
