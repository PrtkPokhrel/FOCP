# TASK: Write some code that uses a list comprehension to create a list called cubes that
# contains the cubed values (x * x * x) of the numbers from 2 to 20 inclusive.


cubes = [x ** 3 for x in range(2, 21)]

print(cubes)
