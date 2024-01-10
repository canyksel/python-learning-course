#Best Friends: Strings and Lists
'''
* Split breaks a string into parts and produces a list of strings. We think of these as words. We can access a particular word or loop through all the words.
'''
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

for w in stuff :
    print(w)

'''
* When you do not specify a delimiter, multiple spaces are treated like one delimiter
* You can specify what delimiter character to use in the splitting
'''

line = 'A lot               of spaces'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(';')
print(thing)
print(len(thing))

fhand = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
for line in fhand :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words)

#The Double Split Pattern
'''
* Sometimes we split a line one way and then grab one of the pieces of the line and split that piece agaig
'''

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces)
print(email)