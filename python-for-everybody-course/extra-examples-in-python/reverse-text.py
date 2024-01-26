def count_words(arr) :
    return print('Number of words:', len(arr))

def reverse_text(text) :
    split_text = text.split()

    count_words(split_text)

    text_list = list()
    for item in split_text :
        text_list.append(item[::-1])

      
    return ' '.join(text_list)

user_input = input('Enter text -> ')
result = reverse_text(user_input)
print('Reversed version -> ', result)