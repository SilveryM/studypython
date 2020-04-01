#找到年龄最大的人，并输出。请找出程序中有什么问题。
'''
#!/usr/bin/python 
# -*- coding: UTF-8 -*- 
if   __name__  ==  ' __main__ ' 
person  = { &quot; li &quot; : 18 , &quot; wang &quot; : 50 , &quot; zhang &quot; : 20 , &quot; sun &quot; : 22 
m  =  ' li ' 
for   key   in   person . keys ( ) 
if   person [ m ]  &lt;  person [ key ] 
m  =  key 
print   ' %s,%d '  %  ( m , person [ m ] ) 
'''