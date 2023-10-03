# Return a list of entered addresses and the same list with the addresses as tuples.
Quit_prompt = "q"
Norm_list = []
Tuple_list = []
address = input()

def get_home_addresses(address):
    while address != Quit_prompt:
        Norm_list.append(address)
        address = input()
    return Norm_list

def get_tuple_from_home_addresses(home_addresses):
    for element in Norm_list: 
            Tuple_list.append(tuple(element.split())) 
    return Tuple_list

def main():
    home_addresses = get_home_addresses(address)
    print(home_addresses)
    street_and_number = get_tuple_from_home_addresses(home_addresses)
    print(street_and_number)


if __name__ == "__main__":
    main()
