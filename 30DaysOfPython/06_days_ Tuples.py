print('days-06-Tuples')

""" 
元组是有序且不可更改（不可变）的不同数据类型的集合。
元组用圆括号 () 书写。
一旦创建了一个元组，我们就不能改变它的值。
我们不能在元组中使用 add、insert、remove 方法，因为它不可修改（可变）。
与列表不同，元组的方法很少。
与元组相关的方法：

    tuple(): 创建一个空元组
    count()：计算元组中指定项的个数
    index()：在元组中查找指定项的索引
        运算符：连接两个或多个元组并创建一个新元组

 """

 # syntax
""" tpl = ('item1', 'item2','item3')
print(tpl)
print(len(tpl))

first_item = tpl[0]
second_item = tpl[1]

print(first_item)
print(second_item) """

""" fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

print(first_fruit)
print(second_fruit)
print(last_fruit)
 """
""" 
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

print(first_fruit)
print(second_fruit)
print(last_fruit) """

# 我们可以通过指定一个索引范围来切出一个子元组从哪里开始和在哪里结束，返回值将是一个具有指定项的新元组。
# # Syntax
# tpl = ('item1', 'item2', 'item3','item4')
# all_items = tpl[0:4]         # all items
# all_items = tpl[0:]         # all items
# middle_two_items = tpl[-3:-1]  # does not include item at index 3

# print(all_items)
# print(middle_two_items)

# 我们可以将元组更改为列表，将列表更改为元组。元组是不可变的，如果我们想修改一个元组，我们应该把它改成一个列表。
# fruits = ('banana', 'orange', 'mango', 'lemon')
# fruits = list(fruits)
# fruits[0] = 'apple'
# print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
# fruits = tuple(fruits)
# print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# # 我们可以使用in检查列表中是否存在项目，它返回一个布尔值。
# fruits = ('banana', 'orange', 'mango', 'lemon')
# print('orange' in fruits) # True
# print('apple' in fruits) # False
# fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment


# # 我们可以使用 + 运算符连接两个或多个元组
# fruits = ('banana', 'orange', 'mango', 'lemon')
# vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
# fruits_and_vegetables = fruits + vegetables

# print(fruits_and_vegetables)

# 不可能删除元组中的单个项目，但可以使用del删除元组本身。
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)

del fruits
print(fruits)
