# Data Structures
# Python program which accepts the radius of a circle from the user and computes area.Python program to print Positive Numbers in a List
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius  " + str(r) + " is: " + str(pi * r**2))

# Python program to accept a filename from the user and print the extension of that.

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
