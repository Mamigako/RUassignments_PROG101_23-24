#ask for input, convert to int and assign to num1,2,3
num1 = int(input()) # Do not change this line
num2 = int(input()) # Do not change this line
num3 = int(input()) # Do not change this line

#designate num1 as the maximum if it is greater than the other two.
if num1 > num2 and num1 > num3:
    max_int = num1

#designate num2 as the maximum if it is greater than the other two.
elif num2 > num1 and num2 > num3:
    max_int = num2 

#otherwise designate num3 as maximum
elif num3 > num1 and num3 > num2:
    max_int= num3

#print maximium
print(max_int) # Do not change this line
