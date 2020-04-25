#利用递归方法求5!。


def fact(num):
    sum = 0
    if (num == 0):
        sum = 1
    else:
        sum = num * fact(num - 1)
    return sum


print(fact(5))