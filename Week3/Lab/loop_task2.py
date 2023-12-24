# TASK: Input and execute a for loop that uses a range() function to generate the following
# output:
# 2 to the power of 2 = 4
# 4 to the power of 4 = 256
# 6 to the power of 6 = 46656
# 8 to the power of 8 = 16777216
# 10 to the power of 10 = 10000000000

num = int(input("Enter the range: "))
for j in range(2, num+2, 2):  
    result = j**j
    print(f"{j} to the power of {j} = {result}")

