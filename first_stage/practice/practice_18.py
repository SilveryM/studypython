#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
Tn  =  0
Sn  =  [ ]
n  =  int ( raw_input ( ' n =  ' ) )
a  =  int ( raw_input ( ' a =  ' ) )
for   count   in   range ( n )
Tn  =  Tn  +  a
a  =  a  *  10
Sn . append ( Tn )
print   Tn
Sn  =  reduce ( lambda   x , y  :  x  +  y , Sn )
print   &quot; 计算和为： &quot; , Sn
'''

number = int(input('number:'))
count = int(input('count:'))

tmp_num = number

Tn = 0
for i in range(count):
    Tn = Tn + tmp_num
    tmp_num = tmp_num * 10 + number
    print(tmp_num, end=' ')

print(Tn)