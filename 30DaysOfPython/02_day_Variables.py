"""
学习的链接
https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md

变量 - 内置函数

"""

"""
变量将数据存储在计算机内存中。
推荐在许多编程语言中使用助记变量。
变量是指存储数据的内存地址。
命名时不允许以数字开头、特殊字符、连字符。
变量可以有一个短名称（如 x、y、z），但强烈建议使用更具描述性的名称（名字、姓氏、年龄、国家/地区）。
Python 变量名规则

    变量名必须以字母或下划线字符开头
    变量名不能以数字开头
    变量名称只能包含字母数字字符和下划线（Az、0-9 和 _ ）
    变量名区分大小写（firstname、Firstname、FirstName 和 FIRSTNAME 是不同的变量）

有效的变量名

"""
# Variables in Python
"""
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }


print('Hello, World!')
print('Hello',',', 'World','!') # it can take multiple arguments
print(len('Hello, World!')) # it takes only one argument

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
"""

# first_name = input('What is your name: ')
# age = input('How old are you? ')

# print(first_name)
# print(age)
"""
first_name = input('What is your name:')
age = input('How old are you?')

print(first_name)

print(age)

"""
# Different python data types
# Let's declare variables with various data types
"""
first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city = 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2,3,4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set
"""


# int to float

num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int

gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int
num_str = "10.6"
print(num_str)

print('num_int111', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)
print(first_name)                    # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
