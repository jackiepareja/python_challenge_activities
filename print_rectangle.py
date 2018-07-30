num_rows = 2
num_cols = 3

for i in range(num_rows):
    print('*', end=' ')
    for j in range(num_cols - 1):
        i *= j
        print('*', end=' ')
    print(' ')
