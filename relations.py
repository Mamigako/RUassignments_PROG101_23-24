# T-117-STR1 Discrete Mathematics I
# Template for Individual assignment 5

# Problem 1a)
def is_reflexive(defined_set, relation_on_set):
    
    # We check whether there is a tuple for each element in the defined set which
    # has a path to itself.
    # If this is the case, we return True, else return False. 
    

    for element in defined_set:
    
        reflexive = False
        if (element,element) in relation_on_set:
            reflexive = True
    
    return reflexive

# Problem 1b)
def is_symmetric(relation_on_set):
    
    # Looping through the relations, we check whether the tuple with its elements reversed is in the relations.
    # If it is not, we return False, as the relation is not symmetric.


    for tuple in relation_on_set:
        symmetric_bool = False
    
        if (tuple[1],tuple[0]) in relation_on_set:
            symmetric_bool = True
    
    return symmetric_bool


# Problem 1c)
def is_antisymmetric(relation_on_set):

    # Looping through the relations, we check whether the tuple with its elements reversed is in the relations.
    # If it is, we return False, as the relation is not antisymmetric.

    
    for tuple in relation_on_set:
        asymmetric_bool = False
    
        if (tuple[1],tuple[0]) not in relation_on_set:
            asymmetric_bool = True
    
            return asymmetric_bool


# Problem 1d)
def is_transitive(relation_on_set):

    # For every tuple, we loop through all other tuples 
    # and if we find that there is no transitive relation for the given values, we return False.

    for (a, b) in relation_on_set:
        for (c, d) in relation_on_set:
            if b == c:
                if (a, d) not in relation_on_set:
                    return False
    return True

# Problem 2    
def is_equivalence_relation(defined_set, relation_on_set):

    # Call all three functions, if all return True, return True, else return False.
    # This is because to qualify for equivalence relation, the relation has to be reflexive, symmetric and transitive.

    reflexive = is_reflexive(defined_set, relation_on_set)
    symmetric = is_symmetric(relation_on_set)
    transitive = is_transitive(relation_on_set)

    if reflexive and symmetric and transitive:
        return True
    else:
        return False


# Problem 3
def composite_relations(relation1, relation2):
    
    # We loop through the relation list tuples and if the latter element in tuple R2 is equal to 
    # the first element in tuple R1, then add the first element in R2 and the latter element in R1 as a tuple to the composite set.
    # return composite as a list of tuples.

    composite = set()

    for (a, b) in relation2:
        for (c, d) in relation1:
            if b == c:
                composite.add((a, d))
    
    return list(composite)



# Problem 4a)
def aces_in_relation_a(A):
    # Because A is defined as not having 0 in it, this function will never return anything else than 0
    # as there are no 0s in this matrix.
    return 0

# Problem 4b)
def aces_in_relation_b(A):

    #Due to a = b + 1, the set of tuples of relations of MatrixA will always be the length of n - 1
    #e.g  (2, 1),(3, 2)...(n, n-1)
    # the amount of 1s in the matrix is equal to the amount of tuples in it´s relations.
    return len(A)-1

# Problem 4c)
def aces_in_relation_c(A):
    
    #we loop through the elements and for each element a we loop through all the elements b
    # and if a >= b, (a,b) gets appended to the list of relations. The length is then the answer.

    relation_list = []

    for a in A:
        for b in A:
            if a >= b:
                relation_list.append((a, b))

    return len(relation_list)
   
# Problem 4d)
def aces_in_relation_d(A):

    # we loop through A, and for every element we check every other element and whether their addition results in 1000.
    # if so, append both to relations list.
    # Lastly, return the length of said list, which is the number of 1s.

    relation_list = []
    
    for a in A:
        for b in A:
            if a + b == 1000:
                relation_list.append((a, b))

    return len(relation_list)
    
# Problem 4e)
def aces_in_relation_e(A):
    
    # we loop through A, and for every element we check every other element and whether their addition results in 1001.
    # if so, append both to relations list.
    # Lastly, return the length of said list, which is the number of 1s.

    relation_list = []
    
    for a in A:
        for b in A:
            if a + b == 1001:
                relation_list.append((a, b))
    
    return len(relation_list)





























            