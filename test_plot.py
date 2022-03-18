""" Unit test for the plot module """

from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels

import matplotlib.pyplot as plt
import datetime

def test_plot_water_levels():

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
        dt=10
        dates, levels = fetch_measure_levels(item.measure_id, dt=datetime.timedelta(days=dt))

        assert len(dates) == len(levels)


def test_plot_water_level_with_fit():

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

        assert len(dates) == len(levels)