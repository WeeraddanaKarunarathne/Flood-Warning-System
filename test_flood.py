import pytest
import floodsystem.flood
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)

    output = stations_level_over_threshold(stations, 0.4)
    assert len(output) <= len(stations)
    if len(output) > 0:
        assert output[0][1] > 0.4
        assert output[-1][1] > 0.4

    output = stations_level_over_threshold(stations, 0.8)
    assert len(output) <= len(stations)
    if len(output) > 0:
        assert output[0][1] > 0.8
        assert output[-1][1] > 0.8

    output = stations_level_over_threshold(stations, 1.2)
    assert len(output) <= len(stations)
    if len(output) > 0:
        assert output[0][1] > 1.2
        assert output[-1][1] > 1.2

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)

    output = stations_highest_rel_level(stations, 3)
    assert len(output) == 3
    assert output[0][1] >= output[-1][1]

    output = stations_highest_rel_level(stations, 10)
    assert len(output) == 10
    assert output[0][1] >= output[-1][1]

    output = stations_highest_rel_level(stations, 50)
    assert len(output) == 50
    assert output[0][1] >= output[-1][1]