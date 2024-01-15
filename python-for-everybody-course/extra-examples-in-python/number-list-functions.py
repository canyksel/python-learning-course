#Example-1
def check_even_odd(number):
    if(number % 2 == 0):
        return "Even"
    else : 
        return "Odd"

user_input = input('Please enter a number:')
result = check_even_odd(int(user_input))
print(f"The number is {result}")

#Example-2

#Functions
def check_even_odd_in_list(arr) :
    count = 0
    if not arr:
        return None
    
    for number in numbers:
        count = count + 1
        if(number % 2 == 0):
            print("The {:0d}.number is even ->".format(count), number)
        else : 
            print("The {:0d}.number is odd ->".format(count), number)

def find_min_max_avg(arr) :
    if not arr:
        return None
    print('Minimum number in list: {:0d}'.format(min(arr)))
    print('Maximum number in list: {:0d}'.format(max(arr)))
    print('Minimum number in list: {:.2f}'.format(sum(arr) / len(arr)))

print('Please enter a number list: ')
is_finish = False
numbers = list()

while is_finish is False :
    user_input = input(f'Please enter the {len(numbers) + 1}. number ->')
    if user_input.isdigit() :
        numbers.append(int(user_input))
        print('You added {:0d}. elements'.format(len(numbers)))
        is_continue = input('You added {:0d} number into list! Will you continue to adding ? Y/N'.format(len(numbers)))
    else : 
        print('You did not enter a number. Please enter a number!')
        continue

    if is_continue.lower().startswith('y') :
        continue
    else :
        if len(numbers) < 2 :
            print('You must add at least two elements')
        else : is_finish = True

check_even_odd_in_list(numbers)
find_min_max_avg(numbers)


    