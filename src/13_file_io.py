"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
foo = open("foo.txt", "r")
read_data = foo.read()
# Print all the contents of the file, then close the file

print(read_data)
foo.close()
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. 

bar = open("bar.txt", "w")

# Write three lines of arbitrary content to that file,

lines = ["This is the first string\n", "this is the second\n", "that second string has bad capitalization"] 
bar.writelines(lines)

# then close the file. 

bar.close()

# Open up "bar.txt" and inspect it to make

bar_open = open("bar.txt", "r")
read_data = bar_open.read()

# Print all the contents of the file, then close the file
# sure that it contains what you expect it to contain

print(read_data)
bar_open.close()

# YOUR CODE HERE