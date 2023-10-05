from copy import deepcopy  # In case you need it :)

def find_min_and_max_index(a_list: list) -> tuple:
    """Finds the position of the lowest number and the highest number in the list."""

    min_index, max_index = 0, 0

    for i in range(1, len(a_list)):
        if a_list[i] < a_list[min_index]:
            min_index = i

        if a_list[i] > a_list[max_index]:
            max_index = i

    return min_index, max_index


def remove_min_and_max(a_list: list) -> None:
    """Removes the lowest number and the highest number from the list."""
    a_list.remove(max(a_list))
    a_list.remove(min(a_list))


def without_outliers(a_list: list) -> list:
    """Returns a copy of the given list, with the lowest and highest numbers excluded."""
    new_list = a_list[:]
    max_num = 0
    for num in new_list:
        if num > max_num:
            max_num = num    
    min_num = max_num
    for num in new_list:
        if num < min_num:
            min_num = num        
    new_list.remove(max_num)
    new_list.remove(min_num)

    return new_list
    
    
#def main():
#remove_min_and_max(a_list)
#without_outliers(a_list)

#main(a_list)

# Feel free to make use of the following function in your implementations.


""" 
# Alternatively:
def find_min_and_max_index(a_list: list) -> tuple:
    min_index = a_list.index(min(a_list))
    max_index = a_list.index(max(a_list))
    return min_index, max_index
 """
