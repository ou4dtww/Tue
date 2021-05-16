import re

# open file to write, create the file if necessary
print ("Reading data set 1")
f=open("mydata.txt", "w+")
f.write("apple orange apple banana apples melon grapes melon orange apple")

# close the file
f.close()

# read from file 'here.txt'
f=open("mydata.txt", "r")

# ensure file is available to read, and put contents into 'contents', and output
if f.mode == 'r':
    contents=f.read()
    print("Fruits:",re.sub(" ", ", ", contents))

# close the file 
f.close()
