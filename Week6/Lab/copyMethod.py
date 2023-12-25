# TASK: Write some code that makes a copy of the colours using the copy() method.
# Then make some changes to the original list. Print the contents of the copied list to ensure
# these changes have not affected the copy.

colours = ["red", "green", "yellow", "blue", "red"]


colorCopy = colours.copy()

# Make some changes to the original 'colours' list
colours.append("orange")
colours.append("black")
colours.pop(0)

# Print the contents of the copied list to ensure changes haven't affected it
print("Original Color List:", colours)
print("Copied Color List:", colorCopy)
