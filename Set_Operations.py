import string

UI = False


def openfile(file1, file2):
    file_list1 = []
    file_list2 = []

    with open(file1) as filename1:
        for line in filename1:
            for word in line.split():
                file_list1.append(word.strip(string.punctuation))

    with open(file2) as filename2:
        for line in filename2:
            for word in line.split():
                file_list2.append(word.strip(string.punctuation))    

    return file_list1, file_list2
 

def common_words(file_list1, file_list2):
    common_set = set(file_list1).intersection(set(file_list2))
    return common_set


def xor(file_list1, file_list2):
    file_xor_set = set(file_list1).symmetric_difference(set(file_list2))
    return file_xor_set


def file1_only(file_list1, file_list2):
    file1_only_set = set(file_list1) - set(file_list2)
    return file1_only_set


def main():
    
    file1 = input("Enter the name of the first file:\n" if UI else "")
    file2 = input("Enter the name of the second file:\n" if UI else "")

    file_list1, file_list2 = openfile(file1, file2)

    common_set = common_words(file_list1, file_list2)

    file_xor_set = xor(file_list1, file_list2)

    file1_only_set = file1_only(file_list1, file_list2)


    n1 = len(common_set)
    print(f"The two files have {n1} words in common.")
    if n1 != 0:
        print(f"These words are as follows:")
        for word in sorted(common_set):
            if len(common_set) == 1:
                print(f"{word}\n")
                break
            elif word == sorted(common_set)[-2]:
                print(f"{sorted(common_set)[-2]} and {sorted(common_set)[-1]}.\n")
                break
            else:
                print(word + ",", end=" ")

    n2 = len(file_xor_set)
    print(f"There are {n2} words that are only in either file but not both.")
    if n2 != 0:
        print(f"These words are as follows:")
        for word in sorted(file_xor_set):
            if len(file_xor_set) == 1:
                print(f"{word}\n")
                break
            elif word == sorted(file_xor_set)[-2]:
                print(f"{sorted(file_xor_set)[-2]} and {sorted(file_xor_set)[-1]}.\n")
                break
            else:
                print(word + ",", end=" ")

    n3 = len(file1_only_set)
    print(f"There are {n3} words that only appear in the first file.")
    if n3 != 0:
        print(f"These words are as follows:")
        for word in sorted(file1_only_set):
            if len(file1_only_set) == 1:
                print(f"{word}\n")
                break            
            elif word == sorted(file1_only_set)[-2]:
                print(f"{sorted(file1_only_set)[-2]} and {sorted(file1_only_set)[-1]}.\n")
                break
            else:
                print(word + ",", end=" ")

if __name__ == "__main__":
    main()
