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