def list_to_bool_tuple(a_list):
    """Returns a tuple with each element in the list converted to bool.

    First converts any integers to int.
    """
    temp_list = []
    for element in a_list:
        try:
            temp_list.append(int(element))
        except ValueError:
            temp_list.append(element)
        except TypeError:
            temp_list.append(element)

    bool_list = [bool(element) for element in temp_list]
    return tuple(bool_list)
