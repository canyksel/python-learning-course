#Regular Expressions
'''
* Very powerful and quite cryptic
* Fun once you understand them
* Regular expressions are a language unto themselves
* A language of "marker characters" - programming with characters
* It is kind of "old school" language - compact
'''

#Regular Expression Quick Guide
'''
^ -> Matches the beginning of a line
$ -> Matches the end of the line
. -> Matches any character
\s -> Matches whitespace
\S -> Matches any non-whitespace characters
* -> Repeats a character zero or more times
*? -> Repeats a character zero or more times (non-greedy)
+ -> Repeats a character one or more times
+? -> Repeats a character zero or more times (non-greedy)
[aeiou] -> Matches a single character in the listed set
[^XYZ] -> Matches a single character not in the listed set
[a-z0-9] -> The set of characters can include a range
( -> Indicates where string extraction is to start
) -> Indicates where string extraction is to end
'''

#The Regular Expression Module
'''
* Before you can use regular expressions in your program, you must import the library using "import re"
* You can use re.search() to see if a string matches a regular expression, similar to using the find() method for strings
* You can use re.findall() to exract portions of a string that match your regular expression, similar to combination of find() an slicing: var[5:10]


#Using re.search() like startswith()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

* We fine-tune what is matched by adding special characters to the strings
'''

#Wild-Card Characters
'''
* The dot character matches any character
* If you add the asterisk character, the character is "any number of times"

Example-1:
pattern -> "^X.*:"
X-Sieve: CMU Sieve 2.3
X-DSPAM-Result: Innocent
X-DSPAM-Confidence: 0.84.75
X-Content-Type-Message-Body: text/plain
(All texts matched until ":" character)

Example-2:
pattern -> "^X-\S+:"
X-Sieve: CMU Sieve 2.3
X-DSPAM-Result: Innocent
X-Plane is behind schedule: two weeks
(Third one did not matched)
'''

#Matching and Extracting Data
'''
* re.search() returns a True/False depending on whether the string matches the regular expression
* If we actually want the matching strings to be extracted, we use re.findall()
'''

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y) #['2', '19', '42']

'''
* When we use re.findall(), it returns a list of zero or more sub-strings that match the regular expression
'''

y = re.findall('[AEIOU]+',x)
print(y) #[]

#Warning: Greedy Matching
'''
* The repeat characters (* and +) push outward in both directions (greedy) to match largest possible string
'''

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y) #['From: Using the :']

#Non-Greedy Matching
'''
* Not all regular expression repeat codes are greedy! If you add a ? character, the + and * chill out a bit
'''

y = re.findall('^F.+?:', x)
print(y) #['From:']

#Fine-Tuning String Extraction
'''
* You can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parentheses
'''

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y) #['stephen.marquard@uct.ac.za']

'''
* Parentheses are not part of the match-but they tell where to start and stop what string to extract
'''

y = re.findall('From (\S+@\S+)',x)
print(y) #['stephen.marquard@uct.ac.za']