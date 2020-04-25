#求1+2!+3!+...+20!的和。


def Factorial(num):
    final_num = 1
    for i in range(1, num + 1):
        final_num = final_num * i
    return final_num


if __name__ == "__main__":
    num = 0
    for i in range(1, 21):
        num = num + Factorial(i)
    print(num)