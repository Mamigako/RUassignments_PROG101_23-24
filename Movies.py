def main():
    """A simple system that performs operations on a csv with movies in it based on user input."""
    
    filename = input("Enter filename:")
    print()
    file_stream = open_file(filename)
    if file_stream != None:

    
        main_dict = make_main_dict(file_stream)

        file_stream.seek(0)

        year_dict = make_year_dict(file_stream)


        selection = "a"

        while selection in "abcABC123":
        
            menu()
            selection = input("Enter your selection:")
            print()

            if selection in "aA1":
                display_result_main_dict(main_dict)
                
                continue

            elif selection in "bB2":
                display_year(year_dict)
                
                continue

            elif selection in "cC3":
                main_dict = change_rating(main_dict)
                #display_result_main_dict(main_dict)
                
                continue

def open_file(filename):
    """Opens the file with the given file name.

    Returns the corresponding file stream, or None if the file cannot be opened.
    """
    try:
        file_stream = open(filename)
        return file_stream
    except FileNotFoundError:
        print(f"\nFile {filename} not found!")
        return None

def make_main_dict(file_stream):
    
    main_dict = {}

    for line in file_stream:
        listo = []
        for word in line.strip().split(";"):
            if word == line.strip().split(";")[0]:
                main_dict[word] = None
            else:
                listo.append(word)
        main_dict[line.strip().split(";")[0]] = listo
    
    return main_dict
                
def make_year_dict(file_stream):
    
    year_dict = {}

    for line in file_stream:
        if line.strip().split(";")[-1] not in year_dict:
            year_dict[line.strip().split(";")[-1]] = [line.strip().split(";")[0]]
        else:
            year_dict[line.strip().split(";")[-1]].append(line.strip().split(";")[0])

    return year_dict

def display_result_main_dict(dictionary: dict) -> None:
    """Prints the words in alphabetical order, along with the definitions."""
    for key in sorted(dictionary):
        print("{:<50}".format(key), end="")
        print("{:>6.2f}".format(float(dictionary[key][0])), end="")
        print("{:>6}".format(dictionary[key][1]))

def display_year(year_dict):
    year = input("Enter year:")
    print()
    for val in year_dict[year]:
        print(val)

def menu():
    print("\n*******************************")
    print("1. Movies in alphabetical order")
    print("2. Titles in given year")
    print("3. Modify all ratings")
    print("*******************************\n")

def change_rating(main_dict):
    
    add_to_rating = float(input("Enter modifier for ratings:"))
    print()


    for key in main_dict:
        main_dict[key][0] = float(main_dict[key][0]) + add_to_rating
    
    return main_dict


if __name__ == "__main__":
    main()
