# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 21:37:30 2022

@author: GYu
"""


# Define `plus()` function
def plus(a,b):
    c = a + b
    return c


# Call `plus()` with `a` and `b` parameters
a = 1
b = 3
result = plus(a, b)

print(result)

def my_list(item):
  for x in item:
    print(x)

def my_numbers(item):
   for x in item:
        if x < 10:
            print(x)
        else:
            print(x + 1)

fruits = ["apple", "banana", "cherry", "orange", "strawberry"]
cities = ["NYC", "DC", "Lansing", "San Francisco"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
url_1 = 'https://weather.com/weather/tenday/l/USDC0001'
url_2 = 'https://weather.com/weather/tenday/l/USCA0987'
url_3 = 'https://weather.com/weather/tenday/l/96f2f84af9a5f5d452eb0574d4e4d8a840c71b05e22264ebdc0056433a642c84' 
url_4 = 'https://weather.com/weather/tenday/l/a0c7694d6c51e53bcf16e4259855a5db57dbcf729423678e8b7711125045f750' 
url = [url_1, url_2, url_3, url_4]

# my_list(fruits)
# my_list(cities)
# my_numbers(numbers)
# my_list(url)