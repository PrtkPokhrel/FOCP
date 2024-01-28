#!/usr/bin/env python3
import getpass
import hashlib 

def hash_password(password):
    """
    Hashes the provided password using SHA-256.

    Parameters:
    - password (str): The password to be hashed.

    Returns:
    - str: The hashed password.
    """
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def change_password():
    """        
    The function takes the user input for their username, real name, current password and new password and
    checks if the provided username, real name and current password matches the stored hashed password. If matched everythin new 
    password can be updated with new hashed password else error message is shown and the password is not changed
    """
    
    # Takes user input to and store in necessary variables also assigns current and new password with their hashed value in two differenct variable
    userName = input("User: ")
    realName = input("Real Name: ")
    currentPass = getpass.getpass("Current Password: ")
    newPass = getpass.getpass("New Password: ")  
    hashed_current_password = hash_password(currentPass)
    hashed_new_password = hash_password(newPass)


#   Reads all line from passwd.txt
    with open('passwd.txt', 'r') as f:
        lines = f.readlines()

    found_user = False 

    with open('passwd.txt', 'w') as g:
        for line in lines:
            columns = line.strip().split(':')
            # If username real mane and current password match then password can be changed
            if columns[0] == userName and columns[1] == realName and columns[2] == hashed_current_password:
                # Write the modified line with the new hashed password
                g.write(userName)
                g.write(':')
                g.write(realName)
                g.write(':')
                g.write(hashed_new_password)
                g.write('\n')
                found_user = True
                
                # If condition doenot match than the information remains unchanged.
            else:
                
                g.write(line)

# If the condition is matched then the variable found_user becomes true  which prints the message 'Password Changed'
    if found_user:
        print('Password Changed')
# Else the false value prompts to print error message
    else:
        print('Error: User not found or current password is incorrect')

# Call the function to change the password
change_password()
