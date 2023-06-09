# tutorial-for-scrap-data


开源数据集   dataset

以下是一些公开的数据集，可以供您使用：
```
1. Kaggle：Kaggle是一个数据科学社区，提供各种数据集，包括图像、文本、时间序列、自然语言处理和机器学习数据集等。

2. UCI Machine Learning Repository：UCI Machine Learning Repository是一个受欢迎的机器学习数据集资源库，提供了各种数据集，包括分类、回归、聚类、网络、时间序列等。

3. 数据普惠：数据普惠是由中国人民大学数字金融研究院推出的一个公益性数据开放平台，提供了各种公开数据集，包括金融、医疗、教育、环境、交通等。

4. 数据.gov：数据.gov是美国政府提供的一个开放数据平台，提供了各种政府数据集，包括人口、气象、能源、交通、农业、工业等。

5. Google Dataset Search：Google Dataset Search是由Google推出的一个数据集搜索引擎，可以帮助用户找到各种公开的数据集。

6. Amazon Web Services (AWS) Public Datasets：AWS Public Datasets是由亚马逊公司提供的一个公开数据集平台，提供了各种领域的数据集，包括气象、生物学、地理信息、金融等。

7. 美国人口普查局：美国人口普查局提供了各种人口统计数据，包括人口、家庭、教育、就业、收入等。

8. 欧盟开放数据门户：欧盟开放数据门户提供了各种公开数据集，包括环境、经济、社会、交通、健康、科技等。
```
以上是一些公开的数据集，您可以根据自己的需求选择合适的数据集。需要注意的是，一些数据集可能有使用限制或需要付费获取，您在使用之前需要仔细了解相关条款和条件。


以下是一些中国公开的数据集，可以供您使用：
```
1. 国家数据：国家数据是由国家统计局提供的一个公开数据平台，包括人口、经济、环境、社会等各个方面的数据。

2. 中国气象数据网：中国气象数据网是由中国气象局提供的一个气象数据平台，包括天气、气候、气象灾害等数据。

3. 数据普惠：数据普惠是由中国人民大学数字金融研究院推出的一个公益性数据开放平台，提供了各种公开数据集，如金融、医疗、教育、环境、交通等。

4. 中国科学数据：中国科学数据是由中国科学院提供的一个科学数据平台，包括天文、生物、地球、环境、材料等各个领域的数据。

5. 国家卫生健康委员会：国家卫生健康委员会提供了各种医疗卫生数据集，包括疾病、医疗资源、卫生人员等。

6. 中国地震局：中国地震局提供了各种地震数据集，包括地震目录、地震参数、地震预警等。

7. 中国铁路客户服务中心：中国铁路客户服务中心提供了各种铁路运输数据集，包括列车时刻、车站信息、票务信息等。

8. 中国知网：中国知网是一个学术文献检索平台，提供了各种学术论文、期刊、会议等数据集。
```

以上是一些中国公开的数据集，您可以根据自己的需求选择合适的数据集。需要注意的是，一些数据集可能有使用限制或需要付费获取，您在使用之前需要仔细了解相关条款和条件。


暴力 — 用纸和笔记录

爬虫 — 优化记录和输入


# bs4 parse html 
#### 推荐是搭建虚拟环境
```
python3 venv -m scrapy 

source ./scrapy/bin/activate

pip install beautifulsoup4
- i https://pypi.tuna.tsinghua.edu.cn/simple
```
#### 尝试爬取一些静态页面
```              
http://quotes.toscrape.com/page/3/  // 查看他的网页源代码 --- 非常的静态
```

code: 
```
from bs4 import BeautifulSoup
import requests
import time 

url = 'http://quotes.toscrape.com/page/'    # 记得检验路由的正确性
urls = [] 
for i in range(1,10): 
    comp = url + str(i) + '/' 
    urls.append(comp)

for detail in urls:
    print(detail)
    response = requests.get(detail)
    html_doc = response.content

    soup = BeautifulSoup(html_doc,'html.parser')
    spans = soup.find_all('span',class_='text')
    time.sleep(1)

    with open('shaguai','a') as f: 
        for span in spans: 
            f.write(span.text + '\n' + '\n') 

```
# Selenium args 

## webdriver 
112.0.5615.137
```
在Selenium 4中，find_elements_by方法的参数可以是以下选项：

1. By.ID：根据元素的id属性查找元素。例如：driver.find_elements(By.ID, 'element_id')。

2. By.NAME：根据元素的name属性查找元素。例如：driver.find_elements(By.NAME, 'element_name')。

3. By.CLASS_NAME：根据元素的class属性查找元素。例如：driver.find_elements(By.CLASS_NAME, 'element_class')。

4. By.TAG_NAME：根据元素的标签名查找元素。例如：driver.find_elements(By.TAG_NAME, 'element_tag')。

5. By.LINK_TEXT：根据链接文本查找元素。例如：driver.find_elements(By.LINK_TEXT, 'link_text')。

6. By.PARTIAL_LINK_TEXT：根据链接文本的部分内容查找元素。例如：driver.find_elements(By.PARTIAL_LINK_TEXT, 'partial_link_text')。

7. By.CSS_SELECTOR：根据CSS选择器查找元素。例如：driver.find_elements(By.CSS_SELECTOR, 'css_selector')。

8. By.XPATH：根据XPath表达式查找元素。例如：driver.find_elements(By.XPATH, 'xpath_expression')。

需要注意的是，find_elements_by方法返回的是一个列表，包含所有符合条件的元素，如果没有找到符合条件的元素，则返回一个空的列表。在使用find_elements_by方法查找元素时，需要根据实际情况选择合适的查找方法和参数，以保证能够准确地找到目标元素。
```
# Selenium
爬个lc周赛数据玩玩，之前爬800个就被封了乐

- 记得先在本地手模一个静态的玩玩 --- 网络延迟 / 防止被封ip 
```
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from fake_useragent import UserAgent

options = webdriver.ChromeOptions()
options.add_argument('--headless')
user_agent = UserAgent().random
options.add_argument(f'user-agent={user_agent}')


driver = webdriver.Chrome(options=options)
# driver.get('file:///Users/hnitro/Desktop/scrap/lc/nicai.html')
url = 'https://leetcode.cn/contest/weekly-contest-341/ranking/' 
urls = [] 
for i in range(1,191):
    urls.append(url+str(i)+'/')
    print(url+str(i)+'/')

for url in urls:
    driver.get(url)
    time.sleep(1)

    tr_tags = driver.find_elements(By.TAG_NAME,'tr')
    for tr_tag in tr_tags:
        cells = tr_tag.find_elements(By.TAG_NAME,'td')
        
        for cell in cells: 
            filter_str = cell.text 
            filter_str = filter_str.strip()
            with open('table_final.csv','a') as f: 
                f.write(filter_str + "      ")
        
        with open('table_final.csv','a') as f: 
            f.write('\n')

    print("Actually in!")
```

# 分布式爬取 / 亚马逊云服务器hhh
