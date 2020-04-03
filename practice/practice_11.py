#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
f1  =  1
f2  =  1
for   i   in   range ( 1 , 22 )
print   ' %12ld %12ld '  %  ( f1 , f2 )
if   ( i  %  3 )  ==  0
print   ' '
f1  =  f1  +  f2
f2  =  f1  +  f2
'''


class Rabit(object):
    def __init__(self, month):
        self._birth_month = month

    def Breed(self, month):
        if (month - self._birth_month >= 3):
            return Rabit(month)
        return None


if __name__ == "__main__":
    rabit_list = []
    cur_month = 0
    rabit_list.append(Rabit(cur_month))

    all_month = int(input('months:')) + 1
    while cur_month < all_month:
        for rabit in rabit_list:
            new_rabit = rabit.Breed(cur_month)
            if new_rabit != None:
                rabit_list.append(new_rabit)

        print('month:%d, rabit_num:%d' % (cur_month, len(rabit_list)))
        cur_month += 1
