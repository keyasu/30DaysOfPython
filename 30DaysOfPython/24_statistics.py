print('24_statistics')
""" 
统计数据
统计学是研究数据的收集、组织、显示、分析、解释和呈现的学科。
    统计学是数学的一个分支，建议作为数据科学和机器学习的先决条件。
    统计学是一个非常广泛的领域，但我们将在本节中只关注最相关的部分。
    
    完成此挑战后，您可以进入 Web 开发、数据分析、机器学习和数据科学路径。
    
    无论您走哪条路，在您职业生涯的某个阶段，您都会获得可以处理的数据。
    拥有一些统计知识将帮助您根据数据做出决策，数据如他们所说。

数据

    什么是数据？数据是为某种目的（通常是分析）收集和翻译的任何字符集。它可以是任何字符，包括文本和数字、图片、声音或视频。如果数据没有放在上下文中，它对人或计算机没有任何意义。为了让数据有意义，我们需要使用不同的工具处理数据。
    数据分析、数据科学或机器学习的工作流程始于数据。可以从某个数据源提供数据，也可以创建数据。有结构化和非结构化数据。  
    可以以小格式或大格式找到数据。我们将获得的大多数数据类型已在文件处理部分中介绍。

统计模块
    
    python统计模块提供了计算数值数据的数理统计的函数。该模块无意成为第三方库（如 NumPy、SciPy）或面向专业统计学家（如 Minitab、SAS 和 Matlab）的专有全功能统计软件包的竞争对手。它针对图形和科学计算器的级别。

NumPy
    
    在第一部分中，我们将 python 定义为一种出色的通用编程语言，但在其他流行库（numpy、scipy、matplotlib、pandas 等）的帮助下，它成为了一个强大的科学计算环境。
    Numpy 是 Python 科学计算的核心库。它提供了一个高性能的多维数组对象，以及用于处理数组的工具。
    到目前为止，我们一直在使用 vscode，但从现在开始我会推荐使用 Jupyter Notebook。要访问 jupter notebook，让我们安装anaconda。如果你使用anaconda，大部分常用包都包含在内，所以你不必安装更多的包。


 """

 # 如何导入 numpy 

import  numpy  as  np
from numpy.random.mtrand import randint 
# # 如何检查 numpy 包的版本
# print ( 'numpy:' , np . __version__ )
#  # 检查可用方法
# print ( dir ( np ))

# python_list = [1, 2, 3, 4, 5]
# print('Type:', type(python_list))
# print(python_list)
# two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
# print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# numpy_array_from_list = np.array(python_list)
# # np.array(python_list)
# print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
# print(numpy_array_from_list) # array([1, 2, 3, 4, 5])

# Python list
# 使用浮点数据类型参数从列表创建浮点 numpy 数组
""" python_list = [1,2,3,4,5]
numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])
 """

#  从列表创建一个布尔值 numpy 数组
""" numpy_bool_array = np.array([0, 1, -1, 2, 3], dtype=bool)
print(numpy_bool_array) """


# 使用numpy创建多维数组
# 一个 numpy 数组可能有一个或多个行和列
""" 
two_demiensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_list = np.array(two_demiensional_list)
print(numpy_two_dimensional_list)
print(type(numpy_two_dimensional_list))
 """


# 在 numpy 中要知道 numpy 数组列表中的项目数，我们使用 size

# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# two_dimensional_list = np.array([[0, 1, 2],
#                               [3, 4, 5],
#                               [6, 7, 8]])

# print('The size:', numpy_array_from_list.size) # 5
# print('The size:', two_dimensional_list.size)  # 9 

# 将 numpy 数组转换为列表
# # We can always convert an array back to a python list using tolist().
# np_to_list = numpy_array_from_list.tolist()
# print(type (np_to_list))
# print('one dimensional array:', np_to_list)
# print('two dimensional array: ', numpy_two_dimensional_list.tolist())
# np_to_list = numpy_array_from_list.tolist()
# print(type(np_to_list))
# print('one dimensional array: ', np_to_list)
# print('two dimensional array: ', numpy_array_from_list.tolist())

# numpy 数组的形状
# shape 方法以元组的形式提供数组的形状。第一个是行，第二个是列。如果数组只是一维，则返回数组的大小。
# nums = np.array([1, 2, 3, 4, 5])
# print(nums)
# print('shape of nums:', nums.shape)
# print('shape of numpu_two_dimensional_list:', two_dimensional_list.shape)

# three_by_four_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
# print(three_by_four_array)

# numpy数组的数据类型
# 数据类型类型：str、int、float、complex、bool、list、None

# int_lists = [-3, -2, -1, 0, 1, 2,3]
# int_array = np.array(int_lists)
# float_array = np.array(int_lists, dtype=float)

# print(int_array)
# print(int_array.dtype)
# print(float_array)
# print(float_array.dtype)


# 使用numpy进行数学运算
# Numpy 数组并不完全像 python 列表。要在 pyhton 列表中进行数学运算，我们必须遍历项目，但 numpy 可以允许在不循环的情况下进行任何数学运算。数学运算：

# 加法 (+)
# 减法 (-)
# 乘法 (*)
# 分配 （/）
# 模块 (%)
# 楼层划分(//)
# 指数(**)


# Mathematical Operation
# Addition
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_plus_original = numpy_array_from_list  + 10
# print(ten_plus_original)


# Subtraction
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_minus_original = numpy_array_from_list  - 10
# print(ten_minus_original)


# # Multiplication
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_times_original = numpy_array_from_list * 10
# print(ten_times_original)

# # Division
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_times_original = numpy_array_from_list / 10
# print(ten_times_original)


# # Modulus; Finding the remainder
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_times_original = numpy_array_from_list % 3
# print(ten_times_original)

# # Floor division: the division result without the remainder
# numpy_array_from_list = np.array([11, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_times_original = numpy_array_from_list // 10
# print(ten_times_original)

# # Exponential is finding some number the power of another:
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_times_original = numpy_array_from_list  ** 2
# print(ten_times_original)

# #Int,  Float numbers
# numpy_int_arr = np.array([1, 2, 3, 4])
# numpy_float_arr = np.array([1.1, 2.0, 3.2])
# numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')

# print(numpy_int_arr.dtype)
# print(numpy_float_arr.dtype)
# print(numpy_bool_arr.dtype)

# numpy_float_list = np.array([1.1, 2.0, 3.2])

# dd = numpy_float_list.astype('int').astype('str')

# print(type(dd))
# print(dd)

# 2 Dimension Array
""" two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array) """

# 切片 Numpy 数组
# 在 numpy 中切片类似于在 python list 中切片
# two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
# first_two_rows_and_columns = two_dimension_array[0:2, 0:2]

# print(first_two_rows_and_columns)

# print(two_dimension_array[::])

    # two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
    # two_dimension_array[::-1,::-1]

# print(two_dimension_array[::-1, ::-1])

# print(two_dimension_array)
# two_dimension_array[1,1] = 55
# two_dimension_array[1,2] =44
# print(two_dimension_array)

# Numpy Zeroes
# numpy.zeros(shape, dtype=float, order='C')
# numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
# # numpy_zeroes
# numpy_zeroes = np.zeros((3, 3), dtype=int, order="F") # rder must be one of 'C', 'F', 'A', or 'K' (got 'D')

# print(numpy_zeroes)


# Numpy Zeroes
# numpy_ones = np.ones((3,3),dtype=int,order='C')
# print(numpy_ones)
# twoes = numpy_ones * 2
# print(twoes)

# Reshape
# numpy.reshape(), numpy.flatten()
# first_shape  = np.array([(1,2,3), (4,5,6)])
# print(first_shape)
# reshaped = first_shape.reshape(3,2)
# print(reshaped)
# flattened = reshaped.flatten()
# print(flattened)

## Horitzontal Stack
# np_list_one = np.array([1,2,3])
# np_list_two = np.array([4,5,6])

# print(np_list_one + np_list_two)

# print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))

# print('Horizontal Append:', np.vstack((np_list_one, np_list_two)))

# # Generate a random float  number
# random_float = np.random.random()
# print(random_float)

# # Generate a random float  number
# random_floats = np.random.random(5)
# print(random_floats)

# 生成 0 到 10 之间的随机整数
# random_int = np.random.randint(0, 11)
# print(random_int)

# 生成一个 2 到 11 之间的随机整数，并创建一个
# random_int = np.random,randint(2, 10, size=4)
# print(list(random_int))
# Generating a random integers between 0 and 10
# random_int = np.random.randint(2,10, size=(3,3))
# print(random_int)

    # np.random.normal(mu, sigma, size)
# normal_array = np.random.normal(79, 15, 80)
# print(normal_array)

# np.random.normal(mu, sigma, size)
# normal_array = np.random.normal(79, 15, 80)
# print(normal_array)



import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()
# plt.hist(normal_array, color="grey", bins=50)



# four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
# print(four_by_four_matrix)

# np.asarray(four_by_four_matrix)[2] = 2
# print(four_by_four_matrix)

# creating list using range(starting, stop, step)
# lst = range(0, 11, 2)
# lst = range(0, 11, 2)
# print(lst)
# for l in lst:
#     print(l)
# # Similar to range arange numpy.arange(start, stop, step)
# whole_numbers = np.arange(0, 20, 1)
# print(whole_numbers)

# numpy.linspace()
# numpy.logspace() in Python with Example
# 例如，它可以用来创建从 1 到 5 的 10 个均匀间隔的值。
# np.linspace(1.0, 5.0, num=10)
# one = np.linspace(1.0, 5.0, num=10)
# print(one)

# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace（开始，停止，数量，端点）
# np.logspace(2, 4.0, num=4)

#  检查数组的大小
# x = np.array([1,2,3], dtype=np.complex128)
# print(x)
# print(x.itemsize)


# 在 Python 中索引和切片 NumPy 数组
""" np_list = np.array([(1,2,3), (4,5,6)])
print(np_list)
print('First row: ', np_list[0])
print('Second row: ', np_list[1])


print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])

 """


""" 
NumPy 统计函数与示例
NumPy 具有非常有用的统计函数，用于从数组中的给定元素中查找最小值、最大值、平均值、中位数、百分位数、标准偏差和方差等。
函数解释如下 - 统计函数 Numpy 配备了如下所列的稳健统计函数

    Numpy 函数
    最小 np.min()
    最大 np.max()
    平均 np.mean()
    中位数 np.median()
    差异
    百分位
    标准差 np.std()

 """

""" two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)
## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array, axis = 0))
print('Column with maximum: ', np.amax(two_dimension_array, axis = 0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array, axis = 1))
print('Row with maximum: ', np.amax(two_dimension_array, axis = 1))

 """
# a = [1,2,3]

# # Repeat whole of 'a' two times
# print('Tile:   ', np.tile(a, 2))
# print('Title:  ', np.tile(a, 2))
# # Repeat each element of 'a' two times
# print('Repeat: ', np.repeat(a, 2))
# print('Repeat: ', np.repeat(a, 2))

# One random number between [0,1)
# one_random_num = np.random.random()
# one_random_in = np.random
# print(one_random_num)
# # Random numbers between [0,1) of shape 2,3
# r = np.random.random(size=[2,3])
# print(r)

# print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
## Random numbers between [0, 1] of shape 2, 2
# rand = np.random.rand(2,2)
# print(rand)
# rand2 = np.random.randn(2,2)
# print(rand2)

""" from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
print(np_normal_dis)
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))


plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()
plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()
 """


# 线性代数
# 点积
## 线性代数
# ### 点积：两个数组的乘积
# f = np.array([1,2,3])
# g = np.array([4,5,3])
# ### 1*4 + 2*5 + 3*6
# np.dot(f, g)  # 23

# print(np.dot(f, g))


# ### Matmul：两个数组的矩阵乘积
# h = [[1,2],[3,4]]
# i = [[5,6],[7,8]]
# ### 1*5+2*7 = 19
# #   1*6 + 2*8
# #   3*5 + 4*7
# #   3*6 + 4*8

# print(np.matmul(h, i))

# d = np.linalg.det(i)
# print(d)


# Z = np.zeros((8,8))
# print(Z)
# Z[1::2,::2] = 1
# Z[::2,1::2] = 1
# print(Z)

# new_list = [ x + 2 for x in range(0, 11)]


# temp = np.array([1,2,3,4,5])
# pressure = temp * 2 + 5
# pressure


# plt.plot(temp, pressure)
# plt.xlabel('Temperature in oC')
# plt.ylabel('Pressure in atm')
# plt.title('Temperature vs Pressure')
# plt.xticks(np.arange(0, 6, step=0.5))
# plt.show()


mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()



