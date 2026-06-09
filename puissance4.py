import copy
import random


class Puissance4:
    def __init__(self, first_player):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
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

    def actions(self, board):
        """
        Finds all the actions possible to play
        """
        nb_cols = len(self.board[0])
        moves = []
        for i in range(nb_cols):
            if board[0][i] == 0:  # check that the upper line is not full
                moves.append(i)  # if upper line has 0 --> possible to add something
        return moves


    def result(self, board, move, player):
        """
        Return the board updated with the move and the player specified in parameters
        """
        # move corresponds to num col
        new_board = copy.deepcopy(board)
        nb_lines = len(self.board)
        for i in range(nb_lines-1, -1, -1):
            if new_board[i][move] == 0:
                new_board[i][move] = player # player is 1 or -1
                return new_board
        print("column ", move, "full")
        return new_board

    def choose_random_move(self):
        """
        Choose a move randomly (when it's the AI's turn)
        """
        moves_allowed = self.actions(self.board)
        index_move = random.randint(0, len(moves_allowed)-1)
        return moves_allowed[index_move]


def main_game():
    game_loop = True
    turn = int(input("Entrez quel joueur commence en premier (-1 = Joueur | 1 = IA) :"))
    game = Puissance4(turn)
    game.display()
    while game_loop:
        if turn == -1:
            print("Au tour du Joueur :")
            move = int(input("Entrez une colonne :"))
            game.board = game.result(game.board, move, -1)
            turn = 1
        if turn == 1:
            move = game.choose_random_move() #on va choisir le vrai move avec l'IA du morpion après
            print("L'IA joue la colonne", move)
            game.board = game.result(game.board, move, 1)
            turn = -1
        game.display()
        game_loop = int(input("Continuer ?"))



if __name__ == "__main__":
    main_game()
    """
    game = Puissance4(1)
    game.display()
    print(game.actions(game.board))
    next_move = game.choose_random_move()
    print("next move", next_move)
    game.board = game.result(game.board, next_move, 1)
    game.display()"""
