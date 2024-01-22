#Using urllib in Python
'''
* Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.example.com/example.txt')
for line in fhand:
    print(line.decode().strip())

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.example.com/')
for line in fhand:
    print(line.decode().strip())
'''

#Reading Web Pages
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.google.com/')
for line in fhand :
    print(line.strip())
