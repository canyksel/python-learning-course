#Definite Loops
'''
* Quite often we have a list of items of the lines in a file - effectively a finite set of things
* We can write a loop to run the loop once for each of the items in a set using the Python for consturct
* These loops are called "definite loops" because the execute an exact number of times
* We say that "definite loops iterate through the members of a set"
'''

#A Simple Definite Loop
for i in [5,4,3,2,1]:
    print(i)
print('Blasstoff!')

#A Definite Loop with Strings
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

'''
* The iteration variable "iterates" through the sequence (ordered set)
* The block (body) of code is executed once for each value in the sequence
* The iteration variable moves through all values in the sequence
'''