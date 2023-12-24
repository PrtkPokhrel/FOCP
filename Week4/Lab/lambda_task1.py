# TASK: Enter the example lambda expression shown above, then find out the data type of
# the hypot variable using a call to the type() function. Notice the result.


import math
hypot = lambda a,b : math.sqrt(a * a + b * b)
print(type(hypot(3,4)))