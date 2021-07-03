print('22_web_scraping')
""" 
什么是网页抓取
    
    互联网充满了可用于不同目的的大量数据。为了收集这些数据，我们需要知道如何从网站上抓取数据。
    网页抓取是从网站中提取和收集数据并将其存储在本地机器或数据库中的过程。
    在本节中，我们将使用 beautifulsoup 和 requests 包来抓取数据。我们使用的包版本是beautifulsoup 4。

    要开始抓取网站，您需要requests、beautifoulSoup4和website。

    pip install requests
    pip install beautifulsoup4

要从网站抓取数据，需要对 HTML 标签和 css 选择器有基本的了解。我们使用 HTML 标签、类或/和 ID 定位来自网站的内容。让我们导入请求和 BeautifulSoup 模块

import requests
from bs4 import BeautifulSoup

让我们为要抓取的网站声明 url 变量。



 """

import requests
from bs4 import BeautifulSoup

url = 'http://mlr.cs.umass.edu/ml/datasets.html'
response = requests.get(url)
status = response.status_code
print(status)

import requests
from bs4 import BeautifulSoup
url = 'http://mlr.cs.umass.edu/ml/datasets.html'

response = requests.get(url)
content = response.content # we get all the content from the website
# soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
# print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
# print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
# print(soup.body) # gives the whole page on the website
# print(response.status_code)

# tables = soup.find_all('table', {'cellpadding':'3'})
# # We are targeting the table with cellpadding attribute with the value of 3
# # We can select using id, class or HTML tag , for more information check the beautifulsoup doc
# table = tables[0] # the result is a list, we are taking out data from it
# for td in table.find('tr').find_all('td'):
#     print(td.text)

soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)

tables = soup.find_all('table', {'cellpading':'3'})
table = tables[0]
for td in table.find('tr').find_all('td'):
    print(td.text)
# 提取此 url ( http://mlr.cs.umass.edu/ml/datasets.html ) 中的表并将其更改为 json 文件
# 抓取总统表并将数据存储为 json( https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States )