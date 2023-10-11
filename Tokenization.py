text_file = input()
Split_word_list = []
Split_token_list = []

"""Outputs a list of words and a list of tokens from a single text file."""

def open_file(text_file):
    try:
        opened = open(text_file)
        return opened
    except ValueError:
        return None

def split_on_words(opened):
    for line in opened:
        for word in line.split():
            Split_word_list.append(word)
    return Split_word_list

def split_on_tokens(word_list):

    for word in word_list:
        if "." in word:
                Split_token_list.append(word[:-1])
                Split_token_list.append(word[-1])
            
        elif "," in word:
            Split_token_list.append(word[:-1])
            Split_token_list.append(word[-1])
            
        elif "!" in word:
            Split_token_list.append(word[:-1])
            Split_token_list.append(word[-1])
            
        elif "?" in word:
            Split_token_list.append(word[:-1])
            Split_token_list.append(word[-1])  
            
        else:
            Split_token_list.append(word) 
    return Split_token_list

def count_and_print(this_list):
    count = 0

    for element in this_list:
        count += 1
    print(count)
    
    for element in this_list: 
        print(element)

def main(text_file):
    try:
        opened = open_file(text_file)
        Split_word_list = split_on_words(opened)
        Split_token_list = split_on_tokens(Split_word_list)
        count_and_print(Split_word_list)
        count_and_print(Split_token_list)
    except FileNotFoundError:
        return None
    except ValueError:
        return None

main(text_file)