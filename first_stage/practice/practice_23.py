#打印出如下图案（菱形）:
import math
size = 10
num = size / 2
for i in range(1, size):
    if i <= size / 2:
        for j in range(1, size):
            if j <= num - i or j >= num + i:
                print(' ', end='')
            else:
                print('*', end='')
    else:
        for j in range(1, size):
            if j <= num - (size - i) or j >= num + (size - i):
                print(' ', end='')
            else:
                print('*', end='')
    print('')
print('')