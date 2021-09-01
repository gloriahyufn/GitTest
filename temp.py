# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# this is a sample dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 5: 'd'}

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
my_dict['a'] = 1337
my_dict['b'] = 1500
my_dict['c'] = 34
my_dict['d'] = 1
my_dict
print(my_dict)

del my_dict['b']
print(my_dict)

my_dict.pop('c')

my_dict

# prints the length of list my_dict
len(my_dict)
print(len(my_dict))

# Special: Ordered Dict

from collections import OrderedDict

ordered_dict = OrderedDict(a=1, b=2, c=3)
regular_dict = dict(a=1, b=2, c=3)
ordered_dict[1] = 4
regular_dict[1] = 4

print(ordered_dict)

regular_dict
print(regular_dict)

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

# Conditions Example 3
    
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two. x equals : ", x)

# Test if a variable is NOT in a list
    
name = 'Dan'
if name not in ['Dan', 'Brian', 'Sergiy', 'Natalia', 'Garrett']:
    print("Name Not Found")
else:
    print("Name Found")

# If there are more than two possibilities and we need more than two branches
    
choice = input("Enter in your choice: ")

if choice == 'a':
    print("You chose 'a'.")
elif choice == 'b':
    print("You chose 'b".")
elif choice == 'c':
    print("You chose 'c'.")
else: 
    print("Invalid choice.")


















