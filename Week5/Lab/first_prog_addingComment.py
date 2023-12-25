# TASK: Open the first_prog.py and add comments above each statement within the file
# describing what that statement does (using a ‘#’ at the beginning of the line) . Save the file
# and execute it again for testing purposes.


# Input the number and assign it to the variable number
number = input("Enter a number: ")
# Changes the datatype to int from string
number = int(number)
# Display the result with a message
print("The numbered entered was", number)
# Check if the number is  even 
if (number % 2) == 0:
#Display the following message if the number is even  
 print("That is an even number")
#  Else
else:
# Display the following message if the number is odd
 print("That is an odd number")
