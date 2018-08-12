# Best Practice: Used lowercase letters and an underscore in between the variables for specificity.
# Best Practice: Used single quotes for shorter strings (and double quotes for longer strings), because there is a
# continued: higher occurrence of apostrophies that maybe misrepresented as string quotations. It also improves
# continued 2: readability.
input_string = input('Enter input string: \n')

# A while loop is used so that the codeblock will keep executing as long as the user doesn't type 'q'.
while input_string != 'q':
    # Rationale: A while statement will keep asking the user to input a string if there is no comma in the input. An if
    # continued: statement will only execute the codeblock once if true.
    # Rationale: Two while loops are used and written on the same branch so that the code block will switch over and
    # Cont: execute as long as the statement is true.
    while ',' not in input_string:
        print('Error: No comma in string.')
        # Rationale: Under the while statement, the user will be prompted until there is a ',' in their string.
        input_string = input('Enter input string: \n')
    # Rationale: An else branch will not have enough clarify to why this codeblock should execute.
    while ',' in input_string:
        # Rationale: The split built in function splits a string by a specific item.
        # continued: The item is the ',', so it was detrimental that it a while statement asks the user if the comma is
        # continue 2: already there in the first place.
        # Best Practice: Appended the python keywords to differentiate from their functions.
        split_string = input_string.split(',')
        # Rationale: The title built-in function transforms the first character of a string into an uppercase letter.
        # continued: This is important since we're dealing with names. Regardless if the user enters a lower case first
        # continued 2: letter of a name, it will output an uppercase first letter.
        # Rationale: The strip built in function strips the white spaces that is before and after the string variable.
        # continued: If the strip function was used for the input_string variable, it will strip the white space before
        # continued 2: the first string, and after the second string.
        # Rationale: The split and stripped individual strings are stored in individual variables to be printed and
        # continued: formatted.
        first_string = split_string[0].title().strip()
        second_string = split_string[1].title().strip()
        # Best Practices: The new .format in Python gives the placeholders an explicit positional index.
        print('First word: {first}\nSecond word:{second}'.format(first=first_string, second=second_string))
        # Rationale: The user is asked multiple inputs as long as the user doesn't type 'q' to quit.
        # If there is no comma in this string, the program will leave the loop and go back to the previous while loop.
        input_string = input('Enter input string: \n')
else:
    # Rationale: This stops the program.
    exit()
