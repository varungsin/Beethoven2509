players = [
    (101,'jaiswal'),
    (102,'gill')
]
# print(players)

player = {}
player = (103,'abhishek')

players.append(player)
# print(player)

for player in players:
    if player[0] == 103:
        print(player)

players_dict = {101:players[0],102:players[1],103:players[2]}

# print(players_dict[103])
print(players)