#输入三个整数x,y,z，请把这三个数由小到大输出。
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
l  =  [ ]
for   i   in   range ( 3 )
x  =  int ( raw_input ( ' integer: \n ' ) )
l . append ( x )
l . sort ( )
print   l
'''

l = []
for i in range(0, 3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)
