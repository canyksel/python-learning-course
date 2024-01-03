'''
* We create a new function using the def keyword followed by optional parameters in parentheses
* We indent the body of the function
* This defines the function but does not execute the body of the function
'''

x = 5
print('Hello')
def print_lyrics() :
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
print_lyrics()
x = x + 2
print(x)

'''
#Arguments
* An argument is a value we pass into the function as its input when we call the function
* We use arguments so we can direct the function to do different kinds of work when we call it at different times
* We put the arguments in parentheses after the name of the function
'''

#Parameters
''''
* A parameter is a variable which we use in the function definition. It is a "handle" that allows the code in the function to access the arguments for a particular function invocation.
'''

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('es')
greet('fr')

#Return Values
'''
* Often a function will take its arguments, do some computation, and return a value to be used as the value of the function call in the calling expression. The return keyword is used for this.
'''

def greet():
    return "Hello"

print(greet(), "Glenn")
print(greet(), "Sally")

'''
* A fruitful function is one that produces a result (or return value)
* The return statement ends the function execution and "sends back" the result of the function
'''

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), "Glenn")
print(greet('es'), "Sally")
print(greet('fr'), "Michael")

#Multiple Parameters / Arguments
'''
* We can define more than one parameter in the function
* We simply add more arguments when we call the function
* We match the number and order of arguments and parameters
'''

def addtwo(a,b):
    added = a + b
    return added

x = addtwo(3,5)
print(x)

#Void (non-fruit) Functions
'''
* When a function does not return a value, we call it a "void" function
* Functions that return values are "fruitful" functions
* Void functions are "not fruitful"
'''

