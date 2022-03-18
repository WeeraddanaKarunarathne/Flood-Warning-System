from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation

def run():
    stations = build_station_list()
        
    output = [station.name for station in inconsistent_typical_range_stations(stations)]
    print(sorted(output))



    #TEST SEQUENCE 1
    #listofstations = ['Addlestone', 'Airmyn', 'Allerford', 'Arundel Queen St Bridge', 'Blacktoft', 'Braunton', 'Brentford', 'Broomfleet Weighton Lock', 'East Hull Hedon Road', 'Eccelsfield Morrisons', 'Fleetwood', 'Goole', 'Gravesend', 'Hedon Thorn Road Bridge', 'Hedon Westlands Drain', 'Hull Barrier Victoria Pier', 'Hull High Flaggs, Lincoln Street', "King's Lynn", 'Littlehampton', 'Paull', 'Salt end', 'Silloth Docks', 'Stone Creek', 'Templers Road', 'Topsham', 'Totnes', 'Truro Harbour', 'Weare Giffard', 'Westbrook Mill', 'Wilfholme PS', 'Wilfholme PS Hull Level']
    #for station in stations:
        #if station.name in listofstations:
            #print(station.name + '  ' + str(station.typical_range) + '  ' + str(MonitoringStation.typical_range_consistent(station)) )
            #print(station.typical_range)
            #print(MonitoringStation.typical_range_consistent(station))
            #print('-----------')
    
    #TEST SEQUENCE 2
    #output = inconsistent_typical_range_stations(stations)
    #for station in output:
    #    print(station.name + '   ' + str(station.typical_range))


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()