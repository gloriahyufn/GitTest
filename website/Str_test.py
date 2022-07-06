# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:06:11 2022

@author: GYu
"""



bill_text = 'SB2001'

#prefix = ""
for char in bill_text:
   if char.isalpha():
      prefix = char
#      print(prefix)
#   if a.isdigit():
#      number = a
#      print(number)
      #print(prefix + ' ' + number)
#      b = prefix + ' ' + number     
      
      

string = 'SB2001'

only_alpha = ""

## looping through the string to find out alphabets

        
alpha  = ''.join(filter(lambda i: i.isalpha(), string))
print(alpha)        
number = ''.join(filter(lambda i: i.isdigit(), string))
print(number)

bill = alpha +' ' + number
print(bill)