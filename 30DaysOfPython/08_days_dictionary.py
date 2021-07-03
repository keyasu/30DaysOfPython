print('days - 08 - dictionary')

""" 
字典是无序、可修改（可变）成对（键：值）数据类型的集合。

"""

# # syntax
# empty_dict = {}
# # Dictionary with data values
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# syntax

# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210',
#         },
#     }
# print(person)
# print(len(person))

# syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dct['key11']) # value1
# print(dct['key4']) # value4

# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210',
#         },
#     }


# print(person.get('first_name')) # Asabeneh
# print(person.get('country'))    # Finland
# print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
# print(person.get('city'))   # None

# syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print('key2' in dct) # True
# print('key5' in dct) # False

# syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# dct.pop('key1') # removes key1 item

# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dct)
# dct.popitem() # removes the last item
# print(dct)
# del dct['key2'] # removes key2 item
# print(dct)

# syntax - 转换为items
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# syntax - 清空字典
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dct.clear()) # None

# syntax - 删除字典
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dct)
# del dct
# print(dct)


# syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# dct.copy()

# syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# print(dct.keys())
# print(dct.values())
# keys = dct.keys()
# print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
