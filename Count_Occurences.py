a_str = input()
char_to_count = input()
count = -1
 
# loop through the string to find the instances of the letter and print their index.

for char in a_str:
    count += 1
    if char_to_count == char:
        print(count)
