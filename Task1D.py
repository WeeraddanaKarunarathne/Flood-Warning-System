
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    stations = build_station_list()
    rivers = rivers_with_station(stations)

    # trial for part 1
    print(len(rivers))
    print(rivers[:10])


    river_dict = stations_by_river(stations)

    # trials for part 2
    print('')
    print(sorted(river_dict['River Aire']))
    print('')
    print(sorted(river_dict['River Cam']))
    print('')
    print(sorted(river_dict['River Thames']))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()