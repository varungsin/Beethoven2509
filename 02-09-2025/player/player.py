players = [
    {'id': 101,'name' : 'jaiswal'},
    {'id': 102,'name' : 'gill'}
]
# print(players)

player = {}
player['id'] = 103
player['name'] = 'abhishek'

players.append(player)
# print(player)

for player in players:
    if player['id'] == 103:
        print(player)

players_dict = {101:players[0],102:players[1],103:players[2]}

print(players_dict[103])