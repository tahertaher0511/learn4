def printer():
    print(f"""
{'-' * 9}
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
{'-' * 9}""")


def state():
    wins = []

    for i in range(3):  # check for wins in rows and cols
        if game[i] == game[i + 3] and game[i] == game[i + 6] and game[i] != '_':
            wins.append(game[i])  # win in row
        if game[i * 3] == game[i * 3 + 1] and game[i * 3] == game[i * 3 + 2] and game[i * 3] != '_':
            wins.append(game[i])  # win in col

    if game[0] == game[4] and game[0] == game[8] and game[0] != '_':  # win on leading diagonal
        wins.append(game[0])
    if game[2] == game[4] and game[2] == game[6] and game[2] != '_':  # win on non-leading diagonal
        wins.append(game[2])

    if 0 < len(wins) < 3:  # winner!
        print(wins[0] + " wins")
        return 1
    elif game.count('X') + game.count('O') == 9:  # draw
        print("Draw")
        return 1
    else:  # unfinished game
        return 0


def pos(move):
    return (3 - int(move[1])) * 3 + int(move[0]) - 1


def make_move():
    global game
    global turn
    move = input("Enter the coordinates: ").split()
    if len(move) != 2:
        print("You should enter two numbers!")
        make_move()
    elif not move[0].isnumeric() or not move[1].isnumeric():
        print("You should enter numbers!")
        make_move()
    elif move[0] not in "123" or move[1] not in "123":
        print("Coordinates should be from 1 to 3!")
        make_move()
    elif game[pos(move)] != '_':
        print("This cell is occupied! Choose another one!")
        make_move()
    else:
        game[pos(move)] = piece[turn % 2]
        turn += 1


piece = ['X', 'O']
turn = 0
game = list("_" * 9)
printer()
while state() == 0:
    make_move()
    printer()
