#输入某年某月某日，判断这一天是这一年的第几天？
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
year  =  int ( raw_input ( ' year: \n ' ) )
month  =  int ( raw_input ( ' month: \n ' ) )
day  =  int ( raw_input ( ' day: \n ' ) )
months  =  ( 0 ,31 , 59 , 90 , 120 , 151 , 181 , 212 , 243 , 273 , 304 , 334 )
if   0  &lt;  month  &lt;=  12
sum  =  months [ month  -  1 ]
else
print   ' data error '
sum  +=  day
leap  =  0
if   ( year  %  400  ==  0 )   or   ( ( year  %  4  ==  0 )   and   ( year  %  100  !=  0 ) )
leap  =  1
if   ( leap  ==  1 )   and   ( month  &gt;  2 )
sum  +=  1
print   ' it is the %dth day. '  %  sum
'''

if __name__ == "__main__":
    while True:
        year = int(input('year:\n'))
        month = int(input('month:\n'))
        day = int(input('day:\n'))

        all_day = day
        months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

        for i in range(-1, month - 1):
            if i >= 0 and i < len(months):
                all_day += months[i]

        if ((year % 400 == 0) or ((year % 4 == 0) and
                                  (year % 100 != 0))) and (month > 2):
            all_day + 1

        print(all_day)