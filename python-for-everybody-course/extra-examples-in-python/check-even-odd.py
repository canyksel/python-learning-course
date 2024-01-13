def check_even_odd(number):
    if(number % 2 == 0):
        return "Even"
    else : 
        return "Odd"

user_input = input('Please enter a number:')
result = check_even_odd(int(user_input))
print(f"The number is {result}")