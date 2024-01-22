#import math module.
import math

#ask for input.
x1_str = input() 
y1_str = input() 
x2_str = input() 
y2_str = input() 
# Convert values from strings to integers.
x1_int = int(x1_str)
y1_int = int(y1_str)
x2_int = int(x2_str)
y2_int = int(y2_str)

#if the numbers are lower than -10000, return error.
if x1_int < -10000 or x1_int > 10000:
    print("Error: x1 out of range")
if y1_int < -10000:
    print("Error: y1 out of range")
if x2_int < -10000:
    print("Error: x2 out of range")
if y2_int < -10000:
    print("Error: y2 out of range")


#if the numbers are higher than 10000, return error.
if x1_int > 10000:
    print("Error: x1 out of range")
if y1_int > 10000:
    print("Error: y1 out of range")
if x2_int > 10000:
    print("Error: x2 out of range")
if y2_int > 10000:
    print("Error: y2 out of range")

#otherwise, apply euclidean distance formula and return result.
else:
    d = math.sqrt((x2_int - x1_int)**2 + (y2_int - y1_int)**2)
    print(d)
