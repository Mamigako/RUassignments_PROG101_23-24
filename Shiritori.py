def main():
    word= input()
    word=word.lower()
    valid_words= [word]
    invalid_words= []
    
    while True:
        last_valid_word= valid_words[-1]
        word= input()
        word= word.lower()

        if word == "x":
            break

        if word[0] == last_valid_word[-1]:
            valid_words.append(word)
        
        else:
            invalid_words.append(word)

    if valid_words != ["x"]:
        for element in valid_words:
            print(element, end=" ")
    
    print()

    for element in invalid_words:
        print(element, end=" ")

if __name__ == "__main__":
    main()