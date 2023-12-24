# Enter the example function shown above, then try calling it using the keyword
# arguments in several different orders

def someFunc(x, y, z):
    print("x is", x, "y is", y, "z is", z)
    
someFunc(1,2,3)
someFunc(y='hello', z='good', x='morning')
someFunc(y=6, z='seven', x='eight')
