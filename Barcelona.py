

def main():
    baginput = input()
    bag_number_input = input()

    bag_number_list = []
    bag_list = []
    
    bag_list = baginput.split()
    bag_number_list = bag_number_input.split()

    amount_of_lines = bag_list[0]
    bennis_bag = bag_list[1]
    for_count = 0
    for bag in bag_number_list:
        if bennis_bag == bag_number_list[0]:
            print("fyrst")
            break
        elif bennis_bag == bag_number_list[1]:
            print("naestfyrst")
            break
        elif bennis_bag == bag_number_list[for_count]:
            print(str(for_count+1) + " " + "fyrst")
            break
        for_count += 1


if __name__ == "__main__":
    main()
