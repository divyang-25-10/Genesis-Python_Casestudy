"""
Name - Divyang Thakkar
Emp Id - 142876
Verson - 1.0
"""

import pandas as pd
import folium

# Feature 3 Starts
# This feature is responsible for Plotting the route on Google Maps

DATA = pd.read_csv('city2final.csv')


def route():
    """ Main function for feature 3"""
    # list of latitudes
    lat_list = DATA[' Latitude']
    # list of longitudes
    long_list = DATA[' Longitude']
    my_map4 = folium.Map(location=[17.46832275, 78.37600683], zoom_start=15)

    folium.Marker([17.46832275, 78.37600683]).add_to(my_map4)
    folium.Marker([17.46755109, 78.44511019]).add_to(my_map4)
    for i in range(2575):
        folium.PolyLine(locations=[(lat_list[i], long_list[i]), (lat_list[i+1], long_list[i+1])], line_opacity = 0.5).add_to(my_map4)
        my_map4

# Feature 3 Ends
