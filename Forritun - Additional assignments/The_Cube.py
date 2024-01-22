#Ask for number.
num_int = int(input()) # Do not change this line.

#if input number is lower than -1000, print error.
if  num_int < -1000:
     print("Error:Number out of range")

#if input number is higher than -1000, print error.
elif num_int > 1000:
     print("Error:Number out of range")

#otherwise continue:
else:
#assign the input number cubed to variable cube.
     cube = num_int ** 3
#print cube
     print(cube)