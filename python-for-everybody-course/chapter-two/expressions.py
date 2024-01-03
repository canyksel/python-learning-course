#Numeric Expressions
'''
+ -> Addition
- -> Substraction
* -> Multiplication
/ -> Division
** -> Power
% -> Remainder
'''

xx = 2
xx = xx + 2
print(xx)

yy = 440 * 12
print(yy)

zz = yy / 1000
print(zz)

jj = 23
kk = jj % 5
print(kk)

print(4 ** 3)

#Operator Precendence Rules
'''
* Parentheses are always respected
* Exponentiatiton( raise to a power)
* Multiplication, Division and Remainder
* Addition and Substraction
* Left to righ

1-)Paranthesis
2-)Power
3-)Multiplication
4-)Addition
5-)Left to right
'''

x = 1 + 2 ** 3 / 4 * 5
print(x)

#type
eee = 'hello' + 'there'
print(type(eee)) #<class 'str'>
print(type('hello')) #<class 'str>
print(type(1)) #<class 'int'>

xx = 1
print(type(xx)) #<class 'int'>
temp = 98.6
print(type(temp)) #<class 'float'>

#Type Conversions
print(float(99) + 100)
i = 42
type(i)
f = float(i)
print(f)
type(f)

#Integer Division
'''Integer division produces a floating point result'''

print(10 / 2)
print(9 / 2)
print(99 / 100)
print(10.0 / 2.0)
print(99.0 / 100.0)

#String Conversions
'''
* We can use int() and float() to convert between string and integers
* We will get an error if the string does not contain numeric characters
'''

#User Input
'''
* We can instruct Python to pause and read data from the user using the input() function
* The input() function returns a string
'''

name = input('Who are you? ')
print('Welcome', name)