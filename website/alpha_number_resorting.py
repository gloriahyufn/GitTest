# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 08:25:03 2021

@author: GYu
"""



a = ['HB', '1', 'HB', '2', 'SB', '1', 'SB', '2', 'SJ', '1', 'SJ', '2']

alpha = []
for item in a:
    for subitem in item.split():
        if(subitem.isalpha()):
            alpha.append(subitem)
print(alpha)

numbers = []
for item in a:
    for subitem in item.split():
        if(subitem.isdigit()):
            numbers.append(subitem)
print(numbers)

b = []
for i in range(0, len(alpha)):
    b.append(alpha[i] + ' ' + numbers[i])
print(b)