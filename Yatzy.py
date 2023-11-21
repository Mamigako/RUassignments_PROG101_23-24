from typing import List

MAX_DICE_RESULT = 6  # Assume a standard 6-sided die.


def main():
    """A single player Yatzy game with 5 dice and 5 outcomes including exiting the game when an empty line is entered."""

    while True:

        #rolling
        dice_ints = dice_roll()

        #break condition
        if dice_ints == False:
            break

        #get counts
        counts = get_counts(dice_ints)

        #display points
        print(points(counts))



def dice_roll() -> List[int]:

    rolls = input()

    if rolls == "":
        return False

    dice_results = rolls.split()

    dice_ints = [int(element) for element in dice_results] 

    return dice_ints


def get_counts(dice_ints: List[int]) -> List[int]:
    """Counts how often each value appears.

    Returns a list of counts
    for each possible outcome on a die roll,
    where the first count in the list
    (at position 0 in the output list)
    indicates how many 1's appear
    in the given list of dice results,
    the second count (at position 1)
    indicates how many 2's appear, and so on.
    The count list is as long as there are sides on the dice.

    For example, if the dice list is [3, 3, 4, 4, 1],
    then the count list is [1, 0, 2, 2, 0, 0],
    indicating that the number 1 appears once,
    the numbers 3 and 4 appear twice each,
    but the numbers 2, 5 and 6 never appear.
    """

    counts = [dice_ints.count(value) for value in range(1, MAX_DICE_RESULT + 1)]
    return counts


def points(counts: List[int]) -> int:


    if 2 not in counts and 3 not in counts and 4 not in counts and 5 not in counts:
        p = 0
        return p
    
    else:

        if 5 in counts:
            p = 50
            return p
    

        counter = 0
    
        for i in counts:
            counter += 1
            if i == 3:
                p = 3 * counter
                return p
            elif i == 4:
                p = 3 * counter
                return p
    

        counter = 0

        for i in counts:
            counter += 1
            if i == 2:
                p = 2 * counter    
        return p






if __name__ == "__main__":
    main()
    