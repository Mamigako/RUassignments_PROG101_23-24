from typing import List


def extract_evens(int_list: List[int]) -> List[int]:
    """Returns a new list with only the even integers from the given list."""
    new_list = []
    for num in int_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


def remove_odds(int_list: List[int]) -> None:
    """Removes odd integers from the given list."""
    for num in int_list:
        if num % 2 != 0:
            int_list.remove(num)
            while num in int_list:
                int_list.remove(num)
    for num in int_list:
        if num % 2 != 0:
            int_list.remove(num)
            while num in int_list:
                int_list.remove(num)