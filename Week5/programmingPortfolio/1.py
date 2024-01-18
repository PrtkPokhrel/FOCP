# Using command-line arguments involves the sys module. Review the docs for this
# module and using the information in there write a short program that when run
# from the command-line reports what operating system platform is being used.

'''import sys

def report_platform():
    platform = sys.platform
    print(f"The operating system platform is: {platform}")

if __name__ == "__main__":
    report_platform()
'''

# 2. Write a program that, when run from the command line, reports how many
# arguments were provided. (Remember that the program name itself is not an
# argument)

"""import sys
num=sys.argv
length=len(sys.argv[1:])
print(f"{length} arguments were provided")
"""

# Write a program that takes a bunch of command-line arguments, and then prints
# out the shortest. If there is more than one of the shortest length, any will do.    

    
"""import sys

if __name__ == "__main__":
    command_line_arguments = sys.argv[1:]

    if command_line_arguments:
        shortest_argument = sorted(command_line_arguments, key=len)[0]
        print("The shortest argument is:", shortest_argument)
    else:
        print("No arguments provided.")
"""


# 4. Write a program that takes a URL as a command-line argument and reports
# whether or not there is a working website at that address.
# Hint: You need to get the HTTP response code.
# Another Hint: StackOverflow is your friend.

"""import sys
import requests

def check_website(url):
    try:
        response = requests.get(url)
        # response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        print(f"The website at {url} is accessible.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to access the website at {url}. Error: {e}")

if __name__ == "__main__":
    # Exclude the first argument (script name) and consider the second as the URL
    if len(sys.argv) != 2:
        print("Usage: python check_website.py <URL>")
    else:
        url = sys.argv[1]
        check_website(url)
"""
  




    



