player_name = [ "Sam", "Steven", "Craig", "Matt", "Jake", "Gavin" ]
player_score = [ [0, 15], [1, 17], [1, 9], [1, 21], [0, 18], [0, 19] ]

n_players = len(player_name)
blue_score = 0
red_score = 0
blue_high_score = 0
red_high_score = 0
blue_player = ""
red_player = ""

for player in range(n_players):
    if player_score[player][0] == 0:
        blue_score = blue_score + player_score[player][1]
        if blue_score > blue_high_score:
            blue_high_score = blue_score
            blue_player = player
    else:
        red_score = red_score + player_score[player][1]
        if red_score > red_high_score:
            red_high_score = red_score
            red_player = player

print("Winning team:")
if blue_score > red_score:
    print("Blue Team!")
else:
    print("Red Team!")

print("Red team total score:", red_score)
print("Blue team total score:", blue_score)
print("Highest scorer in red team:", player_name[red_player])
print("Highest scorer in blue team:", player_name[blue_player])