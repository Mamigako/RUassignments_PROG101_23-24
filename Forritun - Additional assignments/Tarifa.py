# Ask for mb allotment, monnths used and initiate total mb left variable.
mb_per_month = int(input())
n = int(input())
total_mb_left = 0

# Loop through months used, ask for mb used and calculate mb left.
for i in range(n):
    d = int(input())
    mb_left = mb_per_month - d
    total_mb_left += mb_left
    # Add next month´s allotment to final result.
print(total_mb_left+mb_per_month) 