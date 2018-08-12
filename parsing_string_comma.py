# 1. Prompt the user for a string that contains two strings separated by a comma.
input_string = input('Enter input string: \n')

# 4.1 Continue until the user enters q to quit.
while input_string != 'q':
    # 2.0 Report an error if the input string does not contain a comma.
    # Rationale: A while statement will keep asking the user to input a string if there is no comma in the input.
    while ',' not in input_string:
        print('Error: No comma in string.')
        # 2.1 Continue to prompt until a valid string is entered. Note: if the input contains a comma, then assume that the input also contains two strings
        input_string = input('Enter input string: \n')
    # Rationale: Since a while statement was used in the same nest, using if/elif will run an error unless it's a while statement.
    while ',' in input_string:
        # 3. Using string splitting, extract the two words from the input string and then remove any spaces. Output the two words.
        split_string = input_string.split(',')
        # The title built-in function transforms the first character of a string into an uppercase letter. This is important since we're dealing with names.
        # Regardless if the user enters a lower case first letter of a name, it will output an uppercase first letter.
        # The strip built in function strips the white spaces that is before and after the string variable.
        # If the strip function was used for the input_string variable, it will strip the white space before the first string, and after the second string.
        first_string = split_string[0].title().strip()
        second_string = split_string[1].title().strip()
        # The new .format in Python gives the placeholders an explicit positional index.
        print('First word: {first}\nSecond word:{second}'.format(first=first_string, second=second_string))
        # 4.0 Using a loop, extend the program to handle multiple lines of input.
        input_string = input('Enter input string: \n')
        break
    # This will break the infinite loop.

else:
    #This stops the program.
    exit()
