from typing import List, Tuple


def list_to_bool_tuple(a_list: List[str]) -> Tuple[bool]:
    """Returns a tuple with each element in the list converted to bool.

    First converts any integers to int.
    """
    for element in List:
        temp_list = []
        bool_list = []
        try:
            temp_list.append(int(element))
        except TypeError:
            temp_list.append(element)
        for element in temp_list:
            bool_list.append(bool(element))
    return tuple(bool_list)