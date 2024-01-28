"""Write some code that uses the str.format() method to display the area of a circle
with a radius specified by the variable r. Use a keyword replacement field called area to
identify the calculated area and refer to this when passing the value to the str.format()
method. The output should look like the following, in the case where r is set to 52."""

import math


r = 52

area = math.pi * r**2
output = "The area of a circle with radius {} is {:.2f}".format(r, area)

print(output)


"""TASK: Convert the f-string based statement below into an equivalent that uses the
str.format() method to generate the same output."""

name = "Pratik"
age = 19
output = "{name:@^15} - {age:#^10}".format(name=name, age=age)
print(output)