# Ask for input and assign 
number_of_players = int(input())
sum = 0
# ask for number of players as long as it is under 2.
while number_of_players < 2:
    number_of_players = int(input())

# loop through range of players and ask for value, assign to sum.
for i in range((number_of_players)):
    t = int(input())
    sum = sum + t
# Calculate the remainder.
r = sum % number_of_players
# print result.
print(f"The sum of all contributions is {sum}\nWhen {sum} is divided by {number_of_players}, the remainder is {r}\nPlayer {r} is the winner!")