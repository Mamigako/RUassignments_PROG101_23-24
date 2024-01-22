# Import module.
import math
#ask for d and change type to float.
d = float(input())

#define and assign the radius
radius_of_sphere = d/2
#define and assign the volume of a whole sphere.
volume_of_sphere = (4/3)*math.pi*(radius_of_sphere**3)
#define and assign the volume of half a sphere.
volume_of_half_sphere = volume_of_sphere/2
#print volume of half sphere, rounded to 9 decimal points.
print(round(volume_of_half_sphere, 9))
