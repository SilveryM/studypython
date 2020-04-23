#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

a = [2, 3]
b = [1, 2]

for i in range(18):
    a.append(a[-2] + a[-1])
    b.append(b[-2] + b[-1])

c = 0
for i in range(len(a)):
    c = c + a[i] / b[i]

print(c)