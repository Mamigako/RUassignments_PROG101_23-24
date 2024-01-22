#Ask for number.
num_int = int(input())

#if input number is lower than -1000, print error.
if  num_int < -1000:
     print("Error:Number out of range")

#if input number is higher than -1000, print error.
elif num_int > 1000:
     print("Error:Number out of range")

#only if abovementioned criteria are not met:
else:
     
#add 5, multiply by 3 and subtract 10 from num_int and assign to result_int.
     result_int = ((num_int + 5) * 3 ) - 10

#Print result.
print(result_int)
