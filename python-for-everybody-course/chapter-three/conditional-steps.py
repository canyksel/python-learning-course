#Example
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finish')

#Comparison Operators
'''
<       = Less than
<=      = Less than or Equal to
==      = Equal to
>=      = Greater than or Equal to
>       = Greater than
!=      = Not equal

*Remember: '=' is used for assignment
*Boolean expressions produce a Yes or No result (True / False)
'''

x = 5
if x == 5 :
    print('Equals 5')
if x > 4 :
    print('Greater than 4')
if x >= 5 :
    print('Greater than or Equals 5')
if x < 6 :
    print('Less than 6')
if x <= 5 :
    print('Less than or Equals 5')
if x != 6 :
    print('Not equal 6')

#Nested Decisions
x = 42
if x > 1 :
    print('More than one')
    if(x < 100) :
        print('Less than 100')
print('All done')

#Two-way Decisions
x = 4
if x > 2 :
    print('Bigger')
else : 
    print('Smaller')
print('All done')