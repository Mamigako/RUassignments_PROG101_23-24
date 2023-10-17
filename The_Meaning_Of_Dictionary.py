def main():
    dictionary = {}

    add_word(dictionary)
    while more():
        add_word(dictionary)

    display_result(dictionary)


def add_word(dictionary: dict) -> None:
    """Asks the user for a word and definition and stores it in the dictionary."""
    ask_word = input()
    ask_definition = input() 
    dictionary[ask_word] = ask_definition



def more() -> bool:
    """Checks if the user wants to add more words."""
    continue_y_or_n = input()
    if continue_y_or_n == "n":
        return False
    else:
        return True



def display_result(dictionary: dict) -> None:
    """Prints the words in alphabetical order, along with the definitions."""
    for key in sorted(dictionary):
        print("\n"+ key + ":")
        print("    " + dictionary[key])



if __name__ == "__main__":
    main()
