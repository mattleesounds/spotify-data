# Spotify Charts Data Analysis

A Python-based data analysis project that enriches Spotify's global weekly chart data with artist genre and popularity metrics from the Spotify API, then visualizes music trends over time through interactive heatmaps and time-series analysis.

## Overview

This project demonstrates full-stack data engineering and visualization capabilities:

- **API Integration**: Authenticates with Spotify's Web API using OAuth 2.0 client credentials flow
- **Data Enrichment**: Processes raw chart CSV files to fetch additional artist metadata (genres, popularity scores)
- **Data Processing**: Consolidates monthly data across a year-long dataset (Dec 2022 - Nov 2023)
- **Data Visualization**: Generates multiple analytical visualizations using seaborn and matplotlib

## What's Happening in This Repo

### Data Collection (`main.py`)
The core data enrichment script that:
1. Authenticates with Spotify API using client credentials
2. Reads weekly chart CSV files from Spotify Charts
3. For each track, fetches the primary artist's genre and popularity score
4. Outputs enriched CSV files with additional metadata columns

### Visualization Scripts

**`genre-heatmap.py`**
- Consolidates 12 months of chart data
- Creates a heatmap showing the count of songs per genre across months
- Focuses on the top 10 genres by overall chart presence

**`genres-over-time.py`**
- Generates a time-series line graph tracking the top 25 genres
- Shows how different genres gain or lose chart presence over time

**`popularity-heatmap.py`**
- Analyzes artist popularity distribution on charts
- Groups artists into popularity ranges (0-10, 10-20, etc.)
- Visualizes which popularity tiers dominate the charts each month

**`genre-popularity-heatmap.py`**
- Cross-references genre with artist popularity
- Shows which genres tend to have higher or lower artist popularity scores

### Data Structure

- **Input**: Spotify Charts weekly CSVs containing rank, track URI, artist names, streams
- **Output**: Enriched CSVs in `updatedCharts/` directory with `artist_genre` and `artist_popularity` columns
- **Visualizations**: Heatmaps and graphs showing temporal music trends

## Technical Stack

- **Python 3.x**
- **pandas** - Data manipulation and CSV processing
- **requests** - HTTP client for Spotify API
- **seaborn** - Statistical data visualization
- **matplotlib** - Plotting library
- **python-dotenv** - Environment variable management

## Local Testing

### Prerequisites

1. **Python 3.7+** installed on your system
2. **Spotify Developer Account** - [Create one here](https://developer.spotify.com/dashboard)
3. **Spotify API Credentials**:
   - Create a new app in your Spotify Developer Dashboard
   - Note your `Client ID` and `Client Secret`

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/spotify-data.git
   cd spotify-data
   ```

2. **Install dependencies**
   ```bash
   pip install pandas requests matplotlib seaborn python-dotenv
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root:
   ```env
   CLIENT_ID=your_spotify_client_id_here
   CLIENT_SECRET=your_spotify_client_secret_here
   ```

4. **Run data enrichment** (optional - enriched data already included)
   ```bash
   python main.py
   ```
   This will process the chart CSV files and add genre/popularity data. Note: This makes many API calls and takes time.

5. **Generate visualizations**
   ```bash
   # Genre distribution heatmap
   python genre-heatmap.py

   # Genre trends over time
   python genres-over-time.py

   # Artist popularity distribution
   python popularity-heatmap.py

   # Genre vs. popularity heatmap
   python genre-popularity-heatmap.py
   ```

### Expected Output

Each visualization script will display an interactive matplotlib window with the corresponding graph. The visualizations show:

- Seasonal genre trends (e.g., Christmas music in December)
- Emerging vs. declining genres over the year
- Correlation between artist popularity and chart success
- Genre diversity patterns on global charts

### Troubleshooting

- **API Rate Limits**: If you hit Spotify API rate limits, add delays between requests in `main.py`
- **Missing Data**: Some artists may not have genre data - these default to "Not Available"
- **Module Not Found**: Ensure all dependencies are installed via pip

## Project Insights

This analysis reveals:
- How genre preferences shift across seasons
- Which genres consistently maintain chart presence
- The relationship between artist mainstream popularity and chart success
- Global music consumption patterns during 2022-2023

## Future Enhancements

- Add audio features analysis (danceability, energy, valence)
- Implement regional chart comparisons
- Create interactive dashboards with Plotly or Streamlit
- Add statistical correlation analysis between features and chart performance

---

**Note**: This project uses publicly available Spotify Charts data and the Spotify Web API for educational and analytical purposes.
