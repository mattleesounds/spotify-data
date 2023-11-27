import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Base path where the CSV files are located
base_path = "updatedCharts"  # Update this with the actual path

# List of file names for each month
file_names = ["december-22.csv", "january-23.csv", "february-23.csv", "march-23.csv",
              "april-23.csv", "may-23.csv", "june-23.csv", "july-23.csv",
              "august-23.csv", "september-23.csv", "october-23.csv", "november-23.csv"]

# Initialize an empty DataFrame to hold all data
all_data = pd.DataFrame()

# Loop through each file and append to all_data
for file_name in file_names:
    file_path = os.path.join(base_path, file_name)
    monthly_data = pd.read_csv(file_path)
    month = file_name.split("-")[0]  # Extract the month from the file name
    monthly_data['Month'] = month  # Add a 'Month' column
    all_data = pd.concat([all_data, monthly_data])

# Group by Month and Genre, then count the number of songs
genre_counts = all_data.groupby(['Month', 'artist_genre']).size().reset_index(name='SongCount')

# Find the top 25 genres over the entire period
top_genres = all_data['artist_genre'].value_counts().head(25).index

# Filter the data to include only the top 25 genres
filtered_data = genre_counts[genre_counts['artist_genre'].isin(top_genres)]

# Create a pivot table for plotting
pivot_data = filtered_data.pivot(index='Month', columns='artist_genre', values='SongCount').fillna(0)

# Create the line graph
plt.figure(figsize=(15, 10))
sns.lineplot(data=pivot_data)
plt.title('Number of Songs on Chart for Top 25 Genres Over Time')
plt.xlabel('Month')
plt.ylabel('Number of Songs')
plt.xticks(rotation=45)
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
