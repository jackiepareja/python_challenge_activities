#Prompt the user for a string that contains two strings separated by a comma.

input_string = input('Enter input string: ')

#Report an error if the input string does not contain a comma. Continue to prompt until a valid
#string is entered.

#Using string splitting, extract the two words from the input string
#and then remove any spaces. Output the two words.
while input_string != 'q':
    if ',' not in input_string:
        print("Error: No comma in string.")
        input_string = input('Enter input string: \n')
        
    elif ',' in input_string:
        input_string = input_string.split(',')
        first_word = input_string[0]
        second_word = input_string[1]

        print('First word: {first}\nSecond word: {second}\n\n'.format(first = first_word, second = second_word))
else:
    print("Quit")







    
    
    



