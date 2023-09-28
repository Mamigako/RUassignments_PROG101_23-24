def are_permutation_of_same_digits(m: str,n: str)->bool:
    m_sum = 0
    n_sum = 0

    for i in m:
        m_sum += ord(i)

    for i in n:
        n_sum += ord(i)

    if n_sum == m_sum:
        return True

    else:
        return False
    

first_permutation = str(input())
second_permutation = str(input())

if are_permutation_of_same_digits(first_permutation, second_permutation):
    print(f"The numbers {first_permutation} and {second_permutation} are permutations of each other.")
else:
    print(f"The numbers {first_permutation} and {second_permutation} are not permutations of each other.")