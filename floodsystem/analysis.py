#This submodule contains a function that computes the least-squares fit for a station, given its water level data

import numpy as np
import matplotlib

def polyfit(dates, levels, p):

    x = matplotlib.dates.date2num(dates)
    d0 = np.amin(x)
    x = x - d0
    y = levels

    # Find coefficients of best-fit polynomial
    p_coeff = np.polyfit(x, y, p)

    # Convert coefficients into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return poly, d0   

def derivative(dates, levels, p):

    x = matplotlib.dates.date2num(dates)
    d0 = np.amin(x)
    x = x - d0
    y = levels

    # Find coefficients of best-fit polynomial  
    p_coeff = np.polyfit(x, y, p)

    first_derivative = np.polyder(p_coeff)
    first_derivative_poly = np.poly1d(first_derivative)

    if first_derivative_poly(x[-1]) >= 0:
        return 'rising'
    else:
        return 'falling'
                  

