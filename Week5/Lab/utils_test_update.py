# TASK: Update the previous program utils_test.py, so that the import statement
# explicitly imports the average() function directly into the program’s symbol table, allowing
# the prefix to be removed from the later function calls.

from my_utils import average

print(average([1,2,3,4]))
print(average([123,124,51]))
