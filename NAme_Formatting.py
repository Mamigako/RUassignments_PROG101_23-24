name = input()

last_name = name[:(name.find(","))]
first_name = name[(name.find(",") + 2):]

first_name = first_name[0].upper() + ". "
last_name = last_name[0].upper() + last_name[1:]

print(first_name + last_name)
