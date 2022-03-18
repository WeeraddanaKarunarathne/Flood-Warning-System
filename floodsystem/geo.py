# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from haversine import haversine, Unit #The Haversine formula is imported to calculate the distance between a station and 'p'
from .station import MonitoringStation


# The following function utlises the Haversine formula to calculate the distance (in km) between a list of stations and a point 'p', given their geographical coordinates

def stations_by_distance(stations, p):

    station_distances = []

    for station in stations:
        distance = (station.name, station.town, haversine((station.coord), p, unit=Unit.KILOMETERS))
        station_distances.append(distance)
    
    return sorted_by_key(station_distances, 2)


# The following function finds stations within a particular distance from a point 
    
def stations_within_radius(stations, centre, r):

    stations_in_circle = []

    for station in stations:

        if haversine((station.coord), centre, unit=Unit.KILOMETERS) <= r:
            stations_in_circle.append(station.name)
    
    stations_in_circle.sort()
    
    return stations_in_circle

def rivers_with_station(stations):
    
    rivers = set()

    for station in stations:
        rivers.add(station.river)
    
    return sorted(rivers)

def stations_by_river(stations):
    
    river_dict = {}

    for station in stations:
        if station.river not in river_dict:
            river_dict[station.river] = [station.name]
        else:
            river_dict[station.river].append(station.name)

    return river_dict

def rivers_by_station_number(stations, N):

    river_dict = {}

    for station in stations:
        if station.river not in river_dict:
            river_dict[station.river] = 1
        else:
            river_dict[station.river] += 1
    
    river_arr = []
    for item in river_dict:
        river_arr.append((item, river_dict[item]))

    river_arr.sort(key = lambda x: x[1], reverse=True)

    while river_arr[N-1][1] == river_arr[N][1]:
        N += 1

    return river_arr[:N]

    