print('days - 13 - List Comprehension')

# Python 中的列表推导式是一种从序列创建列表的紧凑方式。这是创建新列表的一种快捷方式。列表理解比使用for循环处理列表快得多。

# One way
# language = 'Python'
# lst = list(language) # changing the string to list
# print(type(lst))     # list
# print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# # Second way: list comprehension
# lst = [i for i in language]
# print(type(lst)) # list
# print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']
# # Generating numbers
# numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
# print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # It is possible to do mathematical operations during iteration
# squares = [i * i for i in range(11)]
# print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# # It is also possible to make a list of tuples
# numbers = [(i, i * i) for i in range(11)]
# print(numbers)    
#                          # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# # Generating even numbers
# even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
# print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# # Generating odd numbers
# odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
# print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# # Filter numbers: let's filter out positive even numbers from the list below
# numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
# positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
# print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# # Flattening a three dimensional array
# three_dimen_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened_list = [ number for row in three_dimen_list for number in row]
# print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Lambda 函数是一个没有名字的小型匿名函数。它可以接受任意数量的参数，但只能有一个表达式。Lambda 函数类似于 JavaScript 中的匿名函数。当我们想在另一个函数中编写匿名函数时，我们需要它。

# # Named function
# def add_two_nums(a, b):
#     return a + b

# print(add_two_nums(2, 3))     # 5
# # Lets change the above function to a lambda function
# add_two_nums = lambda a, b: a + b
# print(add_two_nums(2,3))    # 5

# # Self invoking lambda function
# (lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

# square = lambda x : x ** 2
# print(square(3))    # 9
# cube = lambda x : x ** 3
# print(cube(3))    # 27

# # Multiple variables
# multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
# print(multiple_variable(5, 5, 3))

def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32

