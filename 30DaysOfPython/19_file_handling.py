print('19_file_handling')

""" 
文件处理
到目前为止，我们已经看到了不同的 Python 数据类型。我们通常以不同的文件格式存储我们的数据。除了处理文件之外，我们还将在本节中看到不同的文件格式（.txt、.json、.xml、.csv、.tsv、.excel）。
首先，让我们熟悉处理具有通用文件格式 (.txt) 的文件。

文件处理是编程的重要组成部分，它允许我们创建、读取、更新和删除文件。
在 python 中，我们使用open()内置函数来处理数据。

# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

“r” - 读取 - 默认值。打开一个文件进行读取，如果文件不存在则报错
"a" - Append - 打开一个文件进行追加，如果文件不存在则创建该文件
"w" - 写入 - 打开一个文件进行写入，如果文件不存在则创建该文件
"x" - Create - 创建指定的文件，如果文件存在则返回错误
“t” - 文本 - 默认值。文本模式
“b” - 二进制 - 二进制模式（例如图像）

"""

""" 
打开的默认模式是读取，因此我们不必指定 'r' 或 'rt'。
我在文件目录中创建并保存了一个名为 reading_file_example.txt 的文件。让我们看看它是如何完成的：

"""

# f = open('./files/reading_file_example.txt')
# print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

""" f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close() 
"""

""" f = open('./files/reading_file_example.txt')
line = f.read().splitlines()
print(type(line))
print(line)
f.close()
 """
# with open('./files/reading_file_example.txt') as f:
#     lines = f.read().splitlines()
#     print(type(lines))
#     print(lines)


# 打开文件进行写入和更新
# 要写入现有文件，我们必须向open()函数添加一个模式作为参数：

# “a” - 追加 - 将追加到文件的末尾，如果文件不存在，则会引发 FileNotFoundError。
# "w" - 写入 - 将覆盖任何现有内容，如果它创建的文件不存在。
# 让我们将一些文本附加到我们一直在阅读的文件中：

# with open('./files/reading_file_example.txt', 'a') as f:
#     f.write('This text has to be append as the end')

# with open('./files/writing_file_examsple.txt','a') as f:
#     f.write('This text has to be appended at the end')


import os

# os.remove('./files/writing_file_examsple.txt')

import os
# if os.path.exist('./files/example.txt'):
#     os.remove('./files/example.txt')
# else:
#     os.remove('The file does not exist')

# if os.path.exists('./files/writing_file_example.txt'):
#     os.remove('./files/writing_file_example.txt')
# else:
#     print('not exist')

# 带有 json 扩展名的文件
# JSON 代表 JavaScript 对象表示法。实际上，它是一个字符串化的 JavaScript 对象。
# import json
# # JSON
# person_json = '''{
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }'''
# # let's change JSON to dictionary
# person_dct = json.loads(person_json)
# print(person_dct)
# print(person_dct['name'])

# import json

""" person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
person_dct = json.loads(person_json)
print(person_dct)
print(person_dct['name'])
 """

""" import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# with open('./files/json_example.json', 'w', encoding='utf-8') as f:
#     json.dump(person, f, ensure_ascii=False, indent=4)

with open('./files/reading_file_example.txt', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

 """


#  带有 csv 扩展名的文件
# CSV 代表逗号分隔值。CSV 是一种简单的文件格式，用于存储表格数据，例如电子表格或数据库。CSV 是数据科学中非常常见的数据格式。



# import csv
# with open('./files/csv_example.csv') as f:
#     csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are :{", ".join(row)}')
#             line_count += 1
#         else:
#             print(
#                 f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
#             line_count += 1
#     print(f'Number of lines:  {line_count}')

# import csv

# if os.path.exists('./files/csv_example.csv'):

#     with open('./files/csv_example.csv') as f:
#         csv_reader = csv.reader(f, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column name are:{", ".join(row)}')
#                 line_count += 1
#             else:
#                 print(f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
#                 line_count += 1
        
#         print(f'Number of lines: {line_count}')

# else:
#     print('file not exists')

# 带有 xlsx 扩展名的文件
# 要读取 excel 文件，我们需要安装xlrd包。我们将在介绍使用 pip 安装软件包后介绍这一点。

# import xml.etree.ElementTree as ET
# tree = ET.parse('./files/xml_example.xml')
# root = tree.getroot()
# print('Root tag:', root.tag)
# print('Attribute:', root.attrib)
# for child in root:
#     print('field: ', child.tag)







