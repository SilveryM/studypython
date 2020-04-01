#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
#!/usr/bin/python 
# -*- coding: UTF-8 -*- 
x  =  int ( raw_input ( &quot; 请输入一个数: \n &quot; ) ) 
a  =  x  /  10000 
b  =  x  %  10000  /  1000 
c  =  x  %  1000  /  100 
d  =  x  %  100  /  10 
e  =  x  %  10 
if   a  !=  0 
print   &quot; 5 位数： &quot; , e , d , c , b , a 
elif   b  !=  0 
print   &quot; 4 位数： &quot; , e , d , c , b 
elif   c  !=  0 
print   &quot; 3 位数： &quot; , e , d , c 
elif   d  !=  0 
print   &quot; 2 位数： &quot; , e , d 
else 
print   &quot; 1 位数： &quot; , e 
'''