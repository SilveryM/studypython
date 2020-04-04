#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''
#!/usr/bin/python 
# -*- coding: UTF-8 -*- 
a  =  int ( raw_input ( &quot; 请输入一个数字: \n &quot; ) ) 
x  =  str ( a ) 
flag  =  True 
for   i   in   range ( len ( x ) / 2 ) 
if   x [ i ]  !=  x [ - i  -  1 ] 
flag  =  False 
break 
if   flag 
print   &quot; %d 是一个回文数! &quot;  %  a 
else 
print   &quot; %d 不是一个回文数! &quot;  %  a 
'''