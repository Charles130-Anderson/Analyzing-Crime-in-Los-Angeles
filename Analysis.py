# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})

# Convert 'TIME OCC' to datetime
crimes['TIME OCC'] = pd.to_datetime(crimes['TIME OCC'], format='%H%M', errors='coerce')

# Find the hour with the highest frequency of crimes
peak_crime_hour = crimes['TIME OCC'].dt.hour.value_counts().idxmax()

# Determine the area with the largest frequency of night crimes
night_crimes = crimes[(crimes['TIME OCC'].dt.hour >= 22) | (crimes['TIME OCC'].dt.hour < 4)]
peak_night_crime_location = night_crimes['AREA NAME'].value_counts().idxmax()

# Identify the number of crimes committed against victims of different age groups
bins = [0, 18, 26, 35, 45, 55, 65, float('inf')]
labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
victim_ages = pd.cut(crimes['Vict Age'], bins=bins, labels=labels, right=False).value_counts()

# Display the results
print("Hour with the highest frequency of crimes:", peak_crime_hour)
print("Area with the largest frequency of night crimes:", peak_night_crime_location)
print("Crimes committed against victims of different age groups:")
print(victim_ages)
