from selenium import webdriver 
from selenium.webdriver.common.by import By

import time 
from fake_useragent import UserAgent

options = webdriver.ChromeOptions()
options.add_argument('--headless')
user_agent = UserAgent().random
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=options)

url = 'https://www.bilibili.com/v/popular/rank/guochuang' 
driver.get(url) 

time.sleep(10) 
divs = driver.find_elements("css selector","div.content") 

with open('bil.csv','a') as f: 
    input = "视频标题" + "\t" + "up主" + "\t" + "播放数" + "\t" + "弹幕数" + "\t" 
    f.write(input+'\n') 

turn = 1 
for i in divs : 
    time.sleep(1)
    ele_title = i.find_element("css selector","a.title") 
    title = ele_title.text 

    ele_up = i.find_element("css selector","span.up-name") 
    up = ele_up.text 

    ele_data = i.find_elements("css selector","span.data-box") 
    
    played_times = ele_data[1].text 
    barrage = ele_data[2].text 

    print("Active in turn %d" %turn) 
    turn += 1 

    input = title + "\t" + up + "\t" + played_times + "\t" + barrage + "\t" 
    with open('bil.csv','a') as f : 
        f.write(input + '\n') 
    
