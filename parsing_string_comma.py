# 1. Prompt the user for a string that contains two strings separated by a comma.
input_string = input('Enter input string: \n')

if ',' not in input_string:
    print('Error: No comma in string.')
elif ',' in input_string:
    print(input_string)

# 2.0 Report an error if the input string does not contain a comma.

# 2.1 Continue to prompt until a valid string is entered. Note: if the input contains a comma, then assume that the input also contains two strings

# 3. Using string splitting, extract the two words from the input string and then remove any spaces. Output the two words.

# 4.0 Using a loop, extend the program to handle multiple lines of input.

# 4.1 Continue until the user enters q to quit.
