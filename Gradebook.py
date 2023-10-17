def main():
    
    dictionary = {}

    ask_email(dictionary)
    while another():
        ask_email(dictionary)
    get_mean(dictionary)



def ask_email(dictionary):
    email = input()
    grade = input()
    if email in dictionary:
        dictionary[email].append(int(grade))
    else:
        dictionary[email] = []
        dictionary[email].append(int(grade))


def another():
    another_go = input()
    if another_go == "n":
        return False
    else:
        return True


def get_mean(dictionary):
    for key in sorted(dictionary):
        print(key + ":", end=" ")
        print(round(sum(dictionary[key]) / len(dictionary[key]) , 2))

if __name__ == "__main__":
    main()
