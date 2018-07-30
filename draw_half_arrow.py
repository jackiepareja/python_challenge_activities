print ('Enter arrow base height: ')
arrow_base_height = int(input())
   
print ('Enter arrow base width: ')
arrow_base_width = int(input())
   
print ('Enter arrow head width: ')
arrow_head_width = int(input())

while arrow_head_width <= arrow_base_width:
    print('Enter arrow head width: ')
    arrow_head_width = int(input())
    continue
else:
    for i in range(arrow_base_height):
        print('*', end='')
        for j in range(arrow_base_width - 1):
            i *= j
            print('*', end='')
        print('')
    for k in range(arrow_head_width):
        print('*', end='')
        for l in range(arrow_head_width - 1):
            k *= l
            print('*', end='')
        arrow_head_width -= 1
        print('')
