# Ask for number and convert to int.
number = int(input()) # Do not change this line
no_7_found_yet = True
# While number is higher than 0, initiate loop.
while number > 0:
    # assign the remainder of the number after modulo 10.
    remainder = number % 10
    # If the remainder is 7, the number contains 7.
    if remainder == 7:
        no_7_found_yet = False
        break
    # Divide number by 10
    number = number // 10
# If variable True, nr. does not contain 7.    
if no_7_found_yet:
    print("The number does not contain 7.")
# Else it does contain 7.
else:
    print("The number contains 7.")
