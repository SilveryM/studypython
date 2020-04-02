#输出 9*9 乘法口诀表。
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
for   i   in   range ( 1 ,  10 )
print
for   j   in   range ( 1 ,  i + 1 )
print   &quot; %d*%d=%d &quot;  %  ( i ,  j ,  i * j ) ,
'''

for i in range(1, 10):
    for j in range(1, 10):
        print('%d*%d=%d' % (i, j, i * j))