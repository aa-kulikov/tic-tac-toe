import random
import time

class Game:
    def __init__(self):
        self.start()

    def menu(self):
        while True:
            self.lobby = input("Please, enter your commands: start OR exit, and choose users (easy, medium, hard, user):\n").split()
            if self.lobby[0] == 'exit':
                break
            if self.lobby[0] != 'start' and self.lobby[0] != 'exit':
                print('Bad parameters')
                continue
            if (len(self.lobby)) < 3:
                print('Bad parameters')
                continue
            if self.lobby[1] not in {'easy', 'medium', 'hard', 'user'} or self.lobby[2] not in {'easy', 'medium', 'hard', 'user'}:
                print('Bad parameters!')
                continue
            else:
                return

    def start(self):
        self.current_state = [['_', '_', '_'],
                              ['_', '_', '_'],
                              ['_', '_', '_']]
        self.first = 'X'
        self.second = 'O'
        self.closest_win = None
        self.closest_win1 = None
        self.win_in_1 = None

    def draw_board(self):
        print("---------")
        for a in range(0, 3):
            print('|', end=' ')
            for b in range(0, 3):
                print(f"{self.current_state[a][b]}", end=' '),
            print('|')
        print("---------")

    def is_legal(self, px, py):
        if px < 0 or px >= 3 or py < 0 or py >= 3:
            return False
        elif self.current_state[px][py] != '_':
            return False
        else:
            return True

    def is_end_game(self):
        # vertical win_game
        for i in range(0, 3):
            if self.current_state[0][i] != '_' and self.current_state[0][i] == self.current_state[1][i] \
                    and self.current_state[1][i] == self.current_state[2][i]:
                return self.current_state[0][i]
        # horizontal win_game
        for i in range(0, 3):
            if self.current_state[i] == ['X', 'X', 'X']:
                return 'X'
            elif self.current_state[i] == ['O', 'O', 'O']:
                return 'O'
        # main diagonal win_game
        if (self.current_state[0][0] != '_' and
                self.current_state[0][0] == self.current_state[1][1] and
                self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]
        # second diagonal win_game
        if (self.current_state[0][2] != '_' and
                self.current_state[0][2] == self.current_state[1][1] and
                self.current_state[1][1] == self.current_state[2][0]):
            return self.current_state[0][2]

        # is board empty?
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '_':
                    return None
        return '_'

    def close_win(self, grid):
        if grid[0][0] != '_' and grid[0][0] == grid[1][1] and grid[2][2] == '_':
            self.closest_win, self.closest_win1 = 2, 2
            self.win_in_1 = True
        if grid[0][2] != '_' and grid[0][2] == grid[1][1] and grid[2][0] == '_':
            self.closest_win, self.closest_win1 = 2, 0
            self.win_in_1 = True
        if grid[2][0] != '_' and grid[2][0] == grid[1][1] and grid[0][2] == '_':
            self.closest_win, self.closest_win1 = 0, 2
            self.win_in_1 = True
        if grid[2][2] != '_' and grid[2][2] == grid[1][1] and grid[0][0] == '_':
            self.closest_win, self.closest_win1 = 0, 0
            self.win_in_1 = True

        if grid[0][0] != '_' and grid[0][0] == grid[1][0] and grid[2][0] == '_':
            self.closest_win, self.closest_win1 = 2, 0 # vertical lines
            self.win_in_1 = True
        if grid[0][1] != '_' and grid[0][1] == grid[1][1] and grid[2][1] == '_':
            self.closest_win, self.closest_win1 = 2, 1
            self.win_in_1 = True
        if grid[0][2] != '_' and grid[0][2] == grid[1][2] and grid[2][2] == '_':
            self.closest_win, self.closest_win1 = 2, 2
            self.win_in_1 = True
        if grid[2][0] != '_' and grid[2][0] == grid[1][0] and grid[0][0] == '_':
            self.closest_win, self.closest_win1 = 0, 0
            self.win_in_1 = True
        if grid[2][1] != '_' and grid[2][1] == grid[1][1] and grid[0][1] == '_':
            self.closest_win, self.closest_win1 = 0, 1
            self.win_in_1 = True
        if grid[2][2] != '_' and grid[2][2] == grid[1][2] and grid[0][2] == '_':
            self.closest_win, self.closest_win1 = 0, 2 # vertical lines
            self.win_in_1 = True

        if grid[0][0] != '_' and grid[0][0] == grid[0][1] and grid[0][2] == '_':
            self.closest_win, self.closest_win1 = 0, 2
            self.win_in_1 = True
        if grid[1][0] != '_' and grid[1][0] == grid[1][1] and grid[1][2] == '_':
            self.closest_win, self.closest_win1 = 1, 2
            self.win_in_1 = True
        if grid[2][0] != '_' and grid[2][0] == grid[2][1] and grid[2][2] == '_':
            self.closest_win, self.closest_win1 = 2, 2
            self.win_in_1 = True
        if grid[0][2] != '_' and grid[0][2] == grid[0][1] and grid[0][0] == '_':
            self.closest_win, self.closest_win1 = 0, 0
            self.win_in_1 = True
        if grid[1][2] != '_' and grid[1][2] == grid[1][1] and grid[1][0] == '_':
            self.closest_win, self.closest_win1 = 1, 0
            self.win_in_1 = True
        if grid[2][2] != '_' and grid[2][2] == grid[2][1] and grid[2][0] == '_':
            self.closest_win, self.closest_win1 = 2, 0
            self.win_in_1 = True

    def change_letter(self):
        if self.letter1 == 'X':
            self.letter1 = 'O'
        else:
            self.letter1 = 'X'

    def maxi(self, letter):

        maxv = -2
        qx = None
        qv = None

        result = self.is_end_game()
        if result == letter:
            return (1, 0, 0)
        elif result != letter and result != '_' and result is not None:
            return (-1, 0, 0)
        elif result == '_':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '_':
                    self.current_state[i][j] = letter
                    if letter == 'X':
                        (v, min_i, min_j) = self.mini('O')
                        if v > maxv:
                            maxv = v
                            qx = i
                            qv = j
                    elif letter == 'O':
                        (v, min_i, min_j) = self.mini('X')
                        if v > maxv:
                            maxv = v
                            qx = i
                            qv = j
                    self.current_state[i][j] = '_'
        return (maxv, qx, qv)

    def move(self, px, py):
        self.current_state[px][py] = self.letter1
        self.draw_board()
        self.change_letter()

    def rand_move(self, word):
        while True:
            px = random.randint(0, 2)
            py = random.randint(0, 2)
            if self.is_legal(px, py):
                self.move(px, py)
                break

    def mini(self, letter):

        miniv = 2
        px = None
        pv = None

        result = self.is_end_game()
        if result == letter:
            return (-1, 0, 0)
        elif result != letter and result != '_' and result is not None:
            return (1, 0, 0)
        elif result == '_':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '_':
                    self.current_state[i][j] = letter
                    if letter == 'X':
                        (v, max_i, max_j) = self.maxi('O')
                        if v < miniv:
                            miniv = v
                            px = i
                            pv = j
                    elif letter == 'O':
                        (v, max_i, max_j) = self.maxi('X')
                        if v < miniv:
                            miniv = v
                            px = i
                            pv = j
                    self.current_state[i][j] = '_'
        return (miniv, px, pv)

    def turn(self, n):
        if self.lobby[n] == 'user':  # If it's player's turn
            while True:
                coords = input('Enter the coordinates: ').split()
                px, py = int(coords[0]), int(coords[1])

                (qx, qy) = (px - 1, py - 1)

                if self.is_legal(qx, qy):
                    self.move(qx, qy)
                    break
                else:
                    print('The move is not valid! Try again.')

        if self.lobby[n] == 'hard':
            count = 0
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.current_state[i][j] == '_':
                        count += 1
            if count >= 8 and self.is_legal(1, 1):
                self.move(1, 1)
            else:
                (m, px, py) = self.maxi(self.letter1)
                print(f'Making move level "{self.lobby[n]}"')
                self.move(px, py)

        if self.lobby[n] == 'medium':
            if self.win_in_1 is True and self.is_legal(self.closest_win, self.closest_win1):
                print(f'Making move level "{self.lobby[n]}"')
                self.move(self.closest_win, self.closest_win1)
            else:
                print(f'Making move level "{self.lobby[n]}"')
                self.rand_move(self.lobby[n])

        if self.lobby[n] == 'easy':
            print(f'Making move level "{self.lobby[n]}"')
            self.rand_move(self.lobby[n])


    def play(self):  # DELETE THIS
        t0 = time.time_ns()
        self.menu()
        self.letter1 = 'X'
        self.draw_board()
        while self.lobby[0] == 'start':
            self.result = self.is_end_game()
            # Printing the appropriate message if the game has ended
            if self.result is not None:
                t1 = time.time_ns()
                if self.result == 'X':
                    print('X wins!')
                elif self.result == 'O':
                    print('O wins!')
                elif self.result == '_':
                    print("Draw")

                print(f'time is {t1 - t0}')
                self.start()
                return
            self.close_win(self.current_state)
            if self.letter1 == 'X':
                self.turn(1)
                continue
            elif self.letter1 == 'O':
                self.turn(2)
                continue
        if self.lobby[0] == 'exit':
            return


g = Game()
g.play()
