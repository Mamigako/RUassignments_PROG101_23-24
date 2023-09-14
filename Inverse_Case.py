a_str = input()
new_string = ""

for char in a_str:
    if char.upper() == char:
     new_string += char.lower()
    else:
      new_string += char.upper()

print(new_string)