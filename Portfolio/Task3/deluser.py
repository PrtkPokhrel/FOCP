#!/usr/bin/env python3
import getpass
import hashlib

def hash_password(password):
    # Using SHA-256 for hashing
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def delUser():
    """
    The function deletes the user from passwd.txt based on the provided username, real name, and password.
    """
    
    # Gets necessary information from the user and stores it in respective variables
    fileName = 'passwd.txt'
    userName = input("Enter the username: ")
    realName = input("Enter your real name: ")
    passwd = getpass.getpass("Enter the password: ")

    user_found = False  # Initialize a flag to track whether the user is found

    # readlines() reads all the lines from the passwd.txt
    with open(fileName, 'r') as f:
        lines = f.readlines()

    # Open the file in write mode to overwrite the content
    with open(fileName, 'w') as f:
        for line in lines:
            columns = line.strip().split(':')
            if columns[0] == userName and columns[1] == realName:
                stored_password = columns[2]
                hashed_password = hash_password(passwd)

                if stored_password == hashed_password:
                    user_found = True
                    continue  # Skip writing the line for the user to be deleted
            f.write(line)

    if user_found:
        print('User deleted.')
    else:
        print('Error: User not found or password incorrect.')

# Call the function to delete a user
delUser()
