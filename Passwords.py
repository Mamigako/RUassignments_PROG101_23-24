Min_lenght = 6
Max_lenght = 20
Quit_prompt = "q"
Count = 0
Valid_count = 0
Invalid_count = 0
Lower_index = 0
Upper_index = 0
Num_index = 0
password = input()



while password != Quit_prompt:
    Count += 1

    # Indices need to be reset every loopthrough.
    Lower_index = 0
    Upper_index = 0
    Num_index = 0

    # Using the character´s ord value to determine whether all password criteria have been met after evaluating the length.
    if Min_lenght <= len(password) <= Max_lenght:
        for char in password:
            if ord(char) in range(48, 58):
                Num_index = 1
            if ord(char) in range(65, 91):
                Upper_index = 1
            if ord(char) in range(97, 123):
                Lower_index = 1  


        if Lower_index == 0:
            print(f"{password}: Missing lower case letter.")
        if Upper_index == 0:
            print(f"{password}: Missing upper case letter.") 
        if Num_index == 0:
            print(f"{password}: Missing numeric letter.")
        if Lower_index and Upper_index and Num_index:
            Valid_count += 1
            print(f"{password}: Valid password of length {len(password)}.")
            password = input()
        else:
            password = input()


    else:
        print(f"{password}: Invalid length.")
        password = input()


Invalid_count = Count - Valid_count


print(f"You tried {Count} passwords, {Valid_count} valid, {Invalid_count} invalid.")


