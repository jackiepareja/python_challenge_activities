input_string = input('Enter input string: ')

if input_string != 'q':
    if ',' in input_string:
        input_string = input_string.split(',')
        first_word = input_string[0]
        second_word = input_string[1]
        print('First word: {first}\nSecond word: {second}\n\n'.format(first = first_word, second = second_word))
      
    elif ',' not in input_string:
        print('Error: No comma in string.')
        input_string = input('Enter input string: \n')
        
else:
    print('quit')
