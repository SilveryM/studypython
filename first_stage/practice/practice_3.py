#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
for   i   in   range ( 1 , 85 )
if   168  %  i  ==  0
j  =  168  /  i
if    i  &gt;  j   and   ( i  +  j )  %  2  ==  0   and   ( i  -  j )  %  2  ==  0
m  =  ( i  +  j )  /  2
n  =  ( i  -  j )  /  2
x  =  n  *  n  -  100
print ( x )
'''

#暴力破解
# i = 0
# while True:
#     m = i + 100
#     n = m + 168

#     if (m >= 0 and n >= 0):
#         m1 = m**0.5
#         n1 = n**0.5

#         if (m1 == int(m1) and n1 == int(n1)):
#             print(i)
#             # break

#     i += 1
# 暴力破解很难找到所有情况,比如上种就漏了-99

#正常解法
for i in range(1, int(168 / 2 + 1)):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(int(x))