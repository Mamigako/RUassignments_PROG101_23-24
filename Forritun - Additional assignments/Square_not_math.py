# Ask dor input.
size = int(input())

# loop through input range.
for i in range(size):
    # Nested loop to print asterisk or space depending on condition.
    for j in range(size):
        if i == 0 or i == size-1 or j == 0 or j == size-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    # Print lines
    print()
