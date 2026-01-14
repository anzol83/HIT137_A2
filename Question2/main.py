# First we import important libraries
# os, pandas and numpy

import os  #To interact with files and folders
import pandas as pd   #for reading and editing data
import numpy as np  #for mathematical & numerical operations

TEMPERATURE_FOLDER = "temperatures"  #"temperatures" folder has all the csv files.

#Adding Australian season according to months:
SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}

# Now loading all the csv file of temperature folder
# Each file with .csv is stored in df
def load_all_temperature_data():
    """Load and combine all CSV files in the temperatures folder."""
    all_data = []

    for file in os.listdir(TEMPERATURE_FOLDER):
        if file.endswith(".csv"):  #Finds files with csv extension
            file_path = os.path.join(TEMPERATURE_FOLDER, file)   #Joins the file name to make a full file path
            df = pd.read_csv(file_path)  #Reads and stores the pandas dataframe in df
            all_data.append(df)  #adds the data file to all_data list

    return pd.concat(all_data, ignore_index=True)

#Calculating seasonal average temperature
def calculate_seasonal_averages(df):

    #Creating dictionary to store average temperatures for each season
    season_averages = {}

    for season, months in SEASONS.items(): #looping through seasons and months
        values = df[months].values.flatten() #select the month column and convert the Numpyarray to 1-d array
        values = values[~np.isnan(values)] #Removes any missing values
        season_averages[season] = values.mean() #Calculate the average

    #Create a text file in write mode for the data
    with open("average_temp.txt", "w") as f:
        for season, avg in season_averages.items():
            f.write(f"{season}: {avg:.1f}°C\n") #Write season name and average temperature to 1 decimal place

#Function for calculating temperature range
def calculate_temperature_ranges(df):
    station_ranges = [] #Creating dictionary to store temperature range for each station

    month_columns = list(
        SEASONS["Summer"] + SEASONS["Autumn"] + SEASONS["Winter"] + SEASONS["Spring"]
        ) #Combinig seasonal months into 1 column to go through whole year

    for station, group in df.groupby("STATION_NAME"): #looping through the dataframe grouped by station name 'station'
        values = group[month_columns].values.flatten() #Extract temperature values
        values = values[~np.isnan(values)] #Removes any missing values

        if len(values) == 0: #Checking if no valid temperature values exists
            continue

        max_temp = values.max()
        min_temp = values.min()
        temp_range = max_temp - min_temp #Calculating temperature range

        #Storing the station name, temp ramge and max, min temp
        station_ranges.append((station, temp_range, max_temp, min_temp))

    max_range = max(sr[1] for sr in station_ranges) #Largest temperature range

    with open("largest_temp_range_station.txt", "w") as f: #Create a file in write mode
        for station, r, max_t, min_t in station_ranges: #loop through stored station ranges
            if np.isclose(r, max_range): #checking if station range matches the largest range
                #Now store the station name, temp range, max temp and min temp
                f.write(
                    f"{station}: Range {r:.1f}°C "
                    f"(Max: {max_t:.1f}°C, Min: {min_t:.1f}°C)\n"
                )

def calculate_temperature_stability(df):
    """Find most stable and most variable stations based on standard deviation."""
    station_stddevs = []

    month_columns = list(SEASONS["Summer"] + SEASONS["Autumn"] +
                         SEASONS["Winter"] + SEASONS["Spring"])

    for station, group in df.groupby("STATION_NAME"):
        values = group[month_columns].values.flatten()
        values = values[~np.isnan(values)]

        if len(values) == 0:
            continue

        stddev = np.std(values)
        station_stddevs.append((station, stddev))

    min_std = min(s[1] for s in station_stddevs)
    max_std = max(s[1] for s in station_stddevs)

    with open("temperature_stability_stations.txt", "w") as f:
        for station, std in station_stddevs:
            if np.isclose(std, min_std):
                f.write(f"Most Stable: {station}: StdDev {std:.1f}°C\n")

        for station, std in station_stddevs:
            if np.isclose(std, max_std):
                f.write(f"Most Variable: {station}: StdDev {std:.1f}°C\n")
