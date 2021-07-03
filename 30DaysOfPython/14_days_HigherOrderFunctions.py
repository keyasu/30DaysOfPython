print('days - 14 - Higher Order Functions')
""" 
在 Python 中，函数被视为一等公民，允许您对函数执行以下操作：

    一个函数可以接受一个或多个函数作为参数
    一个函数可以作为另一个函数的结果返回
    一个函数可以修改
    一个函数可以赋值给一个变量

"""

""" 
在本节中，我们将介绍：

    将函数作为参数处理
    将函数作为其他函数的返回值返回
    使用 python 闭包和装饰器

"""
# 作为参数的函数

""" def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, *args):  # function as a parameter
    summation = f(*args)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
 """

""" def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

# 从上面的例子可以看出，高阶函数根据传递的参数返回不同的函数

"""
# Python 允许嵌套函数访问封闭函数的外部作用域。这被称为闭包。
# 让我们看看闭包在 Python 中是如何工作的。
# 在 Python 中，闭包是通过在另一个封装函数中嵌套一个函数然后返回内部函数来创建的。
# 请参阅下面的示例。

""" def add_ten():
    ten = 10

    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
 """

#  Python 装饰器
# 装饰器是 Python 中的一种设计模式，它允许用户在不修改其结构的情况下向现有对象添加新功能。
# 装饰器通常在定义要装饰的函数之前调用。

# Normal function
# def greeting():
#     return 'Welcome to Python'
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# g = uppercase_decorator(greeting)
# print(g())          # WELCOME TO PYTHON

## Lets implement the example above with a decorator

''''这个装饰器函数是一个 以函数为参数的 高阶函数'''

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# @uppercase_decorator
# def greeting():
#     return 'Welcome to Python'
# print(greeting())   # WELCOME TO PYTHON

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# @uppercase_decorator
# def  greeting():
#     return 'Welcome to Python'

# print(greeting())
    

# 将多个装饰器应用于单个函数

'''这些装饰器函数都是 以函数为参数的 高阶函数'''

""" def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()

    return wrapper
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator

def greeting():
    return 'Welcome to Python'

print(greeting())
"""
# 在装饰器函数中接受参数
# 大多数时候我们需要我们的函数接受参数，所以我们可能需要定义一个接受参数的装饰器。
""" 
def decorator_with_parameterts(function):
    def wrapper_accepting_parameters(para1, para2, para3, para4):
        function(para1, para2, para3, para4)
        print('I live in {}'.format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameterts
def print_full_name(first_name,last_name, country, countryy):
    print('I an {} {}'.format(first_name, last_name, country, countryy))

print_full_name('A', 'B', 'C')

 """
# 内置高阶函数
# 我们在本部分中介绍的一些内置高阶函数是map()、filter和reduce。
# Lambda 函数可以作为参数传递，而 lambda 函数的最佳用例是 map、filter 和 reduce 等函数。

# numbers = [1, 2, 3, 4, 5]
# def square(x):
#     return x ** 2
# numbers_squared = map(square, numbers)
# print(list(numbers_squared))
# numbers_squared = map(lambda x : x ** 2, numbers)
# print(list(numbers_squared))

# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

# def change_to_upper(name):
#     return name.upper()

# names_upper_cased = map(change_to_upper, names)
# print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# # Lets apply it with a lambda function
# names_upper_cased = map(lambda name: name.upper(), names)
# print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']


# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham'] 
# def change_to_upper(name):
#     return name.upper()

# name_upper_cased = map(change_to_upper, names)
# print(list(name_upper_cased))

# 实际上 map 所做的是迭代一个列表。例如，它将名称更改为大写并返回一个新列表。

# Python - 过滤功能
# filter() 函数调用指定的函数，该函数为指定的可迭代（列表）的每个项目返回布尔值。它过滤满足过滤条件的项目。
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

# even_numbers = filter(is_even, numbers)
# print(list(even_numbers))       # [2, 4]
# numbers = [1, 2, 3, 4, 5]  # iterable

# def is_odd(num):
#     if num % 2 != 0:
#         return True
#     return False

# odd_numbers = filter(is_odd, numbers)
# print(list(odd_numbers))       # [1, 3, 5]

# Python - 减少函数
# 在减少（）函数的fucntools模块里定义，我们应该从这个模块导入。与 map 和 filter 一样，它需要两个参数，一个函数和一个可迭代对象。但是，它不会返回另一个可迭代对象，而是返回一个值。 示例：1
numbers_str = ['1', '2', '3', '4', '5']  # iterable
# def add_two_nums(x, y):
#     return int(x) + int(y)

# total = reduce(add_two_nums, numbers_str)
# print(total)    # 15

from functools import reduce
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)









