# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 12:40:53 2022

@author: GYu
"""

# this is a sample dictionary
my_dict = {'a': 20, 'b': 17, 'c': 35, 5: 'd'}

# print only the keys from my_dict
list(my_dict.keys())
print(list(my_dict.keys()))

# print only the values from my_dict
list(my_dict.values())
print(list(my_dict.values()))

# print the items from my_dict
list(my_dict.items())
print(list(my_dict.items()))

# print 
my_dict['a'] = 5000
my_dict['b'] = 2000
my_dict['c'] = 1000
my_dict['d'] = 900
my_dict
print(my_dict)

del my_dict['c']
print(my_dict)

my_dict.pop('a')

my_dict