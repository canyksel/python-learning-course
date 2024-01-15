#Sortin Lists of Tuples
'''
* We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
* First we sort the dictionary by the key using the items() method and sorted() function
'''

d = {'a': 10, 'b':1, 'c': 22}
print(d.items())
print(sorted(d.items()))

'''
* We can do this even more directly using the built-in functions sorted that takes a sequence as a parameter and returns a sorted sequence
'''

d = {'a': 10, 'b':1, 'c': 22}
t = sorted(d.items())
for key,value in t : 
    print(key,value)

'''
* If we could contruct a list of tuples of the form (value,key) we could sort by value
* We do this with a for loop that creates a list of tuples
'''

c = {'a': 10, 'b':1, 'c': 22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)


#The top 10 most commont words
fhand = open('romeo.txt')
counts = dict()

for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0) + 1

lst = list()
for key,val in counts.items() :
    newtup = (val,key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
for val,key in lst[:10] : 
    print(key, val)


#Even Shorter Version
'''
* List comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it
'''
c = {'a': 10, 'b':1, 'c': 22}
print(sorted([(v,k) for k,v in c.items()])) #Using [] -> We say the python "this is a list"