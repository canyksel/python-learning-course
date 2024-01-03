#Stored (and reused) Steps
def thing() : 
    print('Hello')
    print('Fun')
thing()
print('Zip')
thing()

'''
* There are two kinds of functions in Python
    * Built-in functions that are provided as part of Python -> print(), input(), type(), float(), int()...
    * Functions that we define ourselves then use
* We define a function using the "def" reserved word
* We call/invoke the function by using the function name, parentheses, and argument in an expression
'''

#Example of function - max() and min()
big = max('Hello world')
print(big)

tiny = min('Hello world')
print(tiny)