#  Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before.

"""
userName=input("Enter your name: ")
if userName:
    print("Hello",userName)
else:
    print("Hello stranger ")
""" 


# Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error

"""setPass=input('Enter your password: ')
reEnter=input('Re enter the password: ')
if setPass==reEnter:
    print("Password set")
else:
    print("Wrong password try again")
  """
  
  
#   Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.  


"""
setPass=input('Enter your password: ')
reEnter=input('Re enter the password: ')
count=0

for i in setPass:
    count=count+1
    
if count>=8 and count<=12:
    if setPass==reEnter:
        print("Your password is set")

elif setPass!=reEnter:
    print("Password did not match")

else :
    print("Password is too short")
"""



"""Own Question"""
# write a python program that ask the user to enter the password and confirm it. If the password doesnot match display "Password didnot match" and if the length of password is not between 8 to 12 then display length error. There is a list of bad password that if user enters display the message "Bad Password". and the program should run until the user sucessfully enter the password

"""while True:
    userPass = input("Enter the password: ")
    reEnter = input("Re-enter the password: ")
    alreadyUsed = ['hello', 'password', 'admin', '123']
    check = 0
    countPass = 0

    for i in alreadyUsed:
        if i == userPass:
            check = check + 1

    for j in userPass:
        countPass = countPass + 1

    if check == 1:
        print("Password already used")

    elif userPass == reEnter and (countPass >= 8 and countPass <= 12):
        print("Password set successfully")
        break

    elif userPass != reEnter:
        print('You did not enter the same password')

    elif countPass < 8:
        print('Your password is too short')
 """
 
 
#  6. Write a program that displays the "Seven Times Table". That is, the result of
# multiplying 7 by every number from 0 to 12 inclusive. The output might start:
# 0 x 7 = 0
# 1 x 7 = 7
# 2 x 7 = 14
"""num=7
for i in range(13):
    print(i,"X",num,"=",num*i)
 """   
    
# Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive.

"""num=int(input("Enter the number:"))
for i in range(13):
    print(num,"X",i,"=",num*i)
"""  


# Write a Python program to print the following pattern:

# 1
# 22
# 333
# 4444
# 55555




# i=1
# while i<=5:
#     # print(i)
#     j=i
#     while j<=5:
#         print(i,end='')
#         j=j+1
#     print("\n")
#     i=i+1


i = 1

while i <= 5:
    j = 1
    while j <= i:
        print(i, end='')
        j = j + 1
    print("\n")
    i = i + 1






"""  
i=1  

while i<=5:
    j=1
    while j<=5:
        print("*",end="")
        j=j+1
    print("\n")
    i=i+1
"""
    




