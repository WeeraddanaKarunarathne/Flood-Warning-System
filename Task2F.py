#This file executes the function in analysis.py that plots the lines of best-fit for water levels

from floodsystem.analysis import polyfit, derivative
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import derivative

import matplotlib.pyplot as plt
import datetime

def run():
   """Requirements for Task 2F"""

stations = build_station_list()
update_water_levels(stations)

updated_levels = []
highest_levels = []
station_list = []

for station in stations:
    if station.latest_level != None:
        updated_levels.append(station.latest_level)
    else:
        continue

updated_levels.sort()

highest_levels = updated_levels[-5:]

for station in stations:
    for i in range(0, len(highest_levels)):
        if highest_levels[i] == station.latest_level:
            station_list.append(station)
        else:
            pass


for item in station_list:
    dt=2
    dates, levels = fetch_measure_levels(item.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_level_with_fit(item, dates, levels, 4)
    print(derivative(dates, levels, 4))

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
    