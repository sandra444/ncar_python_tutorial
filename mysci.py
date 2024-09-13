# for reference
# https://ncar.github.io/python-tutorial/tutorials/yourfirst.html


# Compute the wind chill temperature
def compute_windchill(t, v):
   a = 35.74
   b = 0.6215
   c = 35.75
   d = 0.4275

   v2 = v ** 2
   wci = a + (b * t) - (c * v2) + (d * t * v2)
   return wci
	
# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7, 'windchill': 12}

# float is a reference to the function
# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed': float, 'windchill': float}

# Initialize my data variable
data = {}

print('data1')
print(data)

for column in columns:
   data[column] = []

print('data2')
print(data)

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

   # Read the first three lines (header)
   for _ in range(3):
      datafile.readline()

   # Read and parse the rest of the file
   for line in datafile:
      split_line = line.split()
      for column in columns:
         i = columns[column]
         t = types.get(column, str)
         value = t(split_line[i])
         data[column].append(value)

windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
   windchill.append(compute_windchill(temp, windspeed))



# DEBUG
# print(data['tempout'])
print('----------MAIN------------')
# print(data['time'])

# example of zip - generates a tuple
# for x, y in zip([1, 2], [3, 4, 5]):
#    print('x, y:', x, y)

for key in data:
   print(key)
   print(data.get(key)[:5])

print('windchill[:5]')
print(windchill[:5])

print('See to compare')
i = 0
for wc_data, wc_comp in zip(data['windchill'], windchill):
   print(f'{wc_data:.5f}   {wc_comp:.5f}   {wc_data - wc_comp:.5f}')
   i = i+1
   if i > 6:
      break

# Output comparison of data
print('                ORIGINAL  COMPUTED')
print(' DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE')
print('------- ------ --------- --------- ----------')
zip_data = zip(data['date'], data['time'], data['windchill'], windchill)
for date, time, wc_orig, wc_comp in zip_data:
   wc_diff = wc_orig - wc_comp
   print(f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')


# i = 0
# for key, value in data.items():
#    print('i:', i)
#    print(key, value)
#    i = i+1
#    if i > 5:
#       break


