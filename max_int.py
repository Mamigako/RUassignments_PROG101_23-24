# Initiate the variables, and ask for input. Save input.
num_int = int(input())
list_num = []

# loop while input is equal to or larger than 0, keep appending each input to list.
while num_int >= 0:
    list_num.append(num_int)
    num_int = int(input()) 

# Once input falls below 0, print maximum value in list, which is the highest value.
max_int = max(list_num)
print(max_int)
