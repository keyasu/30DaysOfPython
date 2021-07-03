print('04-days-string')

""" 
文本是一种字符串数据类型。任何写成文本的数据类型都是字符串。单引号或双引号下的任何数据都是字符串。有不同的字符串方法和内置函数来处理字符串数据类型。要检查字符串的长度，请使用 len() 方法。
 """

""" 
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
 """

# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''
# print(multiline_string)
# # Another way of doing the same thing
# multiline_string = """I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python."""
# print(multiline_string)

""" first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16
 """

""" 
字符串中的转义序列
在 python 和其他编程语言中 \ 后跟一个字符。让我们看看最常见的转义字符：

\n: 换行
\t: Tab 表示（8 个空格）
\\: 反斜杠
\': 单引号 (')
\"：双引号 (")

 """


""" print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5') 
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"')


 """

""" 
旧式字符串格式（% 运算符）
在python中有很多格式化字符串的方法。在本节中，我们将介绍其中的一些。“%”运算符用于格式化包含在“元组”（固定大小的列表）中的一组变量，以及一个格式字符串，其中包含普通文本和“参数说明符”，特殊符号如“%s” 、“%d”、“%f”、“%.f”。

%s - 字符串（或任何具有字符串表示的对象，如数字）
%d - 整数
%f - 浮点数
%.f - 固定精度的浮点数
 """
""" 

 # Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)

print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'Numpy', 'Pandas']"
 """

""" 
新样式字符串格式 (str.format)
这种格式是在 python 版本 3 中引入的。
 """


""" first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)

print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a cricle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal

print(formated_string)

 """

# greeting = 'Hello, World!'
# greeting = '1234567890'
# print(greeting[::-1])

# language = 'Python'
# pto = language[2:3] #
# print(pto) # Pto
""" 
challenge = 'thirty days of python'
print(challenge.capitalize())
# print(challenge.capitalize()) # 'Thirty days of python'



challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`

print(challenge.count('y'))
print(challenge.count('y', 4, 12))
 """
""" 
challenge = 'thirty days of python'
# print(challenge.endswith('on'))   # True
# print(challenge.endswith('tion')) # False

print(challenge.endswith('on'))
print(challenge.endswith('123'))
 """

 
""" challenge = 'thirty\tdays\tof\tpython'
# print(challenge.expandtabs())   # 'thirty  days    of      python'
# print(challenge.expandtabs(10)) # 'thirty    days      of        python'
print(challenge.expandtabs())
print(challenge.expandtabs(8)) """

""" challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

challenge = 'thirty days of python'
print(challenge.rfind('days'))  # 5
print(challenge.rfind('th')) # 1
 """

""" 
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314
 """

""" challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 3)) # error
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 8
print(challenge.index(sub_string, 2)) # error

 """
""" isalnum() 检测包含字母数字字符 """
""" 
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False
 """
#  isalpha()：检查所有字符串元素是否都是字母字符（az 和 AZ）

""" challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False
 """

#  isdecimal(): 检查字符串中的所有字符是否都是十进制 (0-9)
""" challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdecimal())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, no space allowed
 """

#  isdigit()：检查字符串中的所有字符是否都是数字（0-9 和其他一些用于数字的 unicode 字符）
""" 
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u0032'
print(challenge.isdigit())   # True
"""

# isnumeric()：检查字符串中的所有字符是否都是数字或数字相关的（就像 isdigit()，只接受更多的符号，比如 ½）
""" num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
 """

# isidentifier()：检查一个有效的标识符——意味着它检查一个字符串是否是一个有效的变量名
# challenge = '30DaysOfPython'
# print(challenge.isidentifier()) # False, because it starts with a number
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier()) # True


# islower()：检查字符串中的所有字母字符是否都是小写
# challenge = 'thirty days of python'
# print(challenge.islower()) # True
# challenge = 'Thirty days of python'
# print(challenge.islower()) # False

# isupper()：检查字符串中的所有字母字符是否都是大写
# challenge = 'thirty days of python'
# print(challenge.isupper()) #  False
# challenge = 'THIRTY DAYS OF PYTHON'
# print(challenge.isupper()) # True

# join()：返回一个连接的字符串
# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = '# '.join(web_tech)
# print(result) # 'HTML# CSS# JavaScript# React'
# print(' '.join(web_tech))


# strip()：从字符串的开头和结尾删除所有给定的字符
# challenge = 'thirty days of pythoonnn'
# print(challenge.strip('noth')) # 'irty days of py'
# print(challenge.strip('nothy'))

# replace()：用给定的字符串替换子字符串
# challenge = 'thirty days of python'
# print(challenge.replace('python', 'coding')) # 'thirty days of coding'
# print(challenge.replace('python', 'codinging'))

# split(): 拆分字符串，使用给定的字符串作为分隔符
# challenge = 'thirty days of python'
# print(challenge.split(' ')) # ['thirty', 'days', 'of', 'python']
# print(challenge.split())
# challenge = 'thirty, days, of, python'
# print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# title()：返回一个标题大小写的字符串
# challenge = 'thirty days of python'
# print(challenge.title()) # Thirty Days Of Python
# print(challenge.title())

# swapcase()：将所有大写字符转换为小写，将所有小写字符转换为大写字符 : 大小写装换
# challenge = 'thirty days of python123'
# print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
# print(challenge.swapcase())
# challenge = 'Thirty Days Of Python321'
# print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
# print(challenge.swapcase())

# startswith()：检查字符串是否以指定的字符串开头
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
print(challenge.startswith('thirty'))
print(challenge.endswith('python'))

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False



