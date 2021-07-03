print('days - 07 - sets')

""" 
让我带你回到你的小学或高中数学课。
集合的数学定义也适用于 python。
Set 是无序和无索引的不同元素的集合。
在蟒蛇组用于存储唯一的项目，就可以找到工会，交集，差，对称差，子集，超集和分离集集之间。


"""

# # syntax
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# print(fruits)
# print(len(fruits))
# fruits.add('apple')
# print(fruits)
# fruits.update(['item1', 'item2', 'item3'])
# print(fruits)

# 我们可以使用remove()方法从集合中删除一个项目。如果未找到该项目，remove()方法将引发错误，因此最好检查该项目是否存在于给定的集合中。但是，discard()方法不会引发任何错误。
# syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# print(st)
# st.remove('item2')
# print(st)

# fruits = {'banana', 'orange', 'mango', 'lemon'}
# print(fruits)
# fruits.pop()  # removes the last element from the set
# print(fruits)
# fruits.clear()
# print(fruits)

# del fruits
# print(fruits)


# fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
# print(type(fruits))
# fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
# print(type(fruits))

# syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item5', 'item6', 'item7', 'item8'}
# st3 = st1.union(st2)
# print(st3)
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
# print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}


# syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item5', 'item6', 'item7', 'item8'}
# st1.update(st2) # st2 contents are added to st1
# st1.update(st2)
# print(st1)


# # 交集
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item3', 'item2'}
# st1.intersection(st2) # {'item3', 'item2'}
# print(st1)
# print(st1.intersection(st2))
# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.intersection(dragon)     # {'o', 'n'}

# syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# st2.issubset(st1) # True
# st1.issuperset(st2) # True
# print(st2.issubset(st1))
# print(st1.issuperset(st2))

# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# whole_numbers.issubset(even_numbers) # False, because it is a super set
# whole_numbers.issuperset(even_numbers) # True

# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.issubset(dragon)     # False

# syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# st2.difference(st1) # set()
# st1.difference(st2) # {'item1', 'item4'} => st1\st2
# print(st2.difference(st1))
# print(st1.difference(st2))
# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

# python = {'p', 'y', 't', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# dragon.difference(python)     # {'d', 'r', 'a', 'g'}

# 寻找两个集合之间的对称差异
# 它返回两个集合之间的对称差异。这意味着它返回一个包含两个集合中所有项目的集合，除了两个集合中都存在的项目，数学上： (A\B) ∪ (B\A)

# syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item5', 'item6'}
# # it means (A\B)∪(B)
# st3 = st2.symmetric_difference(st1) # {'item1', 'item4'}
# print(st3)

# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# some_numbers = {1, 2, 3, 4, 5}
# whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item5'}
st3 = st2.isdisjoint(st1) # False
print(st3)
