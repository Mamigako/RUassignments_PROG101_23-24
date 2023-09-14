stop_range = int(input())
n_num = 0
j_num = 1


# Calculate geometric sequence, output sum of all numbers generated including present line. 


for i in range(1, stop_range + 1):
    i = (j_num * 0.5) + n_num
    j_num = j_num * 0.5
    n_num = i
    print(n_num)
