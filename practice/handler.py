# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 12:42:00 2022

@author: GYu
"""

# 1.3.1 Control Structures - Conditions

name = 'Gloria'
if name in ['Dan', 'Brian', 'Sergiy', 'Natalia', 'Garrett']:
    print("Hey that's me!")
else:
    print("Hey that's not me!")

# Conditions Example 1

x = 2
y = 4
if x == 2 and y == x*x:
    print("y equals x*x")
    
# Conditions Example 2
    
x = 1
if x == 3 or x == 2:
    print("x equals either 2 or 4")
else:
    print("x is not equal to 2 or 4")