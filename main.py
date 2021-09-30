grid = list('_________')
name = ''
counter = 0
count_X = grid.count('X')
count_O = grid.count('O')
gridder = []
while grid != []:
    gridder.append(grid[:3])
    grid = grid[3:]

print("---------")
print('| ' + gridder[0][0] + ' ' + gridder[0][1] + ' ' + gridder[0][2] + ' |')
print('| ' + gridder[1][0] + ' ' + gridder[1][1] + ' ' + gridder[1][2] + ' |')
print('| ' + gridder[2][0] + ' ' + gridder[2][1] + ' ' + gridder[2][2] + ' |')
print("---------")

cell = 'X'
while True:
    game_input = input("Enter coordinates: ").split()
    if not (game_input[0] or game_input[1]) in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print('You should enter numbers!')
        continue
    f1 = int(game_input[0])
    f2 = int(game_input[1])
    if f1 < 0 or f2 < 0 or f1 > 3 or f2 > 3:
        print('Coordinates should be from 1 to 3!')
    elif gridder[f1 - 1][f2 - 1] == 'X' or gridder[f1 - 1][f2 - 1] == 'O':
        print("This cell is occupied! Choose another one!")
    elif f2 > 0 and f2 <= 3 and f1 > 0 and f2 <= 3:
        gridder[f1 - 1][f2 - 1] = cell
        print("---------")
        print('| ' + gridder[0][0] + ' ' + gridder[0][1] + ' ' + gridder[0][2] + ' |')
        print('| ' + gridder[1][0] + ' ' + gridder[1][1] + ' ' + gridder[1][2] + ' |')
        print('| ' + gridder[2][0] + ' ' + gridder[2][1] + ' ' + gridder[2][2] + ' |')
        print("---------")
        if cell == 'X':
            cell = 'O'
        elif cell == 'O':
            cell = 'X'
        counter += 1
    if (gridder[0][0] != '_') and (gridder[0][0] == gridder[0][1]) and (gridder[0][1] == gridder[0][2]):
        name += gridder[0][0]
    if (gridder[1][0] != '_') and (gridder[1][0] == gridder[1][1]) and (gridder[1][1] == gridder[1][2]):
        name += gridder[1][0]
    if (gridder[2][0] != '_') and (gridder[2][0] == gridder[2][1]) and (gridder[2][1] == gridder[2][2]):
        name += gridder[2][0]
    if (gridder[0][0] != '_') and (gridder[0][0] == gridder[1][0]) and (gridder[1][0] == gridder[2][0]):
        name += gridder[0][0]
    if (gridder[0][1] != '_') and (gridder[0][1] == gridder[1][1]) and (gridder[1][1] == gridder[2][1]):
        name += gridder[0][1]
    if (gridder[0][2] != '_') and (gridder[0][2] == gridder[1][2]) and (gridder[1][2] == gridder[2][2]):
        name += gridder[0][2]
    if (gridder[0][0] != '_') and (gridder[0][0] == gridder[1][1]) and (gridder[1][1] == gridder[2][2]):
        name += gridder[0][0]
    if (gridder[0][2] != '_') and (gridder[0][2] == gridder[1][1]) and (gridder[1][1] == gridder[2][0]):
        name += gridder[0][2]
    if name != '':
        print(name + ' wins')
        break
    if counter == 9:
        print('Draw')
        break
