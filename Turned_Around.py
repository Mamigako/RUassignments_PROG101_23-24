
def main():
    number_of_ints = input()
    count = 0
    number_list = []
    while str(count) != number_of_ints:
         number = input()
         number_list.append(int(number))
         count += 1 
    while number_list:
        if len(number_list) == 1:
                print(number_list[0])
                break
        for num in number_list:        
            print(number_list[-1])
            number_list.remove(number_list[-1])
        


if __name__ == "__main__":
    main()
