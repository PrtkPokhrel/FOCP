# Functions are often used to validate input. Write a function that accepts a single
# integer as a parameter and returns True if the integer is in the range 0 to 100
# (inclusive), or False otherwise. Write a short program to test the function.


"""def test(singleInt):
    if singleInt in range(0,101):
        return True
    else:
        return False

singleInt=int(input("Enter the number: "))
print(test(singleInt))
"""

# Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.

"""def test(singleStr):
   upp=0
   low=0
   for i in singleStr:
       if i.isupper() :
           upp=upp+1
       else:
           low=low+1
   return upp,low

singleStr=input("Enter the name: ")
print(test(singleStr))
"""


# Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name differently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur


"""
def greet(greetings):
    if greetings:
        return greetings[0].upper()+greetings[1:].lower()

greetings=input("Enter the string: ")
print(greet(greetings))
"""


# When processing data it is often useful to remove the last character from some
# input (it is often a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)

"""def removeLast(oneStr):
    count=0
    for i in oneStr:
        count=count+1
    if count>1:
        
        return oneStr[:-1]
    else:
        return oneStr

oneStr=input("Enter the string:  ")
print(removeLast(oneStr))
"""

# Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae)

"""def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_result = celsius_to_fahrenheit(celsius_input)
print(f"{celsius_input} degrees Celsius is {fahrenheit_result:.2f} degrees Fahrenheit.")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_result = fahrenheit_to_celsius(fahrenheit_input)
print(f"{fahrenheit_input} degrees Fahrenheit is {celsius_result:.2f} degrees Celsius.")"""








