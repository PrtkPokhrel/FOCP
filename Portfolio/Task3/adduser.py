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

def addingUser():
    """
    The function adds a new user to the passwd.txt with hashed password and return errors if
    the username already exist if not then new user can be added.
    """
    # Gets necessary information from user and store in seperate variable
    userName = input("Enter new user name: ")
    realName = input("Enter real name: ")
    passwd = getpass.getpass("Enter password: ")

    # Hash the password
    hashed_password = hash_password(passwd)

    # Check if the username already exists
    with open('passwd.txt', 'r') as g:
        for line in g:
            columns = line.strip().split(':')
            if columns[0] == userName:
                print('Cannot add. Most likely username already exists.')
                exit()

    # Appends the uset detail to passwwd.txt
    with open('passwd.txt', 'a') as f:
        f.write(userName)
        f.write(':')
        f.write(realName)
        f.write(':')
        f.write(hashed_password)
        f.write('\n')
        print('User Created')

# Calls the function 
addingUser()
