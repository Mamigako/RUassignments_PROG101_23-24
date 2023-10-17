def main():

    sentence_1 = input()
    sentence_2 = input()

    if are_anagrams(sentence_1, sentence_2):
        print(f"{sentence_1} is an anagram of {sentence_2}.")
    else:
        print(f"{sentence_1} is not an anagram of {sentence_2}.")


def are_anagrams(sentence_1: str, sentence_2: str) -> bool:

    a_sent_dict = string_to_dict(sentence_1)
    b_sent_dict = string_to_dict(sentence_2)

    if a_sent_dict == b_sent_dict:
        return True
    else:
        return False


def string_to_dict(sentence: str) -> dict:
    
    dictionary = {}
    
    for char in sentence:
        if char != " ":
            if char.lower() in dictionary:
                dictionary[char.lower()] += 1
            else:
                dictionary[char.lower()] = 1

    return dictionary 




if __name__ == "__main__":
    main()
