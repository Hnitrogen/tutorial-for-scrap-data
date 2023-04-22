from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import sys 
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


# sys.exit() 

turn = 1 
for url in urls:
    driver.get(url)
    time.sleep(2)

    tr_tags = driver.find_elements(By.TAG_NAME,'tr')
    time.sleep(1)
    for tr_tag in tr_tags:
        cells = tr_tag.find_elements(By.TAG_NAME,'td')
        
        for cell in cells: 
            filter_str = cell.text 
            filter_str = filter_str.strip()
            with open('table_final.csv','a') as f: 
                f.write(filter_str + '\t')
        
        with open('table_final.csv','a') as f: 
            f.write('\n')
    
    print("Scrap in turn: %d" % turn) 
    turn += 1 