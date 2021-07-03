print('20_python_package_manager')
""" 
PIP 代表首选安装程序。我们使用pip来安装不同的python包。包是一个python模块，可以包含一个或多个模块或其他包。我们可以安装到应用程序的一个或多个模块是一个包。在编程中，我们不必编写每个实用程序，而是安装包并将它们导入到我们的应用程序中。

 """

""" 
 安装
 curl https://bootstrap.pypa.io/get-pip.py | python3
 查看
 pip --version
 查看相对应的包
 pip3 list

安装和更新  pip
 pip install --upgrade pip

"""

# 让我们尝试安装numpy，称为 numeric python。
# 它是机器学习和数据科学社区中最受欢迎的软件包之一。

# NumPy 是使用 Python 进行科学计算的基础包。其中包括：
#     一个强大的 N 维数组对象
#     复杂的（广播）功能
#     用于集成 C/C++ 和 Fortran 代码的工具
#     有用的线性代数、傅立叶变换和随机数功能å
# import webbrowser # web browser module to open websites

# # list of urls: python
# url_lists = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/asabeneh/',
#     'https://twitter.com/Asabeneh',
#     'https://twitter.com/Asabeneh',
# ]

# # opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)

# import webbrowser
# url_lists = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/asabeneh/',
#     'https://twitter.com/Asabeneh',
#     'https://twitter.com/Asabeneh',
# ]
# for url in url_lists:
#     webbrowser.open_new_tab(url)


# 我们将在requests模块中看到get、status_code、headers、text和json方法：

# get()：打开网络并从 url 获取数据 - 它返回一个响应对象
# status_code：获取数据后，我们可以检查操作的状态（成功、错误等）
# headers : 检查标题类型
# text : 从获取的响应对象中提取文本
# json : 提取json数据让我们从这个网站上读取一个txt文件，https://www.w3.org/TR/PNG/iso_8859-1.txt。

# import requests # importing the request module

# url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

# response = requests.get(url) # opening a network and fetching a data
# print(response)
# print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# print(response.text) # gives all the text from the page

""" import requests
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
# url = 'http://47.103.129.42:8095/v4/user/level_point'
response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
print(response.text)
 """
# 让我们从 api 中读取。
# API 代表应用程序接口。
# 它是一种在服务器之间交换结构数据的手段，主要是 json 数据。
# 一个 api 示例：https : //restcountries.eu/rest/v2/all。让我们使用requests模块阅读这个 API 。

import requests
url = 'https://restcountries.eu/rest/v2/all'  # countries api
# response = requests.get(url)  # opening a network and fetching a data
# print(response) # response object
# print(response.status_code)  # status code, success:200
# countries = response.json()
# print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries


# 我们根据一些标准将大量文件组织在不同的文件夹和子文件夹中，以便我们可以轻松地查找和管理它们。
#   如您所知，一个模块可以包含多个对象，例如类、函数等。
#   一个包可以包含一个或多个相关模块。
#   一个包实际上是一个包含一个或多个模块文件的文件夹。
#   让我们使用以下步骤创建一个名为 mypackage 的包：

    # 在 30DaysOfPython 文件夹中创建一个名为 mypacakge 的新文件夹在 mypackage 文件夹中创建一个空的init .py 文件。使用以下代码创建模块 algorithm.py 和 greet.py：



# 关于包的更多信息


""" 
关于包的更多信息
数据库

SQLAlchemy 或 SQLObject - 面向对象访问多个不同的数据库系统
pip 安装 SQLAlchemy

Web开发
    Django - 高级 Web 框架。
    pip 安装 django
Flask - 基于 Werkzeug、Jinja 2 的 Python 微框架。（它是 BSD 许可的）
    
    pip 安装烧瓶
HTML解析器

Beautiful Soup - 专为快速周转项目（如屏幕抓取）而设计的 HTML/XML 解析器，将接受不良标记。
pip 安装 beautifulsoup4
PyQuery - 在 Python 中实现 jQuery；显然比 BeautifulSoup 快。
XML处理

ElementTree - Element 类型是一个简单但灵活的容器对象，旨在在内存中存储分层数据结构，例如简化的 XML 信息集。--注意：Python 2.5 及更高版本在标准库中有 ElementTree
图形用户界面

PyQt - 跨平台 Qt 框架的绑定。
TkInter - 传统的 Python 用户界面工具包。
数据分析、数据科学和机器学习

Numpy：Numpy(numeric python) 被称为 Python 中最受欢迎的机器学习库之一。
Pandas：是 Python 中的机器学习库，提供高级数据结构和多种分析工具。
SciPy：SciPy 是一个面向应用程序开发人员和工程师的机器学习库。SciPy 库包含用于优化、线性代数、集成、图像处理和统计的模块。
Scikit-Learn：它是 NumPy 和 SciPy。它被认为是处理复杂数据的最佳库之一。
TensorFlow：是谷歌构建的机器学习库。
Keras：被认为是 Python 中最酷的机器学习库之一。它提供了一种更简单的机制来表达神经网络。Keras 还提供了一些用于编译模型、处理数据集、图形可视化等的最佳实用程序。
网络：

requests：是一个我们可以用来向服务器发送请求的包（GET、POST、DELETE、PUT）
pip 安装请求

"""

