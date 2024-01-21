#String Parsing Examples
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1: sppos]
print(host)

#The Double Split Pattern
'''
* Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again
'''

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

#The Regex Version
import re
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', line)
z = re.findall('^From .*@([^ ]*)', line)
print(y)
print(z)

#Spam Confidence
'''
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand :
    line = line.rstrip()
    stuff = re.findall('^XDSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)

print('Maximum:', max(numlist))
'''

#Escape Character
'''
* If you want a special regular expression character to just behave normally (most of the time) you prefix with '\'
'''

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)