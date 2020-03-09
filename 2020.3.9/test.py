# fibs = [0, 1]

# for i in range(30):
#     fibs.append(fibs[-2] + fibs[-1])

# print(fibs)


def fibs(num):
    result = [0, 1]
    for i in range(num):
        result.append(result[-2] + result[-1])
    return result


if __name__ == "__main__":
    num = int(input())
    result = fibs(num)
    print(result)