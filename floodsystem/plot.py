#This submodule contains the function used to plot river-level data over a specified period of time

from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

stations = build_station_list 

def plot_water_levels(station, dates, levels): 

    #This function plots the water levels of a station

    t = dates
    level = levels

    #plot graph
    plt.plot(t, level, label ='Water Level')
    plt.plot(t, np.zeros(len(t))+station.typical_range[0], label='Typical Low Range')
    plt.plot(t, np.zeros(len(t))+station.typical_range[1], label='Typical High Range' )

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Dates')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title('{}'.format(station.name))
    plt.legend()

    # Display plot
    plt.tight_layout()  

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):

    #This function plots the water levels of a station

    t_1 = dates
    t_2 = matplotlib.dates.date2num(dates)
    level = levels

    #plot graph
    plt.plot(t_1, level, label ='Water Level')
    plt.plot(t_1, np.zeros(len(t_1))+station.typical_range[0], label='Typical Low Range')
    plt.plot(t_1, np.zeros(len(t_1))+station.typical_range[1], label='Typical High Range' )

    plt.plot(t_1, polyfit(dates, levels, p)[0](t_2 - polyfit(dates, levels, p)[1]), label='Best-Fit Polynomial of degree {}'.format(p))

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Dates')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title('{}'.format(station.name))
    plt.legend()

    # Display plot
    plt.tight_layout()  

    plt.show()










