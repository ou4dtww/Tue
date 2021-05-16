import re

# function to count words in string contents
def word_count(string):
    return(len(string.strip().split(" ")))

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

# Give total quantity
print("Total Fruits:",word_count(contents))

# Output as a set occurence of word in string 'contents'
# Use / build up a dictionary of plural words, replace plural 
# as singular, and count them as single occurence
# e.g. each 'apples' is changed to 'apple' and counted as 1

# Create a set type, split the words, and change data type of contents
set1=set()
contents=contents.split(" ")
a=0

# see explanation above
for x in contents:
    a=a+1
    if x == 'apples':
        contents[a] = 'apple'

# reset counter
a=0

# build up the set 
for i in contents:
    set1.add((i,contents.count(i)))

print("Total fruits and quantity for each:", set1)

# close the file 
f.close()
