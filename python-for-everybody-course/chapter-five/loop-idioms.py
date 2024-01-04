#What is the Largest Number?
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

#Extra: What is the largest and lowest number?
largest_num= float('-inf')
lowest_num = float('inf')

for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_num:
        largest_num = the_num
    elif the_num < lowest_num:
        lowest_num = the_num

print('Largest', largest_num)
print('Lowest', lowest_num)


#Extra: Alternative of the finding largest and lowest number:
numbers = [9, 41, 12, 3, 74, 15]
lowest = min(numbers)
largest = max(numbers)

print('Largest', largest)
print('Lowest', lowest)

