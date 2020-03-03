"""
Name - Divyang Thakkar
Emp Id - 142876
Verson - 1.0
"""

import pandas as pd
import matplotlib.pyplot as plt

DATA = pd.read_csv('city2final.csv')

# Feature 1 Starts
# This feature is responsible for Checking the Pollution Level during the trip


def pollution():
    """ Main function for feature 1 """
    carbon_value = DATA["CO in g/km (Average)(g/km)"]
    max_value = (carbon_value.max())
    min_value = (carbon_value.min())
    avg_value = (max_value+min_value)/2

    type_of_poll = ['Low', 'Medium', 'High']

    poll_caused = []
    latl = []
    latm = []
    lath = []
    longl = []
    longm = []
    longh = []

    for i in range(2576):
        if (carbon_value[i] >= min_value and carbon_value[i] <= (avg_value-4)):
            poll_caused.append(type_of_poll[0])
            latl.append(DATA[' Latitude'][i])
            longl.append(DATA[' Longitude'][i])
        elif (carbon_value[i] > (avg_value-4) and carbon_value[i] <= (avg_value+4)):
            poll_caused.append(type_of_poll[1])
            latm.append(DATA[' Latitude'][i])
            longm.append(DATA[' Longitude'][i])
        else:
            poll_caused.append(type_of_poll[2])
            lath.append(DATA[' Latitude'][i])
            longh.append(DATA[' Longitude'][i])
    plt.scatter(latl, longl, label='Speed', color='y')
    plt.scatter(latm, longm, label='Speed', color='b')
    plt.scatter(lath, longh, label='Speed', color='r')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('Pollution Level')
    plt.legend(type_of_poll)

# Feature 1 Ends
