
# squares = [4, 9, 16, 25]
# TASK: Write a for..in loop that iterates over all the elements of the squares list and
# prints the square root of each to the screen. Hint: you may want to import a function from
# the math module to help achieve this.

"""
from math import sqrt

squares=[4,9,16,25]
for i in squares:
    result=sqrt(i)
    print(result)
    
"""    
# TASK: Write some code that uses the append() method to add the next three square
# values (49, 64, 81) to the end of the squares list.

from math import sqrt

squares=[4,9,16,25]
sqrAppend=[49, 64, 81]

for i in squares:
    result=sqrt(i)
    print(result)

for i in sqrAppend:
    result=sqrt(i)
    print(result)