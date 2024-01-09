# A List is a kind of Collection
'''
* A collection allows us to put many values in a single "variable"
* A collection is nice because we can carry all many values around in one convenient package.

friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']
'''

#List Constants
'''
* List constants are surrounded by square brackets and the elements in the list are separated by commas
* A list element can be any Python object-even another list
* A list cn be empty
'''

print([1, 24 ,76])
print(['red', 'yellow', 'blue'])
print(['red', 24, 98.6])
print([1, [5, 6], 7])
print([])

for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')

z = ['Joseph', 'Glenn', 'Sally']
for x in z:
        print('Happy New Year:', x)
print('Done!')

#Looking Inside Lists
'''
* Just like strings, we can get at any single element in a list using an index specified in square brackets
'''

friends = ['Joseph', 'Glenn', 'Sally'] #[0, 1, 2]
print(friends[1])

#List are Mutable
'''
* Strings are "immutable" - we cannot change the contents of a string - we must make a new string to make any change
* Lists are "mutable" - we can change an element of a list using the index operator
'''

'''
fruit = 'Banana'
fruit[0] = 'b'
-> Throws an error
'''
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)

#How Long is a List?
'''
* The len() function takes a list as a parameter and returns the number of elements in the list
* Actually len() tells us the number or elements of any set or sequence (such as a strin...)
'''
greet = 'Hello Bob'
print(len(greet))
x = [1, 2, 'joe', 99]
print(len(x))

'''
#Using the range function
* The range function returns a list of numbers that range from zero to one less than the parameter
* We can construct an index loop using for and an integer iterator
'''

print(range(4))
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
print(range(len(friends)))

#A tale of two loops
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year', friend)