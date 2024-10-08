# for reference
# https://ncar.github.io/python-tutorial/tutorials/yourfirst.html

# Initialize my data variable
data = {'date': [],
  'time': [],
  'tempout': []}

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

   # Read the first three lines (header)
   for _ in range(3):
      datafile.readline()

   # Read and parse the rest of the file
   for line in datafile:
      split_line = line.split()
      data['date'].append(split_line[0])
      data['time'].append(split_line[1])
      data['tempout'].append(float(split_line[2]))

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