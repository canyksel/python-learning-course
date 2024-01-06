#Slicing Strings
'''
* We can also look at any continious section of a string using a colon operator
* The second number is one beyond the end of the slice - "up to but not including"(this is important)
* If the second number is beyond the end of the string, it stops at the end
* If we leave off the first number or the last number of the slice, it is assumed to be the beginning or end of the string respectively
'''

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

print(s[:2])
print(s[8:])
print(s[:])

#String Concatenation
'''
* When the + operator is applied to strings, it means "concatenation"
* print(str1, str2) //Automatically added space
'''

a = 'Hello'
b  = a + 'There'
print(b)

c = a + ' ' + 'There'
print(c)

#Using in as logical Operator
'''
* The in keyword can also be used to check to see if one string is "in" another string
* The in expression is a logical expression that returns True or false and can be used an if statement
'''

fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit :
    print('Found it!')


#Extra example - The order in which the character was first found

entered_word = input('Please enter a word:')
entered_key = input('Please enter the character or number you want to be found:')

if len(entered_key) > 1 :
    print('Please enter a one character or number!')
    entered_key = ''
    entered_key = input('Please re-enter the character or number you want to be found:')
else :
    index = 0
    is_find = False

    while not is_find and index < len(entered_word):
        if entered_word[index] == entered_key:
            is_find = True
            print(f"Character: '{entered_key}' founded at {index + 1}. order.")
        else : 
            index = index +1

    if not is_find:
        print('Character not found')

#String Comparison
word = input('Word:')
if word == 'banana' :
    print('All right, bananas.')

if word < 'banana' :
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana' :
    print('Your word,' + word + ', comes after banana.')
else :
    print('All right, bananas.')

'''
* Python has a number of string functions which are in the string library
* These functions are already built into every string - we invoke them by appending the function to the string variable
* These functions do not modify the original string, instead they return a new string that has been altered
'''

greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

stuff = 'Hello world'
type(stuff)
dir(stuff)