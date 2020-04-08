#输出指定格式的日期。 使用 datetime 模块
'''

'''

import datetime

print(datetime.date.today())
print(datetime.date.today().strftime('%d/%m/%Y'))

print(datetime.date(2020, 4, 7))
print(datetime.date(2020, 4, 7).strftime('%d/%m/%Y'))

day = datetime.date(2020, 4, 7)
print(day)
day = day + datetime.timedelta(days=1)
print(day)
day = day.replace(year=day.year + 1, month=1, day=1)
print(day)