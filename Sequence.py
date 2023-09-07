n = int(input())  # Do not change this line

# Initiate variables.
x = 0
y = 0
z = 0
temp = 0

# loop through range, print 1,2,3.
for i in range(1, n+1):
    if i == 1:
        x = i
        temp = i
    elif i == 2:
        y = i
        temp = i
    elif i == 3:
        z = i
        temp = i
    # After 3rd number in range, sum the first 3 numbers, assign 2nd to 1st, 3rd to 2nd, and temp(p) to 3rd.
    # Also print temp variable, which is the sum of the last 3 numbers.
    else:
        temp = x + y + z
        x = y
        y = z
        z = temp
    print(temp)        


     
     
