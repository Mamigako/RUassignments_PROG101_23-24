Input_string = input()
Input_int_list = []
Missing_int_list = []

"""Transform a string into 3 different kinds of lists."""

def output_string(strings):
    strings = Input_string.split()
    Input_list = strings
    print(Input_list)
    return Input_list


def output_int_list(string_list):
    for element in string_list:
        if element.isdigit():
            Input_int_list.append(int(element))
   
    print(Input_int_list)
    return Input_int_list


def output_missing_ints(list_of_ints):
    try:
    
        for i in range(max(Input_int_list)):
            if i not in Input_int_list:
                Missing_int_list.append(i)
        print(Missing_int_list)
    
    except ValueError:
    
        print(Missing_int_list)


def main():
    string_list = output_string(Input_string)
    int_list = output_int_list(string_list)
    output_missing_ints(int_list)

main()