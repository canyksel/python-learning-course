#Concatenating list using +
'''
* We can create a new list by adding two existing lists together
'''

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
c = b + a
print(c)
print(a)

#Lists can be sliced using :
'''
* Remember: Just like in strings, the second number is "up to but not including"
'''

t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

#List Methods
x = list()
type(x)
dir(x)

#Building a List from Scratch
'''
* We can add create an empty list and then add elements using the append method
* The list stays in order and new elements are added at the end of the list
'''

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

#Is Something in a List
'''
* Python provides two operators that let you check if an item is in a list
* These are logical operators that return True or False
* They do not modify the list
'''

some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)

#Lists are in Order
'''
* A list can hold many items and keeps those items in the order until we do something to change the order
* A list can be sorted
* The sort method (unlike in strings) means "sort yourself"
'''

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
print(friends[1])

#Built-in Functions and Lists
'''
* There are a number of functions built into Python that take lists as parameters
* Remember the loops we built? These are much simpler
'''

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

total = 0
count = 0
while True :
    inp = input('Enter a number ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count +1

average = total / count
print('Average:', average)

numlist = list()
while True :
    inp = input('Enter a number ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
