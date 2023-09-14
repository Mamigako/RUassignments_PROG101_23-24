a_str = input() 
new_string = ""
 
 # append all characters whose index is even to the new list and print.

for char in range(len(a_str)):
    if char  % 2 == 0:
        new_string += a_str[char]


print(new_string)
    