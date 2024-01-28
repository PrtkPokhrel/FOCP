"""TASK: Use a text editor to create a file called info.txt and enter the text shown below.
Once the file has been created and saved, write a small program that:
1. Opens the file,
2. reads and prints the contents,
3. close file"""

f = open("Week8/Lab/info.txt","r") #
print(f.read())
f.close()



"""write a small program that opens the info.txt file, then reads and displays each of
the three lines of text using calls to the readline() method. Remember to close the file
once the content has been read."""



file = open("Week8/Lab/info.txt", "r")


for i in range(3):
    line = file.readline()
    print(line, end="")  

# Close the file
file.close()


"""write a small program that opens the info.txt file, then reads and displays each
line of text using a for...in loop. Remember to close the file once the content has been
read."""
myfile = open("Week8/Lab/info.txt","r")
for lines in myfile:
    print(lines)
myfile.close()