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

def check_login(username, password):
    """
    Checks if the provided username and password match the stored hashed password.

    Parameters:
    - username (str): The username to be checked.
    - password (str): The password to be checked.

    Returns:
    - bool: True if the login is successful, False otherwise.
    """
    with open('passwd.txt', 'r') as f:
        for line in f:
            columns = line.strip().split(':')
            if columns[0] == username:
                stored_password = columns[2]
                hashed_password = hash_password(password)

                if stored_password == hashed_password:
                    return True

    return False

def login():
    """
    Prompts the user to enter their username and password and checks for login validity.
    """
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    if check_login(username, password):
        print("Access Granted")
    else:
        print("Access Denied")

login()
