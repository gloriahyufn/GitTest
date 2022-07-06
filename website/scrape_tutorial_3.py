# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:42:47 2021

@author: GYu
"""



from selenium import webdriver
from bs4 import BeautifulSoup



# Python script
driver = webdriver.Chrome()
driver.get("https://weather.com/weather/today/l/0b4ccdd5d42119a4ae232ac047f9128283b48c412a50312e224c33a64565ba9d")
## t_url = "https://weather.com/weather/today/l/7ebb344012f0c5ff88820d763da89ed94306a86c770fda50c983bf01a0f55c0d"
## driver.get("<a href='" + t_url + "'>" + t_url + "</a>")
t_content = driver.page_source
soup_in_bowl = BeautifulSoup(t_content, 'html.parser')

## o_temp = soup_in_bowl.find('span', attrs={'class':'deg-feels'})
o_temp = soup_in_bowl.find('span', attrs={'class':'CurrentConditions--tempValue--3a50n'})
n_temp = o_temp.text

print (n_temp)

