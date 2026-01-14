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

    for season, months in SEASONS.items(): #loopinf through seasons and months
        values = df[months].values.flatten() #select the month column and convert the Numpyarray to 1-d array
        values = values[~np.isnan(values)] #Removes any missing values
        season_averages[season] = values.mean() #Calculate the average

    #Create a text file in write mode for the data
    with open("average_temp.txt", "w") as f:
        for season, avg in season_averages.items():
            f.write(f"{season}: {avg:.1f}°C\n") #Write season name and average temperature to 1 decimal place