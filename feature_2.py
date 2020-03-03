"""
Name - Divyang Thakkar
Emp Id - 142876
Version - 1.0
"""

import pandas as pd
import matplotlib.pyplot as plt

# Feature 2 Starts
# This feature is responsible for Analysing Speed using pie-chart

DATA = pd.read_csv('city2final.csv')


def speed_analysis():
    """ Main function for feature 2"""
    speed = DATA["Speed (GPS)(km/h)"]
    c_0 = 0
    c_0_10 = 0
    c_10_20 = 0
    c_20_30 = 0
    c_30_40 = 0
    c_40_50 = 0
    c_50 = 0

    for i in speed:
        if i == 0:
            c_0 += 1
        elif i > 0 and i <= 10:
            c_0_10 += 1
        elif i > 10 and i <= 20:
            c_10_20 += 1
        elif i > 20 and i <= 30:
            c_20_30 += 1
        elif i > 30 and i <= 40:
            c_30_40 += 1
        elif i > 40 and i <= 50:
            c_40_50 += 1
        else:
            c_50 += 1

    fig = plt.figure()
    ax1 = fig.add_axes([0, 0, 1, 1])
    ax1.axis('equal')
    speed_limits = ['0 (Km/hr)', '0-10 (Km/hr)', '10-20 (Km/hr)', '20-30 (Km/hr)', '30-40(Km/hr)', '40-50(Km/hr)', '>50(Km/hr)']
    speed_values = [c_0, c_0_10, c_10_20, c_20_30, c_30_40, c_40_50, c_50]
    explode = (0, 0, 0, 0, 0, 0, 0)
    ax1.pie(speed_values, explode=explode, labels=speed_limits, autopct='%1.1f%%')
    plt.show()

# Feature 2 Ends
