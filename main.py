from game import game

num_players = int(input('How many player are going to play? '))

if num_players not in range(1, 4):
    while num_players not in range(1, 4):
        print('\nYou can play solo or up to 4 players.')
        num_players = int(input('How many player are going to play? '))

points = {}
for i in range(1, num_players + 1):
    player_name = input(f'\nWhat´s the player {i} name? ')
    points[player_name] = game(player_name)

winner = [i for i, e in points.items() if e == max(points.values())]

if len(winner) == 1:
    print(f'\nThe winner with {max(points.values())} points is {"".join(winner)}!!!')
else:
    print(f'\nIt´s a tie! The winners are {", ".join(winner[0:-1])} and {"".join(winner[-1:])}!')
