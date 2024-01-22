# ask for rating and convert to int.
rating = int(input()) # Do not change this line.

# if rating more or equal to 2700, super GM
if rating >= 2700:
    print("Super grandmaster")

# if rating more or equal to 2500, GM
elif rating >= 2500:
    print("Grandmaster")

# if rating more or equal to 2400, IGM
elif rating >= 2400:
    print("International Grandmaster")

# if rating between 1000 and 2399, amateur
elif 999 < rating < 2400: 
    print("Amateur")
    
# under 1000 return invalid.
elif rating <= 999:
    print("Invalid")
