#打印出如下图案（菱形）:
size = int(input('size:'))
num = size / 2
for i in range(1, size):
    if i <= num:
        tip = i
    else:
        tip = size - i

    for j in range(1, size):
        if j <= num - tip or j >= num + tip:
            print(' ', end='')
        else:
            print('*', end='')
    print('')
print('')