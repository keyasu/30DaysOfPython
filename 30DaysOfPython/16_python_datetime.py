print('days-16_python_datetime')

""" 
Python日期时间
    获取日期时间信息
    使用strftime格式化日期输出
    使用strptime 将字符串转换为时间
    使用日期时间中的日期
    代表时间的时间对象
    两个时间点之间的差异使用
    使用timedelata 的两个时间点之间的差异

"""
# import datetime
# print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
# import datetime
# print(dir(datetime))

# 使用 dir 或 help 内置命令可以知道某个模块中的可用功能。
# 如您所见，在 datetime 模块中有许多函数，但我们将重点介绍date、datetime、time和timedelta。让我们一一看看。

# from datetime import datetime
# now = datetime.now()
# print(now)                      # 2019-12-04 23:34:46.549883
# day = now.day                   # 4
# month = now.month               # 12
# year = now.year                 # 2019
# hour = now.hour                 # 23
# minute = now.minute             # 38
# second = now.second
# timestamp = now.timestamp()
# print(day, month, year, hour, minute)
# print('timestamp', timestamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}')  # 4/12/2019, 23:38

""" from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(year, month, day)
print(hour, minute, second)
print(timestamp)

print(f'{year}/{month}/{day}, {hour}:{minute}:{second}')

 """

from datetime import date, datetime, time, timedelta
# current date and time
# now = datetime.now()
# t = now.strftime("%H:%M:%S")
# print("time:", t)
# time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print("time one:", time_one)
# time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("time two:", time_two)
# now = datetime.now()
# t = now.strftime("%H:%M:%S")
# print('time:', t)

# time_one = now.strftime("%Y/%m/%d, %H:%M:%S")
# print(time_one)

# time_two = now.strftime("%Y/%m/%d, %H:%M:%S")
# print("time two:", time_two)

# from datetime import datetime
# date_string = "5 December, 2019"
# print("date_string =", date_string)
# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object =", date_object)

# from datetime import date
# d = date(2020, 1, 1)
# print(d)
# print('Current date:', d.today())    # 2019-12-05
# # date object of today's date
# today = date.today()
# print("Current year:", today.year)   # 2019
# print("Current month:", today.month) # 12
# print("Current day:", today.day)     # 5

from datetime import time
# time(hour = 0, minute = 0, second = 0)
# a = time()
# print("a =", a)
# # time(hour, minute and second)
# b = time(10, 30, 50)
# print("b =", b)
# # time(hour, minute and second)
# c = time(hour=10, minute=30, second=50)
# print("c =", c)
# # time(hour, minute, second, microsecond)
# d = time(10, 30, 50, 200555)
# print("d =", d)

# today = date(year=2019, month=12, day=5)
# new_year = date(year=2020, month=1, day=1)
# time_left_for_newyear = new_year - today
# # Time left for new year:  27 days, 0:00:00
# print('Time left for new year: ', time_left_for_newyear)

# t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
# t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
# diff = t2 - t1
# print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00

# 使用timedelata 的两个时间点之间的差异
# from datetime import timedelta
# t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
# t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
# t3 = t1 - t2
# print("t3 =", t3)
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)

print('时间差:', t2-t1)

