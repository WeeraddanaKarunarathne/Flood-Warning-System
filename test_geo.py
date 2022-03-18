""" Unit test for the geo module """

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

def test_stations_by_distance():

    output = stations_by_distance(build_station_list(), (52.2053, 0.1218)[:10])
    expected_output = [('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494), ('Bin Brook', 'Cambridge', 2.502277543239629), ("Cambridge Byron's Pool", 'Grantchester', 4.07204948005424), ('Cambridge Baits Bite', 'Milton', 5.115596582531859), ('Girton', 'Girton', 5.227077565748483), ('Haslingfield Burnt Mill', 'Haslingfield', 7.0443978959918025), ('Oakington', 'Oakington', 7.12825901765745), ('Stapleford', 'Stapleford', 7.265704342799649), ('Comberton', 'Comberton', 7.735085060177142), ('Dernford', 'Great Shelford', 7.993872393303291)]
    output == expected_output

def test_stations_within_radius():

    output_length = len(stations_within_radius(build_station_list(), (52.2053, 0.1218), 10)) 
    assert output_length == 11

def test_rivers_with_station():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    assert len(rivers) > 0

    counter = 0
    for station in stations:
        if station.river in rivers:
            counter += 1
    assert counter == len(stations)

def test_stations_by_river():
    stations = build_station_list()
    river_dict = {}

    for station in stations:
        if station.river not in river_dict:
            river_dict[station.river] = [station.name]
        else:
            river_dict[station.river].append(station.name)

    assert sorted(river_dict['River Aire']) == ['Airmyn', 'Apperley Bridge', 'Armley', 'Beal Weir Bridge', 'Bingley', 'Birkin Holme Washlands', 'Carlton Bridge', 'Castleford', 'Chapel Haddlesey', 'Cononley', 'Cottingley Bridge', 'Ferrybridge Lock', 'Fleet Weir', 'Gargrave', 'Kildwick', 'Kirkstall Abbey', 'Knottingley Lock', 'Leeds Crown Point', 'Leeds Crown Point Flood Alleviation Scheme', 'Leeds Knostrop Weir Flood Alleviation Scheme', 'Saltaire', 'Snaygill', 'Stockbridge']
    assert sorted(river_dict['River Cam']) ==  ['Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Dernford', 'Great Chesterford', 'Weston Bampfylde']
    assert sorted(river_dict['River Thames']) == ['Abingdon Lock', 'Bell Weir', 'Benson Lock', 'Boulters Lock', 'Bray Lock', 'Buscot Lock', 'Caversham Lock', 'Chertsey Lock', 'Cleeve Lock', 'Clifton Lock', 'Cookham Lock', 'Cricklade', 'Culham Lock', 'Days Lock', 'Ewen', 'Eynsham Lock', 'Farmoor', 'Godstow Lock', 'Goring Lock', 'Grafton Lock', 'Hannington Bridge', 'Hurley Lock', 'Iffley Lock', 'Kings Lock', 'Kingston', 'Maidenhead', 'Mapledurham Lock', 'Marlow Lock', 'Marsh Lock', 'Molesey Lock', 'Northmoor Lock', 'Old Windsor Lock', 'Osney Lock', 'Penton Hook', 'Pinkhill Lock', 'Radcot Lock', 'Reading', 'Romney Lock', 'Rushey Lock', 'Sandford-on-Thames', 'Shepperton Lock', 'Shifford Lock', 'Shiplake Lock', 'Somerford Keynes', 'Sonning Lock', 'St Johns Lock', 'Staines', 'Sunbury  Lock', 'Sutton Courtenay', 'Teddington Lock', 'Thames Ditton Island', 'Trowlock Island', 'Walton', 'Whitchurch Lock', 'Windsor Park']

def test_rivers_by_station_number():
    stations = build_station_list()
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

    N = 9
    while river_arr[N-1][1] == river_arr[N][1]:
        N += 1

    assert river_arr[:N] == [('River Thames', 55), ('River Avon', 32), ('River Great Ouse', 31), ('River Aire', 23), ('River Calder', 21), ('River Severn', 21), ('River Derwent', 21), ('River Stour', 19), ('River Ouse', 16), ('River Trent', 16)]
