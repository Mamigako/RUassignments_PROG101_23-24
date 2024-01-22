#import math module.
import math

#Ask for inpput values.
a_str = input() # Do not change this line.
b_str = input() # Do not change this line.
c_str = input() # Do not change this line.

#changes value types from sting to integer.
a_int = int(a_str)
b_int = int(b_str)
c_int = int(c_str)

#define and assign s.
s = (a_int + b_int + c_int) / 2
#define and assign area of triangle.
area = math.sqrt((s*(s - a_int)*(s - b_int)*(s - c_int)))
#print area rounded to 9 decimal points.
print(round(area, 9))