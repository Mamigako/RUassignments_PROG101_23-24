# Ask for input and convert to int.
year = int(input()) # Do not change this line

# If the year is divisible evenly by 4, go to next step, otherwise year is not a leap year.
if year % 4 == 0:
# If year is div evenly by 4 and by 100, continue, else it is a leap year.
    if year % 4 == 0 and year % 100 == 0:
        # if year is div evenly by 4, 100 and 400, it is a leap year. Otherwise it is not.
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            print(True)
        else:
            print(False) 
    else: 
        print(True)
else:
    print(False)
