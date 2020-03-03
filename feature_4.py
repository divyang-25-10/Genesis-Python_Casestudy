"""
Name - Divyang Thakkar
Emp Id - 142876
Verson - 1.0
"""

import pandas as pd
import matplotlib.pyplot as plt

# Feature 4 Starts
# This feature is responsible for Fuel Trim Analysis

DATA = pd.read_csv('city2final.csv')


def trim_analysis():
    """ Main function for feature 4"""
    trim = DATA["Fuel trim bank 1 sensor 1(%)"]
    lat_ideal = []
    long_ideal = []
    time_ideal = []
    lat_non_ideal = []
    long_non_ideal = []
    time_non_ideal = []
    lat_malfunction = []
    long_malfunction = []
    time_malfunction = []

    count = 0

    for i in trim:
        if ((i) < 10 and (i) > -10):  # Ideal_trim1 = 10 Ideal_trim2 = -10
            lat_ideal.append(DATA[' Latitude'][count])
            long_ideal.append(DATA[' Longitude'][count])
            time_ideal.append(DATA[' Device Time'][count])
        elif ((i >= 10 and i < 25) and (i <= -10 and i > -25)):
            lat_non_ideal.append(DATA[' Latitude'][count])
            long_non_ideal.append(DATA[' Longitude'][count])
            time_non_ideal.append(DATA[' Device Time'][count])
        else:
            lat_malfunction.append(DATA[' Latitude'][count])
            long_malfunction.append(DATA[' Longitude'][count])
            time_malfunction.append(DATA[' Device Time'][count])
        count = count + 1

    plt.scatter(lat_ideal, long_ideal, label='Speed', color='b')
    plt.scatter(lat_non_ideal, long_non_ideal, label='Speed', color='y')
    plt.scatter(lat_malfunction, long_malfunction, label='Speed', color='r')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('Trim Analysis')
    plt.legend(['Ideal', 'Non-Ideal', 'Malfunction'])

# Feature 4 Ends
