user_input = '1-555-HOLIDAY'
phone_number = ' '

for character in user_input: #for the characters in user_input string
    if ('0' <= character <= '9') or (character == '-'):
        phone_number += character
        #prints phone_number = 1555
    elif ('a' <= character <= 'c') or ('A' <= character <= 'C'):
        #phone_number += '?'
        phone_number += '2' #letter A is 2.
        #FIXME: Add remaining elif branches
    elif ('d' <= character <= 'f') or ('D' <= character <= 'F'):
        phone_number += '3'
    elif('g' <= character <= 'i') or ('G' <= character <= 'i'):
        phone_number += '4'
    elif ('j' <= character <=  'l') or ('J' <= character <=  'L'):
        phone_number += '5'
    elif ('m' <= character <=  'o') or ('M' <= character <=  'O'):
        phone_number += '6'
    elif ('p' <= character <=  's') or ('P' <= character <=  'S'):
        phone_number += '7'
    elif ('t' <= character <=  'v') or ('T' <= character <=  'V'):
        phone_number += '8'
    elif ('w' <= character <=  'z') or ('W' <= character <=  'Z'):
        phone_number += '9'
    else:
        phone_number += '?'
print('Numbers only: %s' % phone_number)
