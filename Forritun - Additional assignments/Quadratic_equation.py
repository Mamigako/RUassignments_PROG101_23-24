#ask for input, convert it to int and assign to 3 variables a,b,c
val_a_int = int(input())
val_b_int = int(input())
val_c_int = int(input())
# define formula for discriminant includiing the input variables.
discriminant = val_b_int**2 - 4*(val_a_int*val_c_int)
# If the discriminant is greater than 0, the quad equation has 2 solutions.
if discriminant > 0:
    print(2)
# If it is equal to 0, there is 1 solution
elif discriminant == 0:
    print(1)
# Otherwise(less than 0) it has 0 solutions.
else:
    print(0)