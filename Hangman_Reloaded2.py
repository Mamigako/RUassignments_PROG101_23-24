try:
    text_file = input()
    decision_int = int(input())
except ValueError:
    None
except NameError:
    None

# generate word list.
def open_and_list(text_file):
    
    word_list = []

    with open(text_file, "r") as file:
        
        for line in file:
            word_list.append(line.strip())
        
        return word_list

# Extract word.
def choose_word(word_list):
    secret_word_list = []

    for word in word_list[decision_int-1]:
    
        for letter in word:
            secret_word_list.append(letter)    
    
    return secret_word_list

# Encode word.
def make_hyphen_word(secret_word_list):
    hyphen_word_list = []

    for element in secret_word_list:
        hyphen_word_list.append("-")
    
    return hyphen_word_list

# Gameplay loop.
def play(hyphen_word_list, secret_word_list):
    
    count = 1


    while hyphen_word_list != secret_word_list:
        
        print(f"Secret word: {' '.join(hyphen_word_list)}")
        print(f"Guess {count}/12")
        
        good_guess = False
        
        guess_letter = input()
        

        for i in range(len(secret_word_list)):

            if guess_letter == secret_word_list[i]:
                hyphen_word_list[i] = guess_letter
                good_guess = guess_letter
    

        if good_guess:
            print(f"Correct letter {guess_letter}!")
        else: 
            print(f"Incorrect letter {guess_letter}!")


        if hyphen_word_list == secret_word_list:
            break
        elif count == 12:
            break
    
        count += 1
    
    if hyphen_word_list == secret_word_list:

        print(f"Secret word: {' '.join(hyphen_word_list)}")
        print("You won!")
    
    else:
        print(f"Secret word: {' '.join(hyphen_word_list)}")
        print(f"You lost! The secret word was {''.join(secret_word_list)}")


def main(text_file, decision_int):
    try:
        word_list = open_and_list(text_file)
    except FileNotFoundError:
        None

    secret_word_list = choose_word(word_list)

    hyphen_word_list = make_hyphen_word(secret_word_list)



    play(hyphen_word_list, secret_word_list)

try:
    main(text_file, decision_int)
except NameError:
    None
except ValueError:
    None
except FileNotFoundError:
    None
