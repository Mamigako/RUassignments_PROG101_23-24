import re

age_valid = False
name_valid = False

def main():
    global age_valid
    global name_valid
    
    while not name_valid:
        name = get_name()
    
    while not age_valid:
        age = get_age()
    
    print(f"Nice to meet you {name}. Congratulations on your {age} years.")

def get_name() -> str:
    global name_valid
    name = input("What's your name? ")
    if re.search("[^a-zA-Z\s]", name):
        print("Please enter a valid name.")
    elif name == "":
        print("Please enter a valid name.")
    else:
        name_valid = True
        return name

def get_age() -> str:
    global age_valid
    age = input("How old are you? ")
    if not re.search("[0-9]", age):
        print("Please enter an integer.")
    else:
        try:
            if int(age) < 0 or int(age) > 125:
                print(f"You seriously expect me to believe you are {age} years old?")
            else:
                age_valid = True
                return str(age)
        except ValueError:
            print("Please enter an integer.")


if __name__ == "__main__":
    main()
