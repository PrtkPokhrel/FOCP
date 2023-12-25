# TASK: Use sequence unpacking to extract the values you stored within the address tuple
# earlier. Unpack the tuple into variables named house_num, street and postcode.

"""
address = ("000", " 3rd Street", "2023")


house_num, street, postcode = address


print("House Number:", house_num)
print("Street:", street)
print("Postcode:", postcode)
"""


# TASK: Write some code that calls the print() function to output the contents of the
# address tuple you created earlier. Ensure you use the ‘*’ prefix so that the elements are
# extracted before being passed to the function. Compare this with a version of the same code
# that calls the print() function without using the ‘*’ prefix,



address = ("000", " 3rd Street", "2023")

print(*address)

print(address)
