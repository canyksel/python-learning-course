#Fibonacci Series
def calculate_fibonacci_method_one(n):
    fibonacci_series = [0,1]

    for i in range(2,n):
        next_item = fibonacci_series[i-1] + fibonacci_series[i-2]
        fibonacci_series.append(next_item)

    return fibonacci_series[:n]

def calculate_fibonacci_method_two(n):
    fibo_series = []
    
    for i in range(n):
        if i < 1:
            fibo_series.append(0)
            fibo_series.append(1)
        else :
            next_item = fibo_series[i] + fibo_series[i-1]
            fibo_series.append(next_item)
    return fibo_series[:n]

user_input = input('Please enter length of the series ->')
result_one = calculate_fibonacci_method_one(int(user_input))
result_two = calculate_fibonacci_method_two(int(user_input))

print(result_one)
print(result_two)

#Bubble Sorting
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

user_input_list = []

while True :
    user_input = input('Please enter length of the sequence ->')
    if user_input.isdigit() :
        for i in range(int(user_input)):
            list_item = input(f'Please enter the {i+1}. element'.format(i))
            user_input_list.append(list_item)
        break
    else:
        print('Please enter a valid input!')

bubble_sort(user_input_list)
print('Sorted list ->', user_input_list)

#Factorial
#Method-1:
def calculate_factorial(n):
    sum = 1
    for i in range(n) :
        sum += sum * i
    return sum
#Method-2:
def calculate_factorial2(n):
    arr = []
    sum = 1
    for i in range(n):
        arr.append(i)
    print(arr)
    for j in arr :
        sum += sum * j
    return sum


user_input = input('Please enter the value ->')

first_result_factorial = calculate_factorial(int(user_input))
second_result_factorial = calculate_factorial2(int(user_input))

print(first_result_factorial)
print(second_result_factorial)