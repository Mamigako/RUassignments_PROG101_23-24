queen = 9
rook = 5
bishop = 3
knight = 3
pawn = 1


value = int(input())


#Evaluate whether value is equal to chess piece and print.
if value == 9:
    print("Queen")
elif value == 5:
    print("Rook")
elif value == 3:
    print("Bishop or Knight")
elif value == 1:
    print("Pawn")
else:
    print("No Piece")