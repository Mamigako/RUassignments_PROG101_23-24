Quit_prompt = "q"

def collect_digits(a_string: str) -> str:
    """Outputs all digits found in string."""
    Num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    Num_string = ""

    for char in a_string:
        if char in Num_list:
            Num_string += char
    return Num_string


def inverse_case(a_string: str) -> str:
    """Inverts the case of all characters in the string."""
    Inverse_case_string = ""
    for char in a_string:
        if char == char.lower():
            Inverse_case_string += char.upper()
        else:
            Inverse_case_string += char.lower()
    return Inverse_case_string



def to_hex(decimal: int) -> str:
    """Converts an integer from decimal to its hexadecimal representation."""
    hex_string = ""
    decimal = int(decimal)
    while decimal // 16 != 0:

        remainder = decimal % 16
        if remainder == 10:
            hex_string += "A"
        elif remainder == 11:
            hex_string += "B"
        elif remainder == 12:
            hex_string += "C"
        elif remainder == 13:
            hex_string += "D"
        elif remainder == 14:
            hex_string += "E"
        elif remainder == 15:
            hex_string += "F"
        else:
            hex_string += str(remainder)
            decimal = decimal // 16

    remainder = decimal % 16
    if remainder == 10:
        hex_string += "A"
    elif remainder == 11:
        hex_string += "B"
    elif remainder == 12:
        hex_string += "C"
    elif remainder == 13:
        hex_string += "D"
    elif remainder == 14:
        hex_string += "E"
    elif remainder == 15:
        hex_string += "F"
    else:
        hex_string += str(remainder)
        decimal = decimal // 16
    return hex_string[::-1]



def String_Functions(): 
    command = input() 
    while command != Quit_prompt:
        if command == "c":
            string = input()
            print(collect_digits(string))
        elif command == "i":
            string = input()
            print(inverse_case(string))
        elif command == "h":
            string = input()
            print(to_hex(string))
        command = input()


String_Functions()