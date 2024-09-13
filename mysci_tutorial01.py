# for reference
# https://ncar.github.io/python-tutorial/tutorials/yourfirst.html


# Read the data file
# import os
# script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
# sub_dir = "data"
# filetxt = "wxobs20170821.txt"
# filename = os.path.join(script_dir, sub_dir, filetxt)
# print('filename:', filename)

# Using relative path
filename = "data/wxobs20170821.txt"
datafile = open(filename, 'r')


# use a context manager to self clean-up
with open(filename, 'r') as datafile:
   data = datafile.read()

print('data')
print(data)
print(type(data))


# Another way, must open and close yourself
# datafile = open(filename, 'r')
# data = datafile.read()
# datafile.close()

# Just to see if we are working
# maybe want to use this to get the header line
# datafile = open(filename, 'r')
# print(datafile.readline())
# print(datafile.readline())
# print(datafile.readline())
# print(datafile.readline())
# datafile.close()
