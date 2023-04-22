from bs4 import BeautifulSoup
import requests
import time 

url = 'http://quotes.toscrape.com/page/'
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
