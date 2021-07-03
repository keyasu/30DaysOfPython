# import _12_days_mymodule
# print('days - 12 - modules')
# print(_12_days_mymodule.generate_full_name('A', 'B'))

# 模块是包含一组代码或一组可以包含在应用程序中的功能的文件。一个模块可以是一个包含单个变量的文件，也可以是一个函数，一个大的代码库。

# 为了创建一个模块，我们在 python 脚本中编写代码并将其保存为 .py 文件。在项目文件夹中创建一个名为 mymodule.py 的文件。让我们在这个文件中写一些代码。
# main.py file
# from _12_days_mymodule import generate_full_name, sum_two_nums, person, gravity
# print(generate_full_name('Asabneh','Yetay'))
# print(sum_two_nums(1,9))
# mass = 100;
# weight = mass * gravity
# print(weight)
# print(person['firstname'])

# # main.py file
# from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
# print(fullname('Asabneh','Yetayeh'))
# print(total(1,9))
# mass = 100;
# weight = mass * g
# print(weight)
# print(p)
# print(p['firstname'])
# from _12_days_mymodule import generate_full_name as fullName
# print(fullName('A', 'B'))

import math, os, datetime, sys, random, statistics, collections, json, re

# print(os.getcwd())
# print(sys.platform)
# os.mkdir('directory_name1')
# os.rmdir('directory_name')

# # import the module
# import os
# # Creating a directory
# os.mkdir('directory_name')
# # Changing the current directory
# os.chdir('./directory_name')
# # Getting current working directory
# os.getcwd()
# # Removing directory
# os.rmdir()

#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
# print('args:first={}, seconds={}'.format(sys.argv[1], sys.argv[3], sys.argv[2]))
# print('args={}'.format(sys.argv))


# # to exit sys
# # sys.exit()
# # To know the largest integer variable it takes
# print(sys.maxsize)
# # To know environment path
# print(sys.path)
# # To know the version of python you are using
# print(sys.version)

# 统计模块提供数值数据的数理统计功能。此模块中定义的流行统计函数：mean、median、mode、stdev等。

""" from statistics import * # importing all the statistics modules
# ages = [20,20,24,24,25,22,26,20,23,22,26]
# print(mean(ages))       # ~22.9
# print(median(ages))     # 23
# print(mode(ages))       # 20
# print(stdev(ages))      # ~2.3
ages = [20,20,24,24,25,22,26,20,23,22,26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))
"""

import math
# print(math.pi)           # 3.141592653589793, pi constant
# print(math.sqrt(2))      # 1.4142135623730951, square root
# print(math.pow(2, 3))    # 8.0, exponential function
# print(math.floor(9.81))  # 9, rounding to the lowest
# print(math.ceil(9.81))   # 10, rounding to the highest
# print(math.log10(100))   # 2, logarithim with 10 as base

# 现在，我们已经导入了 math 模块，其中包含许多可以帮助我们进行数学计算的功能。
# 要检查模块具有哪些功能，您可以使用help(math)或dir(math)。
# 这将显示模块中的可用功能。
# 如果我们只想从模块中导入一个特定的函数，我们按如下方式导入它：


# import string
# print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)        # 0123456789
# print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# from random import random, randint
# print(random())   # 不带任何参数；它返回一个 0 到 0.9999 之间的值
# print(randint(5, 20.1)) # 它返回一个 5 到 20 之间的随机整数
from random import random, randint
print(random())
print(randint(5, 30))