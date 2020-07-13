#利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
def output(s, l):
    if l == 0:
        return
    print(s[l - 1], end='')
    return output(s, l - 1)

if __name__ == "__main__":
    s = input('input words:')
    output(s, len(s))
    print('')