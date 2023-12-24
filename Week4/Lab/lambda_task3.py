# TASK: Improve your previous lambda expression so that if only one argument is passed
# within a call, then the number of minutes defaults to 0, as detailed below:
# >>> to_seconds(1)
# 3600
# >>> to_seconds(2)
# 7200TASK: Improve your previous lambda expression so that if only one argument is passed
# within a call, then the number of minutes defaults to 0, as detailed below:
# >>> to_seconds(1)
# 3600
# >>> to_seconds(2)
# 7200

to_seconds = lambda hours, minutes=0: hours * 3600 + minutes * 60
result1 = to_seconds(1, 30) 
result2 = to_seconds(2, 45)  
result3 = to_seconds(3)      
print("Result 1:", result1, "seconds")
print("Result 2:", result2, "seconds")
print("Result 3:", result3, "seconds")