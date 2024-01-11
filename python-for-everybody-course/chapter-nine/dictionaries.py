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
