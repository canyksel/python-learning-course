#Tuples are like lists
'''
* Tuples are another kind of sequence that functions much like a list - they have elements which are indexed starting at 0
'''
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
y =  (1, 9, 2)
print(y)
print(max(y))

for iter in y :
    print(iter)

'''
* Tuples are "immutable"
* Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string
'''

x = [9, 8, 7]
x[2] = 6
print(x)

'''
y = 'ABC'
y[2] = 'D' //Throw an error

z = (5, 4, 3)
z[2] = 0 //Throw an error
'''

#Things not to do with tuples
'''
x = (3, 2, 1)
x.sort() // Throw an error
x.append(5) //Throw an error
x.reverse() //Throw an error
'''

#Tuples are more efficient
'''
* Since Python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terms of memory use and performance than lists
* So in our program when we are making "temporary variables" we prefer tuples over lists
'''

#Tuples and Assignment
'''
* We can also put a tuple on the left-hand side of an assignment statement
* We can even omit the parentheses
'''

(x, y) = (4, 'fred')
print(y)

(a, b) = (99, 98)
print(a)

#Tuples and Dictionaries
'''
* The items() method in dictionaries returns a list of (key, value) tuples
'''

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (key,value) in d.items() :
    print(key,value)

tups = d.items()
print(tups)

#Tuples are Comparable
'''
* The comparison operator work with tuples and other sequences. If the firs item is equal, Python goes on the next element, and so on, until it finds elements that differ
(0, 1, 2) < (5, 1, 2) // True
(0, 1, 2000000) < (0, 3, 4) // True
('Jones', 'Sally') < ('Jones', 'Sam') // True
('Jones', 'Sally') > ('Adams', 'Sam') // True
'''
