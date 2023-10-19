def main():

    num_of_lines = int(input())

    chore_list = chores(num_of_lines)

    output_chores(chore_list)



def chores(num_of_lines):
    chore_list = []
    chore_set = set()
    for i in range(num_of_lines):
        chore = input()
        if chore not in chore_set:
            chore_set.add(chore)
            chore_list.append(chore)
    

    return chore_list


def output_chores(chore_list):
    for chore in chore_list:
        print(chore)


main()
