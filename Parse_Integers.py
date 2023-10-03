# Convert a list of integers into a tuple. 
def list_to_int_tuple(some_list):
    temp_list = []
    for element in some_list:
        try:
            temp_list.append(int(element))
        except ValueError:
            continue
    return tuple(temp_list)

