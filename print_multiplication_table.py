mult_table = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]

bar = '| '
for row, num in enumerate(mult_table):
    for cell, num in enumerate(num):
        print(num, end=' ')
        if cell == len(mult_table)-1:
            print()

        else:
            print(bar, end='')

