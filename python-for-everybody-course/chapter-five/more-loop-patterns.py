#Counting in a Loop
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('After', zork)

'''
* To count how many times we execute a loop, we introduce a counter variable thant starts at 0 and we add one to it each time through the loop.
'''

#Summing in a Loop
zork = 0 
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print('After', zork)

'''
* To add up a value we encounter in a loop, we introduce a sum variable that starts at 0 and we add the value to the sum each time through the loop.
'''

#Finding the Average in a Loop
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count,sum,value)
print('After', count, sum, sum / count)

'''
* An average just combines the counting and sum patterns and divides whe the loop is done.
'''

#Filtering in a Loop
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20 :
        print('Large number', value)
print('After')

'''
* We use an if statement in the loop to catch / filter the values we are looking for.
'''

#Search Using a Boolean Variable
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 : 
        found = True
    print(found, value)
print('After', found)

'''
* If we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for.
'''

#How to find the smallest value
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)

'''
* We still have a variable that is the smallest so far. The first time through the loop smallest is None, so we take the first value to be the smallest.
'''

# The "is" and "is not" Operators
'''
* Python has an is operator that can be used in logical expressions
* Implies "is the same as"
* Similar to, but stronger than ==
* is not also is a logical operator
For example 0 == 0.0 is return as "true" because it doesn't look a type. But if write 0 is 0.0 it returns "false" becase each one has a different type
'''