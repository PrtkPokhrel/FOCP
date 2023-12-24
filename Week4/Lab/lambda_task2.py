# TASK: Write a lambda expression that takes two formal parameters, hours and minutes.
# The expression should calculate and return the total number of equivalent seconds. Assign
# the expression to a variable called to_seconds, then call the function several times for
# testing.

to_seconds = lambda hours, minutes: hours * 3600 + minutes * 60


result1 = to_seconds(1, 30)  # 1 hour and 30 minutes
result2 = to_seconds(2, 45)  # 2 hours and 45 minutes
result3 = to_seconds(0, 15)  # 15 minutes
print("Result 1:", result1, "seconds")
print("Result 2:", result2, "seconds")
print("Result 3:", result3, "seconds")
