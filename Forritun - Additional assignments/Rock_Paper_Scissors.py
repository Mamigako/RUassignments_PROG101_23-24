# ask for input, 1=rock, 2=paper, 3=scissors
player_a = int(input())
player_b = int(input())


def rock_paper_scissors(player_a, player_b):
    # If player a and b choose the same, tie.
    if (player_a == player_b):
        print("Tie")
    # if a chooses 1(rock) and if b chooses 3(scissors), a wins.
    # this is expressed by (1 - 3 = -2), (-2 % 3 == -2)
    # if a chooses paper and b scissors, b wins 
    # this is expressed by (2 - 3 = 5), (5 % 3 == 2)  
    # if a chooses scissors and b chooses paper, a wins
    # this is expressed by (3 -)
    elif (player_a - player_b) % 3 == 1:
        print("player_a wins")
    else:
        print("player_b wins")

rock_paper_scissors(player_a, player_b)