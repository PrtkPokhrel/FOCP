# TASK: Try writing an if statement similar to the last example that includes an extra elif
# clause to check ages between 30-40. Print a suitable message in the associated code block.

age=int(input("Enter your age: "))
if age>=18 and age<=30:
    print('You are still young')
elif age>30 and age<=40:
    print('You are neither young nor old')
elif age>40:
    print('You are old')
else:
    print("You are a child")
