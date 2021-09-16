# f = open("sample.txt", 'r')

# By default the mode is read
f = open("sample.txt",)

# This will read the whole file
# data = f.read()

# This will only read  character from the file
# data = f.read(5)

# This will read the first line from file
data = f.readline()
print(data)
# This will read the second line from file
data = f.readline()
print(data)
# This will read the third line from file
data = f.readline()
print(data)
f.close()

# Write into a file.
f = open('anotherFile.txt', 'w')
f.write("This is just another text file")
f.close()


# Appending into a file
f = open('anotherFile.txt', 'a')
f.write(" Appending data into this file")
f.close()

# The best way to open and close a file is with statement. because it will automatically close the file
with open("anotherFile.txt", 'r') as f:
    print(f.read())
