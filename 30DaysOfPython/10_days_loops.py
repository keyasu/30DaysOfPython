print('days - 10 - loops')

""" 
生活处处都是例行公事。在编程中，我们也会做很多重复的任务。为了处理重复性任务，编程语言提供了循环。Python 编程语言还提供了以下两种循环类型：

    while 循环
    for循环

"""


# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print(count)

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
#     if count == 3:
#         break

# count = 0
# while count < 5:
#     if count == 3:
#         continue
    
#     print(count)
#     count = count + 1


# numbers = [0, 1, 2, 3, 4, 5]
# for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
#     print(number)       # the numbers will be printed line by line, from 0 to 5


# language = 'Python'
# for letter in language:
#     print(letter)

# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }
# for key in person:
#     print(key)

# for (key, value) in person.items():
#     print(key, value) # this way we get both keys and values printed out

# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# for company in it_companies:
#     print(company)

# numbers = (10,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
# print('outside the loop')

# lst = list(range(11)) 
# print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
# print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# lst = list(range(0,11,4))
# print(lst) # [0, 2, 4, 6, 8, 10]
# st = set(range(0,11,2))
# print(st) #  {0, 2, 4, 6, 8, 10}
# for number in range(11):
#     print(number)   # prints 0 to 10, not including 11

# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)


# for number in range(11):
#     print(number)   # prints 0 to 10, not including 11
# else:
#     print('The loop stops at', number)


# for number in range(6):
#     pass

# count = 1
# while count < 8:
#     print('########'[0:count])
#     count = count + 1


cStr = '###############################'
lists = [[8, 1, 7, 1, 7], [1], [7, 1, 15, 1, 7, 1, 6]]

for list in lists:
    str = []
    for number in list:

        sStr = cStr[0:number]
        str.append(sStr)
        # print(number)
        # str = sStr+"  "
    
    print(' '.join(str))
        
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100


for i in range(11):
    result = '{} x {} = {}'.format(i, i, i * i)
    print(result)