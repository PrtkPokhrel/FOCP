# TASK: Input the following code, when asked to type your age input a numeric value such as
# 20. Does this program work? If not, why?


age = input("Enter your age ")
print("in one year your age will be", age + 1)

# The program doesnot run beacuse the age is of string type and string is incapable of performing \
# aritmetic operation


# Output
# Traceback (most recent call last):
#   File "/home/mint/Documents/FOCP /Week2/lab/task8.py", line 6, in <module>
#     print("in one year your age will be", age + 1)
# TypeError: can only concatenate str (not "int") to str
