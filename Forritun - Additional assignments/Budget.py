# Do not change the following 4 lines:
#ask for input, convert to int and assign budget and project values.
budget = int(input())
project1 = int(input())
project2 = int(input())
project3 = int(input())

#if sum of projects is equal to or less than the budget, it is sufficient.
if (project1 + project2 + project3) <= budget:
    print("Budget is sufficient.")
    
#otherwise it is insufficient.
else:
    print("Budget is insufficient.")
