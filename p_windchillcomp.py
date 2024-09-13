# for reference
# https://ncar.github.io/python-tutorial/tutorials/yourfirst.html

	
from mysci.p_readdata import read_data
from mysci.p_printing import print_comparison
from mysci.p_computation import compute_windchill

  
# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7, 'windchill': 12}

# float is a reference to the function
# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed': float, 'windchill': float}

data = read_data(columns, types=types)

# Compute the wind chill factor
# windchill = []
# for temp, windspeed in zip(data['tempout'], data['windspeed']):
#    windchill.append(compute_windchill(temp, windspeed))

# better way
# Compute the wind chill factor
windchill = [compute_windchill(t, w) for t, w in zip(data['tempout'], data['windspeed'])]

# Output comparison of data
print_comparison('WINDCHILL', data['date'], data['time'], data['windchill'], windchill)
