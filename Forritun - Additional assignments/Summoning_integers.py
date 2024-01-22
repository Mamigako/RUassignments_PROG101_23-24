# assign 2 empty variables for the loop.
num = 0
num2 = 0
# While the input number is not 10 exactly, run loop.
while num != 10:  
    # add num to num2
    num2 += num 
    # ask for new value for num
    num = int(input())
# if num equals 10, print num2
else:
    print(num2)
