# for reference
# https://ncar.github.io/python-tutorial/tutorials/yourfirst.html

	
from mysci.p_readdata import read_data
from mysci.p_printing import print_comparison
from mysci.p_computation import compute_heatindex


# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'humout': 5, 'heatindex': 13}
# Data types for each column (only if non-string)
types = {'tempout': float, 'humout': float, 'heatindex': float}

data = read_data(columns, types=types)

# Compute the heat index
# heatindex = []
# for temp, hum in zip(data['tempout'], data['humout']):
#    heatindex.append(compute_heatindex(temp, hum))

# better way
# # Compute the heat index
heatindex = [compute_heatindex(t, h) for t, h in zip(data['tempout'], data['humout'])]

# Output comparison of data
print_comparison('HEAT INDX', data['date'], data['time'], data['heatindex'], heatindex)
