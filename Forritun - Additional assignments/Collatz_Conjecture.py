# Ask for input and convert to integer.
x = int(input()) # Do not change this line
# Print initial input
print(x)
# While x is not equal to 1, run loop.
while x != 1:
    # If x is even, divide it by 2 and print.
    if x % 2 == 0:
        x = x/2
        print(int(x))
    # If x is odd, apply formula and print.
    elif x % 2 != 0:
        x= 3*x+1
        print(int(x))
