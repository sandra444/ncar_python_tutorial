# for reference
# https://ncar.github.io/python-tutorial/tutorials/yourfirst.html

# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2}

# Data types for each column (only if non-string)
# float is a reference to the function
types = {'tempout': float}

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

# # DEBUG
# print(data['tempout'])

# DEBUG
print('----------')
# print(data['time'])

for key in data:
   print(key)
   print(data.get(key)[:5])



# i = 0
# for key, value in data.items():
#    print('i:', i)
#    print(key, value)
#    i = i+1
#    if i > 5:
#       break