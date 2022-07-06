# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 18:12:42 2021

@author: GYu
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://www.python.org")
# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()







