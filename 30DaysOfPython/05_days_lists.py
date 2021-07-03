print('days - 05 - lists')

""" 
python中有四种集合数据类型：

列表：是一个有序且可变（可修改）的集合。允许重复成员。
元组：是有序且不可更改或不可修改（不可变）的集合。允许重复成员。
Set：是一个无序、无索引且不可修改的集合，但您可以添加新项目。没有重复的成员。
字典：是一个无序、可变（可修改）和索引的集合。没有重复的成员。
列表是有序且可修改（可变）的不同数据类型的集合。列表可以为空，也可以具有不同的数据类型项或项


 """

"""  # syntax
lst = list()
print(lst)

# syntax
lst = []
print(lst)

empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0
 """

""" fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
 """

""" fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
 """


""" fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
 """

""" lst = ['item','item2','item3', 'item4', 'item5']
# first_item, second_item, third_item, *rest = lst
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
 """
""" # First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
 """

# 正索引：我们可以通过指定开始、结束和步骤来指定一系列正索引，返回值将是一个新列表。（开始的默认值 = 0，结束 = len(lst) - 1（最后一项），步骤 = 1）
""" fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
print(all_fruits)

all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
print(all_fruits)

orange_and_mango = fruits[1:3] # it does not include the first index
print(orange_and_mango)

orange_mango_lemon = fruits[1:]
print(orange_mango_lemon)

orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['orange', 'lemon']
print(orange_and_lemon) """
# 负索引：我们可以通过指定开始、结束和步骤来指定一系列负索引，返回值将是一个新列表。
""" fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
print(all_fruits)

orange_and_mango = fruits[-3:-1] # it does not include the last index
print(orange_and_mango)

orange_mango_lemon = fruits[-3:] # this will give the same result as the one above
print(orange_mango_lemon)

reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order
print(reverse_fruits)
 """

# 列表是可变或可修改的有序项集合。让我们修改水果列表。
""" fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

 """
# syntax
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.append('apple')
# print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
# fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
# print(fruits)

""" fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)


fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']
 """

# pop() 方法删除指定的索引，（如果未指定索引，则删除最后一项）：
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.pop()
# print(fruits)       # ['banana', 'orange', 'mango']

# fruits.pop(0)
# print(fruits)       # ['orange', 'mango']

# del 关键字删除指定的索引，也可用于删除索引范围内的项目。它也可以完全删除列表
# fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
# # del fruits[0]
# # print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
# # del fruits[1]
# # print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
# print(fruits[1:3])

# del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
# print(fruits)       # ['orange', 'lime']
# # del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined


# syntax
# clear() 方法清空列表：
# lst = ['item1', 'item2']
# print(lst)
# lst.clear()
# print(lst)

# 可以通过以下方式将列表重新分配给新变量来复制列表：list2 = list1。现在，list2 是对list1 的引用，我们在list2 中所做的任何更改也将修改原来的list2。
# 但是在很多情况下，我们不喜欢修改原始版本，而是喜欢拥有不同的副本。避免上述问题的一种方法是使用copy()。
# syntax
# lst = ['item1', 'item2']
# lst_copy = lst.copy()

# positive_numbers = [1, 2, 3, 4, 5]
# zero = [0]
# negative_numbers = [-5,-4,-3,-2,-1]
# integers = negative_numbers + zero + positive_numbers
# print(integers)
# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables )

# 使用 extend() 方法加入
# list1 = ['item1', 'item2']
# list2 = ['item3', 'item4', 'item5']
# list1.extend(list2)
# print(list1)

# num1 = [0, 1, 2, 3]
# num2 = [4, 5,6]
# num1.extend(num2)
# print('Numbers:', num1)
# negative_numbers = [-5,-4,-3,-2,-1]
# positive_numbers = [1, 2, 3,4,5]
# zero = [0]

# negative_numbers.extend(zero)
# negative_numbers.extend(positive_numbers)
# print('Integers:', negative_numbers)
# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
# fruits.extend(vegetables)
# print('Fruits and vegetables:', fruits )

# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(fruits.count('orange'))   # 1
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# print(ages.count(24))           # 3


# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(fruits.index('orange'))   # 1

# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# print(ages.index(24))   # 2, the first occurrence

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.reverse()
# print(fruits)
# fruits.reverse()
# print(fruits)
# print(fruits.reverse())
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# ages.reverse()
# print(ages)
# print(ages.reverse())
# print(ages.reverse())

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.sort(reverse=False)
# print(fruits)             # sorted in alphabetical order
# fruits.sort(reverse=True)
# print(fruits)
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# ages.sort()
# print(ages)
# ages.sort(reverse=True)
# print(ages)

#  sorted() : 返回有序的list 并不修改原来的值
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))     # ['banana', 'lemon', 'mango', 'orange']
print(fruits)
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']






