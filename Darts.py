STARTING_POINTS = 301
PLAYER1 = "Player 1"
PLAYER2 = "Player 2"


def play1(PLAYER1,current_points1, points, index):
    
    current_points1 = current_points1 - points
    
    if current_points1 < 0:
        return current_points1 + points, index
    else:
        if current_points1 == 0:
            print(f"\n{PLAYER1} remaining points: {current_points1}")
            print(f"\n{PLAYER1} won!")
            index = True
            return "Victory", index
        else:
            print(f"\n{PLAYER1} remaining points: {current_points1}")
            index = True
            return current_points1, index


def play2(PLAYER2, current_points2, points, index2):

    current_points2 = current_points2 - points
    
    if current_points2 < 0:
        return current_points2 + points, index2
    else:
        if current_points2 == 0:
            print(f"\n{PLAYER2} remaining points: {current_points2}")
            print(f"\n{PLAYER2} won!")
            index2 = True
            return "Victory", index2
        else:
            print(f"\n{PLAYER2} remaining points: {current_points2}")
            index2 = True
            return current_points2, index2


def main():
    
    current_points1 = STARTING_POINTS
    current_points2 = STARTING_POINTS

    index = False
    index2 = False    
    
    while current_points1 and current_points2 > 0:

        index = False
        while not index:
            try:
                points1 = int(input(f"Input points for {PLAYER1}: "))
                if current_points1 - points1 < 0:
                    print(f"\n{PLAYER1} remaining points: {current_points1}")
                    index = True
                    continue
            except ValueError:
                print("\nInvalid input!")
                continue


            current_points1, index = play1(PLAYER1, current_points1, points1, index)
            
        
        if current_points1 == "Victory":
            break
        
        index2 = False
        while not index2:
            try:
                points2 = int(input(f"Input points for {PLAYER2}: "))
                if current_points2 - points2 < 0:
                    print(f"\n{PLAYER2} remaining points: {current_points2}")
                    index2 = True
                    continue
            except ValueError:
                print("\nInvalid input!")
                continue
            

            current_points2, index2 = play2(PLAYER2, current_points2, points2, index2)
        
        if current_points2 == "Victory":
            break



if __name__ == "__main__":
    main()
