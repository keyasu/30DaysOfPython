from typing import AsyncGenerator


print('17_exception_handling')

""" 
异常处理
Python 使用try和except来优雅地处理错误。错误的优雅退出（或优雅处理）是一种简单的编程习惯用法 - 程序检测到严重的错误情况并因此以受控方式“优雅退出”。
    通常，作为优雅退出的一部分，程序会向终端或日志打印描述性错误消息，这使我们的应用程序更加健壮。
    异常的原因通常在程序本身之外。异常的一个例子可能是不正确的输入、错误的文件名、无法找到文件、IO 设备故障。
    
    优雅地处理错误可以防止我们的应用程序崩溃。

我们在上一节中介绍了不同的 Python错误类型。如果我们在我们的程序中使用try和except，那么它不会在这些块中引发错误

"""

# try:
#     print(10 + '4')
# except:
#     print('Something went wrong')

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born

#     print(f'You are {name}. And your age is {age}.')
# except:
#     print('Something went wrong')

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     age = 2019 - int(year_born)

#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')

# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')


# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1,2,3,4,5]
# print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'


# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1,2,3,4,5]
# print(sum_of_five_nums(*lst))  # 15
# print(sum_of_five_nums(*lst))

# numbers = range(2, 7)  # normal call with separate arguments
# print(list(numbers)) # [2, 3, 4, 5, 6]
# args = [2, 7]
# numbers = range(*args)  # call with arguments unpacked from a list
# print(numbers)      # [2, 3, 4, 5,6]


# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
# numbers = [1, 2, 3, 4, 5, 6, 7]
# one, *middle, last = numbers
# print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

""" def unpacking_person_info(name, country, city, age):
    str = f'{name} lives in {country}, {city}. He is {age} year old.'
    return str
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
 """

# def sum_all(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(sum_all(1, 2, 3))             # 6
# print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
#

# Packing Dictionaries

# def packing_person_info(**kwargs):
#     for key in kwargs:        
#         print(f"{key} = {kwargs[key]}")
#     return kwargs

# print(packing_person_info(name="Asabeneh",
#       country="Finland", city="Helsinki", age=250))

""" def packing_person_info(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs

print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250))
 """

# Spreading in Python
""" 
lst_one = [1, 2, 3]
lst_two = [4, 5, 6,7]
lst = [0, *list_one, *list_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)        ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
"""

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
countries = [*country_lst_one, *country_lst_two]

for index, i in enumerate(countries):
    # print('hi')
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')
 


# .有时我们想在循环时组合列表。请参阅下面的示例：
""" fruits = ['banana', 'orange', 'mango', 'lemon']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []

for f, v  in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
 """
