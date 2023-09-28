def main():
    problem_numbers= input()
    problem_numbers= problem_numbers.split(";")
    consecutive_problems= 0
    non_consecutive_problems= 0

    for problem in problem_numbers:

        if "-" in problem:
            subproblem=problem.split("-")
            number_of_consecutive_problems= int(subproblem[1])- int(subproblem[0]) + 1
            consecutive_problems+= number_of_consecutive_problems

        else:
            non_consecutive_problems+= 1

    total_problems= consecutive_problems + non_consecutive_problems
    print(total_problems)

if __name__ == "__main__":
    main()