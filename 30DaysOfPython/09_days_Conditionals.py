print('days - 09 - Conditionals')

""" 
默认情况下，python脚本中的语句是从上到下依次执行的。如果处理逻辑需要，可以通过两种方式改变执行的顺序流程：

条件执行：如果某个表达式为真，将执行一个或多个语句块
重复执行：只要某个表达式为真，一个或多个语句块就会被重复执行。
在本节中，我们将介绍if、else、elif语句。我们在前几节中学到的比较和逻辑运算符在这里会很有用。

 """


# a = 0
# if a > 0:
#     print('A is a positive number')
# elif a < 0:
#     print('A is a negative number')
# else:
#     print('A is zero')

# if a > 0:
#     print('')
# elif a < 0:
#     print('')
# else:
#     print()


a = 3
# print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed
print('A is position') if a > 0 else print('A is negative')
