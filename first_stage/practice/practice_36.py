#求100之内的素数。
'''
#!/usr/bin/python 
# -*- coding: UTF-8 -*- 
# 输出指定范围内的素数 
# 用户输入数据 
lower  =  int ( input ( &quot; 输入区间最小值:  &quot; ) ) 
upper  =  int ( input ( &quot; 输入区间最大值:  &quot; ) ) 
for   num   in   range ( lower , upper  +  1 ) 
# 素数大于 1 
if   num  &gt;  1 
for   i   in   range ( 2 , num ) 
if   ( num  %  i )  ==  0 
break 
else 
print ( num ) 
'''