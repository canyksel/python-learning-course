#Representing Simple Strings
'''
* Each character is represented by a number between 0 and 256 stored in 8 bits of memory
* We refer to "8 bits of memory as a "byte" of memory - (i.e. my disk drive contains 3 Terabytes of memory)"
* The ord() function tells us the numeric value of a simple ASCII character
'''

print(ord('H'))
print(ord('e'))
print(ord('\n'))

#Multi-Byte Characters
'''
* To represent the wide range of characters computers must handle we represent characters with more than one byte
    * UTF-16 — Fixed length - Two bytes
    * UTF-32 — Fixed length - Four bytes
    * UTF-8 — 1-4 bytes
        * Upwards compatible with ASCII
        * Automatic detection between ASCII and UTF-8
        * UTF-8 is recommended practice for encoding data to be exchanged between systems
'''

#Python Strings to Bytes
'''
* When we talk to an external resource like a network socker we send bytes, so we need to encode Python 3 strings into a given character encoding
* When we read data from an external resource, we must decode it based on the chracter set so it is properly represented in Python 3 as a string
* encode() -> string unicode to Bytes UTF-8
* decode() -> Bytes UTF-8 to string unicode
'''
