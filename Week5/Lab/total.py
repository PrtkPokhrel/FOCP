# TASK: Use an editor to input the Python program shown below then save it to a file called
# total.py. Once that has been done, execute the program from the command line, passing
# several numeric values for testing.
# import sys
# count = len(sys.argv)
# total = 0
# while count > 1:
# count -= 1
# total += float(sys.argv[count])
# print("Total is", total)


import sys

count = len(sys.argv)
total = 0

while count > 1:
    count -= 1
    total += float(sys.argv[count])

print("Total is", total)

