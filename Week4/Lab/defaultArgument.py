# TASK: Define a function that takes two numeric values, multiplies them together then returns
# the result. If the function is called with only a single argument however, then the value should
# be multiplied by itself. Once the function is defined, call it several times and display the
# returned values for testing purposes.


def operations(num1,num2=None):
    """The function 'operation' takes two argument 'num1' and 'num2' of which 'num2' is a default argument which
    has been assigned value None. Further an if statement is used to check whether one or two argument has been 
    provided, and the result is returned. Also if there is single value it multiplies itself but with two values  
    it multiplies together."""
    
    if num2 is not None:
        return num1*num2 
    else:
        return num1*num1


print(operations(3))
print(operations(1,8))
print(operations(9))
print(operations(4,2))

