#String Library
'''
* str.capitalize()
* str.replace(old, new[, count])
* str.center(width[,fillchar])
* str.lower()
* str.endswith(suffix[, start[, end]])
* str.rstrip([chars])
* str.find(sub[, start[, end]])
* str.strip([chars])
* str.lstrip([chars])
* str.upper()
'''

#Searching a String
'''
* We use the find() function to search for a substring within another string
* find() finds the first occurrence of the substring
* If the substring is not found, find() returns -1
* Remember that string position starts at zero
'''

fruit = 'banana'
pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)

#Making everthing UPPER CASE
'''
* You can make a copy of a string in lower case or upper case
* Ofter when we are searching for a string using find() we firs convert the string to lower case so we can search a string regardless of case
'''

greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)

www = greet.lower()
print(www)

#Search and Replace
'''
* The replace() function is like a "search and replace" operation in a word processor
* It replaces all occurrences of the search string the replacement string
'''

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Can')
print(nstr)

nstr = greet.replace('o', 'X')
print(nstr)

#Stripping Whitespace
'''
* Sometimes we want to take a string and remove whitespace at the beginning and/or end
* lstrip() and rstrip() remove whitespaces at the left or right
* strip() removes both beginning and ending whitespace
'''

greet = '    Hello Bob      '
greet.lstrip()
greet.rstrip()
greet.strip()

#Prefixes
line = 'Please have a nice day'
line.startswith('Please') #True
line.startswith('p') #False

#Parsing and Extracting
data = ' From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

#Two Kinds of Strings
'''
* In Python 3, all strings are Unicode
'''