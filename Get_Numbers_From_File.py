The_List = []

def main():
    with get_file() as file_obj:
        numbers = get_numbers_from_file(file_obj)
        display_numbers(numbers)

def get_file():
    """Gets file name from user and returns the open file handle.

    Asks the user repeatedly for file name
    until an existing file name is given.
    """
    filename = input()
    opened = open_file(filename)
    return opened

def open_file(filename: str):
    index = 0
    while index == 0:
        try:
            return open(filename) 
        except FileNotFoundError:
            try:
                print(f"{filename} not found! Please try again.")
                filename = input()
                return open(filename)
                index = 1
            except EOFError:
                return None
            except FileNotFoundError:
                continue

def get_numbers_from_file(file) -> list:
    """Returns a list of all numbers in the given file.

    Assumes all numbers appear on their own,
    separated from other text by whitespace.
    """
    for line in file:
        linelist = line.strip().split()
        for element in linelist:
            try:
                The_List.append(int(element))
            except ValueError:
                continue
    return The_List

def display_numbers(numbers):
    """Prints out the list, after sorting it."""

    print(sorted(The_List))
    


if __name__ == "__main__":
    main()
