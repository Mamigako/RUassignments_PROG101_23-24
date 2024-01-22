k = int(input())
n = int(input())
# Initialise the sum variable.
the_sum = 0

# Loop through range of n, asking for int to power k with
for i in range(n):
    power = int(input())
    # Add k to the power of power to sum.
    the_sum += k**power

# Print result.
print(the_sum)