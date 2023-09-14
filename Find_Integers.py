stop_range = int(input())
num_divisors = int(input())



# loop through range and split number into both decimal parts, then add them together.
for i in range(10, stop_range):
    num1 = int(i / 10)
    num2 = i - (num1 * 10)
    num3 = num1 + num2
    if (num3 ** 2) == i:
        print(i)



# Find divisors for every number j in range k.
# If divisor, add 1 to x, if x equals input at end of loop, print k.
for k in range(1,stop_range):
    x = 0
    for j in range(1, k + 1):
        if k % j == 0:
            x += 1
    if x == num_divisors:
        print(k)
