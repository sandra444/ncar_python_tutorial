# for reference
# https://ncar.github.io/python-tutorial/tutorials/yourfirst.html

# Initialize my data variable
data = []

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

 # Read the first three lines (header)
 # _ means we are not going to call it, but you can use a character instead
    for _ in range(3):
        print('_', _)
        # datafile.readline()
        print(datafile.readline())

    # Read and parse the rest of the file
    j = 0
    for line in datafile:
        datum = line.split()
        data.append(datum)
        j = j+1
        if j < 6:
            print('\nline:', line)
            print('datum', datum, '\n')

# DEBUG
i = 0
for datum in data:
   print(datum)
   i = i+1
   if i > 5:
      break

print('##data[0]:', data[0])
print('##data[9]:', data[9])
print('##data[-1]:', data[-1])

# note that data[0:10] gives us a list
for datum in data[0:10]:
   print(datum)

print('##data[:10]:', data[:10])
print('##data[0:10:2]:', data[0:10:2])
print('##data[slice(0,10,2)]:', data[slice(0,10,2)])


print('##data[:4]:', data[:4])
print('##data[0:4:2]:', data[0:4:2])
print('##data[slice(0,4,2)]:', data[slice(0,4,2)])

print('##data[8]:', data[8])
print('##data[8][4]:', data[8][4])
print('##data[8][:5]:', data[8][:5])
print('##data[8][::2]:',data[8][::2])

print('##data[5:8][2]:', data[5:8][2])
