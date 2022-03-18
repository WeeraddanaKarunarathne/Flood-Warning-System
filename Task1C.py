#This file executes the function in geo.py that finds those stations within a particular radius of a point

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1C"""

    stations = build_station_list()

    # We find the stations that are within 10km of the Cambridge city centre

    print(stations_within_radius(stations, (52.2053, 0.1218), 10))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()


    