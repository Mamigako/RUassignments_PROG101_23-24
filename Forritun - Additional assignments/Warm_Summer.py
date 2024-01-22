# ask for answer and store it in a variable.
answer = input("You need something doubled? (Y)es? \n")
# While answer is yes, loop through.
while answer == "Y":
    # Ask for number to multiply.
    number = float(input("All right, then. Give me a number, and I'll double it for ya: \n"))
    # Multiply the number
    multinum = number*2
    # Print the number.
    print(multinum)
    # Ask again 
    answer = input("You need something else doubled? (Y)es? \n")
