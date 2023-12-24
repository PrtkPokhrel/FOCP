# """TASK: Write code that uses slicing to access then print the first four prime numbers defined
# within the ‘primes’ list given above. Note: you will have to input that list first for testing
# purposes."""

primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


first_four_primes = primes[:4]


print(first_four_primes)



# """TASK: Write code that uses slicing to insert two new names just before the final name within
# the 'names' list."""

names = ["Tim", "Bill", "Graeme", "John", "Brian"]


final_name_index = len(names) - 1


names[final_name_index:final_name_index] = ["Alice", "Bob"]


print(names)



# """
# Lists also support the * operator in the same way as strings. This allows the contents of a
# list to be duplicated a number of times, e.g.
# nums = [1,2,3] * 5
# TASK: Work out in your head what the contents of the ‘nums’ list would be, then check this
# using the Python interpreter."""
nums = [1, 2, 3] * 5
print(nums)