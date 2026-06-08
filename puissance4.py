import copy

class Puissance4:
    def __init__(self, first_player):
        self.board = [[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],]
        self.player = first_player # at first, player is first player
        self.nb_actions = 0 # nb actions played

    def display(self):
        nb_lines = len(self.board)
        nb_col = len(self.board[0])
        for i in range(nb_lines):
            for j in range(nb_col):
                print(" |", end="")
                if self.board[i][j] == 0:
                    print("   ", end="")
                elif self.board[i][j] == 1:
                    print(" x ", end="")
                else:
                    print(" o ", end="")
            print(" |")

        for k in range(nb_col):
            print(" ", k, " ", end="")
        print()


