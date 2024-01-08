#File Handle as a Sequence
'''
* A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
* We can use the for statement to iterate through a sequence
* Remember - a sequence is an ordered set
#Example:
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

'''

#Counting Lines in a File
'''
* Open a file read-only
* Use a for loop to read each line
* Count the lines and print out the number of lines

#Example:
fhand = open('mbox.txt')
count = 0
for line in fhand :
    count = count + 1
print('Line Count:', count)
'''

#Reading the *Whole* File
'''
* We can read the whole file (newlines and all) into a single string

#Example
fhand = opena('mbox-short.txt')
inp = fhand.read()
pring(len(inp))
print(inp[:20])
'''

#Searching Through a File
'''
* We can put an if statement in our for loop to only print lines that meet some criteria

#Example
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:') :
        print(line)

* Each line from the file has a newline at the end
* The print statement adds a newline to each line
* We can strip the whitespace from the right-hand side of the string using rstrip() from the string library
* The newline is considered "white space" and is stripped

#Example
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
'''

#Skipping with continue
'''
* We can conveniently skip a line by using the continue statement

#Example
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
'''

#Using in to select lines
'''
* We can look for a string anywhere in a line as our selection criteria

#Example
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line :
        continue
    print(line)
'''

#Prompt for File Name
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

#Bad file Names
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
