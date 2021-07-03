print('25_pandas')

""" 
Pandas 是 Python 编程语言的开源、高性能、易用的数据结构和数据分析工具。
    
    Pandas 添加了数据结构和工具，旨在处理类似表格的数据，即系列和数据框。
    Pandas 提供了数据操作工具：重塑、合并、排序、切片、聚合和插补。

 """
# import pandas as pd # importing pandas as pd
# import numpy  as np # importing numpy as np

import pandas as pd
import numpy as np

# 使用默认索引创建 Pandas 系列
""" nums = [1, 2, 3, 4, 5]
# s = pd.Series(nums)
# print(s)
s = pd.Series(nums)
print(s) """

# 使用自定义索引创建 Pandas 系列
""" nums = [1, 2, 3, 4, 5]
# s = pd.Series(nums, index=[1, 2, 3, 4, 5])
s = pd.Series(nums, index=[1,2,3,4,5])
print(s) """

""" fruits = ['Orange','Banana','Mangao']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits) """


# 从字典创建 Pandas 系列
""" dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s)

s = pd.Series(10, index = [1, 2,3])
print(s) """


""" s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)
 """
""" data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names', 'Country', 'City'])

print(df)
 """

""" data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)

print(df)

data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df) """

# curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv
# import pandas as pd

# df = pd.read_csv('weight-height.csv')
# # print(df)
# # print(df.head()) # 给五行我们可以通过将参数传递给 head() 方法来增加行数
# # print(df.shape)
# # print(df.columns)
# # print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method
# heights = df['Height'] # this is now a series
# # print(heights)
# weights = df['Weight'] # this is now a series
# # print(weights)

# # print(len(heights) == len(weights))

# # print(heights.describe()) # give statisical information about height data
# # print(weights.describe())
# print(df.describe())  # describe 还可以给出来自数据帧的统计信息


""" 
修改DataFrame： 
  * 我们可以创建一个新的DataFrame 
  * 我们可以创建一个新列并将其添加到DataFrame， 
  * 我们可以从DataFrame 中删除现有列， 
  * 我们可以修改DataFrame 中的现有列， 
  * 我们可以更改 DataFrame 中列值的数据类型

"""
import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)
weights = [74, 78, 69]
df['Weight'] = weights
print(df)
heights = [173, 175, 169]
df['Height'] = heights
print(df)
df['Height'] = df['Height'] * 0.01
print(df)
# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
    
bmi = calculate_bmi()
print(bmi)
df['BMI'] = bmi
print(df)

df['BMI'] = round(df['BMI'], 1)
print(df)

birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2021, index=[0, 1, 2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)

print(df.Weight.dtype)
print(df['Birth Year'].dtype) # it gives string object , we should change this to number

df['Current Year'] = df['Current Year'].astype('int')
print(df['Current Year'].dtype)

ages = df['Current Year'].astype('int') - df['Birth Year'].astype('int')
print(ages)
df['Ages'] = ages
print(df)

mean = (36 + 31)/ 2
print('Mean: ',mean)	#it is good to add some description to the output, so we know what is what


print(df[df['Ages'] < 120])















