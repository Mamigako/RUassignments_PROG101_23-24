import sys

def main():
    dictionary = {}
    
    while True:
        text_file = input()
        
        index = make_dictionary(text_file, dictionary)
        
        if index == 1:
            while True:
                exit_program = output_len_countries(dictionary)
                if exit_program:
                    sys.exit()

def make_dictionary(text_file, dictionary):
    try:
        with open(text_file) as file:
            for line in file:
                length = len(line.strip())
                if length in dictionary:
                    dictionary[length].append(line.strip())
                else:
                    dictionary[length] = [line.strip()]
        return 1

    except FileNotFoundError:
        print(f"File {text_file} not found!")
        return 0  

def output_len_countries(dictionary):
    while True:
        length = int(input())
        if length in dictionary:
            country_list = dictionary[length]
            print(", ".join(country_list))
        else:
            print(f"No country name of length {length} exists.")
        
        again = input().lower()
        if again == "n":
            return True
        elif again == "y":
            return False

if __name__ == "__main__":
    main()
