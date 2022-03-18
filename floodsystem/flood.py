from .station import MonitoringStation
from .station import inconsistent_typical_range_stations

def stations_level_over_threshold(stations, tol):
    """Returns a list of the tuples, each containing the name of a station at which the relative
    water level is above tol and the relative water level at that station"""

    output = []

    for station in stations:
        relative_level = station.relative_water_level()
        # the following raises an exception if relative_level is None
        try:
            if relative_level > tol:
                output.append((station, relative_level))
        except:
            pass
    # sort list by second value in descending order
    output.sort(key=lambda x: x[1], reverse=True)
    return output


def stations_highest_rel_level(stations, N):
    """Returns a list of the N stations at which the water level,
    relative to the typical range, is highest"""

    stations_relative_level = []

    for station in stations:
        relative_level = station.relative_water_level()

        # only append if relative level is present
        if relative_level != None:
            stations_relative_level.append((station, relative_level))

        stations_relative_level.sort(key=lambda x: x[1], reverse=True)
        output = stations_relative_level[:N]

    return output
    
    