# Last week you wrote a program that printed out a cheery greeting including your
# name. Take a copy of it, and modify it so that the user enters their name at the
# keyboard, and then receives a greeting. For example:
# Hello, what is your name? Mr Apricot
# Hello, Mr Apricot. Good to meet you!

"""userName=input("Hello, what is your name? ")
print(f"Hello, {userName}. Good to meet you")
"""

#  Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
# Enter a temperature in Celsius: 32.5
# 32.5C is equivalent to 90.5F.


"""temCelsius=float(input("Enter a temperature in Celsius: "))
convert=(temCelsius*9/5)+32
print(f"{temCelsius} is equivalent to {convert}F")
"""

# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but this is
# sometimes varied to create groups of similar size. Write a program that prompts for
# the number of students and group size, and then displays how many groups will be
# needed and how many will be left over in a smaller group.
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101
# students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.



studentNum=int(input("How many students? "))
groupSize=5
leftStudent=studentNum%groupSize
grouping=studentNum/groupSize

print(f"There will be {int(grouping)} groups with {int(leftStudent)} student left over")
