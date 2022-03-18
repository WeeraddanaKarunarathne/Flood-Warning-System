from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit, derivative
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import MonitoringStation
from floodsystem.plot import plot_water_level_with_fit

import datetime
import numpy as np

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stations_atrisk = []

    for station in stations:
        if station.relative_water_level() == None:
            continue
        if station.relative_water_level() > 1.6:
            stations_atrisk.append(station)
    
    station_assessment = []
    for station in stations_atrisk[:15]:
        relative_level = station.relative_water_level()

        dt=2
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        #output of gradient function attached to variable 'forecast' -> rising/falling/constant
        try:
            forecast = derivative(dates, levels, 4)
            print(forecast)
        except:
            print("error for " + station.name)

        #print(station.name, forecast, relative_level)

        #steps to determine risk assessment
        if relative_level >= 1.6 and forecast == 'rising':
            risk_assessment = 'severe'

        elif relative_level >= 1.6 and forecast == 'falling':
            risk_assessment = 'high'
        elif relative_level >= 1.2 and forecast == 'rising':
            risk_assessment = 'high'

        elif relative_level >= 1.2 and forecast == 'falling':
            risk_assessment = 'moderate'
        elif relative_level >= 0.8 and forecast == 'rising':
            risk_assessment = 'moderate'

        else:
            risk_assessment = 'low'

        station_assessment.append((station.name, relative_level, forecast, risk_assessment))

    station_assessment.sort(key=lambda x: x[1], reverse = True)
    for station in station_assessment[:10]:
        print(station[0] + "   " + str(station[1]) + "   " + station[2] + "   " + station[3] ) 
        


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()