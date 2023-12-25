# TASK: Improve the program once more by adding a check to see whether no arguments
# have been passed, if so print a message saying “no arguments were provided”. Also
# add comments to the program. Execute the program several times for testing.

# Imports sys
import sys

# Get the number of command-line arguments
count = len(sys.argv)

# Initialize variables for total and average
total = 0

# Check whether  arguments is provided
if count > 1:
    # Loop through the command-line arguments and calculate the total
    while count > 1:
        count -= 1
        total += float(sys.argv[count])

    # Calculate  average
    average = total / (len(sys.argv) - 1)

    # Display the total and average
    print("Total is", total)
    print("Average is", average)
else:
    # Display the following message if arguments is not provided
    print("No arguments were provided")

