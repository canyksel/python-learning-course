#What is a "Collection"?
'''
* A collection is nice because we can put more than one value in it and carry them all around in one convenient package
* We have a bunch of values in a sing "variable"
* We do this by having more than one place "in" the variable
* We have ways of finding the different places is the variable
'''

#What is not a "Collection"?
'''
* Most of our variables have one value in them - when we put a new value in the variable - the old value is overwritten
x = 2
x = 4
print(x) //4
'''

#A Story of Two Collections
#List
'''
* A linear collection of values that stay in order
'''

#Dictionary
'''
* A "bag" of values, each with its own label
* Dictionaries are Python's most powerful data collection
* Dictionaries allow us to do fast database-like operations in Python
* Dictionaries have different names in different language
    * Associative Arrays - Perl / PHP
    * Properties or Map or HashMap - Java
    * Property Bag - C# / .Net
* List index their entries based on the position in the list
* Dictionaries are like bags - no order
* So we index the things we put in the dictionary with a "lookup tag"
'''

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

print(purse)
print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse)

#Comparing Lists and Dictionaries
'''
* Dictionaries are like lists except that they use keys instead of numbers to look up values
'''

lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)

ddd['age'] = 23
print(ddd)

#Dictionary Literals (Constants)
'''
* Dictionary literals use curly braces and have a list of key : value pairs
* You can make an empty dictionary using empty curly braces
'''

jjj = {'chuck' : 1, 'fred' : 42, 'jan': 100}
print(jjj)

ooo = {} # it is same meanings as dict()
print(ooo)

#Most Common Name
#Many Counters with a Dictionary
'''
* One common use of dictionaries is counting how often we "see" something.
'''
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

#Dictionary Tracebacks
'''
* It is an error to reference a key which is not in the dictionary
* We can use the in operator to see if a key is in the dictionary

#Example
ccc = dict()
print(ccc[''])
'csev' in ccc //False
'''

#When we see a new name
'''
* When we encounter a new name, we need to add a new entry in the dictionary and if this the second or later time we have seen the name, we simply add one to the count in the dictionary under that name
'''

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

#The get method for dictionaries
'''
* The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called get() that does this for us
* We can use get() and provide a default value of zero when the key is not yet in the dictionary - and then just add one
'''

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

#Counting Pattern
'''
* The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently.
'''

counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()
print('Words:', words)

print('Counting...')
for word in words :
    counts[word] = counts.get(word,0) + 1
print('Counts',counts)

#Definite Loops and Dictionaries
'''
* Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary - actually it goes through all of the keys in the dictionary and looks up the values
'''

counts = {'chuck' : 1, 'fred' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

#Retrieving lists of Keys and Values
'''
* You can get a list of keys, values, or items(both) from a dictionary
'''

jjj = {'chuck' : 1, 'fred' : 42, 'jan': 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

#Bonus: Two Iteration Variables!
'''
* We loop through the key-value pairs in a dictionary using "two" iteration variables
* Each iteration, the first variable is the key and the second variable is the corresponding value for the key
'''

jjj = {'chuck' : 1, 'fred' : 42, 'jan': 100}
for aaa,bbb in jjj.items() :
    print(aaa, bbb)
