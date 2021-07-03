print('18_regular_expressions')

""" 
常用表达
正则表达式或 RegEx 是一种特殊的文本字符串，有助于在数据中查找模式。RegEx 可用于检查某些模式是否存在于不同的数据类型中。要首先在 python 中使用 RegEx，我们应该导入名为re的 RegEx 模块。
正则表达式  RegRx

 """

# import re
""" 
 re模块中的函数
为了找到一个模式，我们使用不同的re字符集集，允许在字符串中搜索匹配项。

    re.match()：仅在字符串第一行的开头搜索，如果找到则返回匹配的对象，否则返回无。
    re.search：如果字符串中的任何地方都有匹配对象，包括多行字符串，则返回一个匹配对象。
    re.findall：返回包含所有匹配项的列表
    re.split：获取一个字符串，在匹配点处将其拆分，返回一个列表
    re.sub：替换字符串中的一个或多个匹配项
    
    re.mathc()
    re.search
    re.findall
    re.split
    re.sub

"""


""" 
import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach
 """
# txt = 'I love to teach python and javaScript'
# match = re.match('I love to teach', txt, re.I)
# print(match)
# span = match.span()
# print(span)
# start, end = span
# print(start, end)
# substring = txt[start : end]
# print(substring)

# 从上面的示例中可以看出，我们正在寻找的模式（或我们正在寻找的子字符串）是I love to Teaching。仅当文本以模式开头时，match 函数才返回一个对象。


import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

""" # It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
 """
# match = re.search('first', txt, re.I)
# print(match)
# span = match.span()
# start, end = span
# print(start, end)
# substring = txt[start : end]
# print(substring)
# 如您所见，搜索比匹配好得多，因为它可以在整个文本中查找模式。搜索返回具有找到的第一个匹配项的匹配对象，否则返回None。一个更好的re函数是findall。此函数检查整个字符串中的模式并将所有匹配项作为列表返回。
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# It return a list
# matches = re.findall('language', txt, re.I)
# print(matches)  # ['language', 'language']
# matchs = re.findall('language', txt, re.I)
# print(matchs)
# 如您所见，在字符串中找到了两次 language 一词。让我们多练习一些。现在我们将在字符串中查找 Python 和 python 单词：



# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# It returns list
# matches = re.findall('python', txt, re.I)
# print(matches)  # ['Python', 'python']
# matchs = re.findall('python', txt, re.I)
# print(matchs)
# 由于我们使用re.I，因此包括小写和大写字母。如果我们没有那个标志，那么我们将不得不以不同的方式编写我们的模式。让我们来看看：


# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# matches = re.findall('Python|python', txt)
# print(matches)  # ['Python', 'python']
# matches = re.findall('[Pp]ython', txt)
# print(matches)  # ['Python', 'python']

# 替换子串
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
# print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# # OR
# match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
# print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

# match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
# print(match_replaced)

# match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
# print(match_replaced)


""" 
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

# matches = re.sub('%', '', txt)
# print(matches)
mathches = re.sub('%', '', txt)
print(mathches)

 """

""" txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

# print(re.split('\n', txt)) # splitting using \n - end of line symbol
print(re.split('\n', txt))
 """


""" 
重头戏来了
 """
#  编写正则表达式模式
# 要声明一个字符串变量，我们使用单引号或双引号。
# 声明 RegEx 变量r''。
# 下面的模式只用小写字母标识苹果，为了使它不区分大小写，我们应该重写我们的模式，或者我们应该添加一个标志。

""" import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# 为了不区分大小写添加标志 ' 
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
 """
""" import re
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)
# 不进行大小写的区分
matches = re.findall(regex_pattern, txt, re.I)
print(matches)
# 
regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)
 """
#  匹配的格式为
""" 
 []：一组字符
    [ac] 表示 a 或 b 或 c
    [az] 表示从 a 到 z 的任何字母
    [AZ] 表示从 A 到 Z 的任何字符
    [0-3] 表示 0 或 1 或 2 或 3
    [0-9] 表示 0 到 9 之间的任意数字
    [A-Za-z0-9] 任何单个字符，即 a 到 z、A 到 Z 或 0 到 9
\：用于转义特殊字符
    \d 表示：匹配字符串包含数字的地方（0-9 的数字）
    \D 表示：匹配不包含数字的字符串
. : 除换行符以外的任何字符(\n)
^：以什么开后
    r'^substring' eg r'^love', 一个以单词 love 开头的句子
    r'[^abc] 表示不是 a，不是 b，不是 c。
$：以什么结尾
    r'substring$' 例如 r'love$'，以单词 love 结尾的句子
*：零次或多次
    r'[a]*' 表示一个可选的或者它可以出现多次。
+：一次或多次
    r'[a]+' 表示至少一次（或多次）
?: 零次或一次
    r'[a]?' 表示零次或一次
{3}：正好 3 个字符
{3,}：至少 3 个字符
{3,8}：3 到 8 个字符
|: 或者关系
    r'apple|banana' 表示苹果或香蕉
()：捕获和分组 

"""


# 让我们使用方括号来包含小写和大写

# txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
# regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
# matches = re.findall(regex_pattern, txt)
# print(matches)  # ['Apple', 'apple']
# regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
# txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
# matches = re.findall(regex_pattern, txt)
# print(matches)  # ['Apple', 'banana', 'apple', 'banana']
# regex_pattern = r'[Aa]pple|[Bb]anana'
# matches = re.findall(regex_pattern, txt)
# print(matches)

# 正则表达式中的转义字符（\）
# # regex_pattern = r'\d'  # d is a special character which means digits
# txt = 'This regular expression example was made on December 6,  2019.'
# # matches = re.findall(regex_pattern, txt)
# # print(matches)  # ['6', '2', '0', '1', '9'], this is not what we want
# regax_patthen = r'\d+'
# matches = re.findall(regax_patthen, txt)
# print(matches)

# txt = '''Apple and banana are fruits'''
# regex_pattern = r'[a].?'
# matches = re.findall(regex_pattern, txt)
# print(matches)

# regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line

# matches = re.findall(regex_pattern, txt)
# print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

# regex_pattern = r'[a].+'  # . any character, + any character one or more times 
# matches = re.findall(regex_pattern, txt)
# print(matches)  # ['and banana are fruits']

# 零次或多次。该模式可能不会出现，也可能会出现多次。

""" txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
 """

# 零次或一次。该模式可能不会出现，也可能出现一次。
""" txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
 """

# 正则表达式中的量词
# 我们可以使用大括号指定我们在文本中查找的子字符串的长度。
# 让我们想象一下，我们对长度为 4 个字符的子字符串感兴趣：
# txt = 'This regular expression example was made on December 6,  2019.'
# regex_pattern = r'\d{4}'  # exactly four times
# matches = re.findall(regex_pattern, txt)
# print(matches)  # ['2019']

# txt = 'This regular expression example was made on December 6,  2019.'
# regex_pattern = r'\d{1, 4}'   # 1 to 4
# matches = re.findall(regex_pattern, txt)
# print(matches)  # ['6', '2019']


# txt = 'This regular expression example was made on December 6,  2019.'
# regex_pattern = r'^This'  # ^ means starts with
# matches = re.findall(regex_pattern, txt)
# print(matches)  # ['This']

txt = 'This regular expression example was made on December 6,  2019.'
# regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
# matches = re.findall(regex_pattern, txt)
# print(matches)  # ['6,', '2019.']
regex_pattern = r'[^A-Za-z]+'
matches = re.findall(regex_pattern, txt)
print(matches)






