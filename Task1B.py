#This file executes the function in the file geo.py that calculates the distance between stations and a coordinate 'p'

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    stations = build_station_list()

    #The following function outputs the 10 closest stations from Cambridge

    print(stations_by_distance(stations, (52.2053, 0.1218))[:10])

    #The following function outputs the 10 furthest stations from Cambridge

    print(stations_by_distance(stations, (52.2053, 0.1218))[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()