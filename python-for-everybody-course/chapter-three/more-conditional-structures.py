#Multi-way
x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('Large')
print('All done')

#No Else
x = 50
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
print('All done')

x = 6
if x < 2 :
    print('Below 2')
elif x < 20 :
    print('Below 20')
elif x < 10 :
    print('Below 10')
else :
    print('Something else')


#The try / except Structure
'''
* If the code in the try works - the except is skipped
* If the code in the try fails - it jumps to the except section
'''

astr = 'Hello Bob'
try :
    istr = int(astr)
except :
    istr = -1
print('First', istr)

astr = '123'
try : 
    istr = int(astr)
except :
    istr = -1
print('Second', istr)


#Sample try / except
rawstr = input('Enter a number:')
try :
    ival = int(rawstr)
except :
    ival = -1

if ival > 0 :
    print('Nice work')
else :
    print('Not a number')
