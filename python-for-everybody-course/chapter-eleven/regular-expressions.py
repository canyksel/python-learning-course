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