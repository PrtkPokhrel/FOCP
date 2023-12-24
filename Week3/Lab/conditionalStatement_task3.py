# TASK: Rewrite the above code that inputs a name then prints a message, but change the
# condition so it explicitly uses a Boolean expression.

name = input("Enter your name: ")
if bool(name):
    print("Your name is", name)
else:
    print("Name not entered")
