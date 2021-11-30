# Python program to print Positive Numbers in a List
 
# list of numbers
list1 = [12, -7, 5, 64, -14]
print("Input::  ", list1)
# using list comprehension
pos_nos1 = [num for num in list1 if num >= 0]
 
print("Output:  ", *pos_nos1)

list2 = [12, 14, -95, 3]
print("Input::  ", list2)
# using list comprehension
pos_nos2 = [num for num in list2 if num >= 0]
 
print("Output:  ", *pos_nos2)
