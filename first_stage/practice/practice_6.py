#斐波那契数列。
#斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
'''

'''


def fib(n):
    f = [0, 1]
    for i in range(n - 1):
        f.append(f[-1] + f[-2])
    return f


print(fib(int(input('number:\n'))))