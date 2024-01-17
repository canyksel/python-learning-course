student_size = 0
student_list = dict()
counter = 0
is_finished = False
average = 0

def get_student_size(prompt) : 
    while True :
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) != 0 and not user_input.startswith('0'):
            print('Entered class size is:', user_input)
            return int(user_input)
        else :
            print('Please enter a valid number!')

def calculate_average(sum, len) :
        return "{:.2f}".format(sum / len)

def calculate_standart_deviation(data) : 
    n = len(data)
    if n < 2 :
        return "Not enough elements to calculate standart deviation"
    
    mean = sum(data) / n
    sum_squared_diff = sum((x - mean) ** 2 for x in data)
    std_dev = (sum_squared_diff / n) ** 0.5

    return "{:.3}".format(std_dev)

def calculate_grades(point) :
    if point <= 39 :
        return 'FF'
    elif point > 39 and point <= 49 :
        return 'FD'
    elif point > 49 and point <= 54 :
        return 'DD'
    elif point > 54 and point <= 59 :
        return 'DC'
    elif point > 59 and point <= 69 :
        return 'CC'
    elif point > 69 and point <= 79 :
        return 'CB'
    elif point > 79 and point <= 84 :
        return 'BB'
    elif point > 84 and point <= 89 :
        return 'BA'
    elif point > 89 and point <= 100 :
        return 'AA'
    
print('Welcome to Calculate Bell Curve Program !')
student_size = get_student_size('Please enter number of the student -> ')

while is_finished is False :
    if counter < student_size :
        counter = counter + 1
        key = input('Please enter a name of {:0d}. student -> '.format(counter))
        value = int(input('Please enter an exam grade -> '))
        student_list[key] = value
    else :
        is_finished = True

average = calculate_average(sum(student_list.values()), len(student_list))
standart_deviation = calculate_standart_deviation(student_list.values())

print('Standart deviation is ->',standart_deviation)
print('Average of exam grades is ->', average)

result_list = [(key, calculate_grades(value)) for key, value in student_list.items()]

print('Results with grades: ', result_list)
