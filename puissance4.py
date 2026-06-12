import copy
import random
import timeit

NB_ACTIONS = 0  # utilisée en tant que variable globale pour compter les coups

class Puissance4:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]


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


def actions(board):
    """
    Finds all the actions possible to play
    """
    nb_cols = len(board[0])
    moves = []
    for i in range(nb_cols):
        if board[0][i] == 0:  # check that the upper line is not full
            moves.append(i)  # if upper line has 0 --> possible to add something
    return moves

def result(board, move, player):
    """
    Return the board updated with the move and the player specified in parameters
    """
    # move corresponds to num col
    new_board = copy.deepcopy(board)
    nb_lines = len(new_board)
    for i in range(nb_lines-1, -1, -1):
        if new_board[i][move] == 0:
            new_board[i][move] = player # player is 1 or -1
            return new_board
    print("column ", move, "full")
    return new_board


def choose_random_move(board):
    """
    Choose a move randomly (when it's the AI's turn)
    """
    moves_allowed = actions(board)
    index_move = random.randint(0, len(moves_allowed)-1)
    return moves_allowed[index_move]

def terminal_test(board):
    """
    Verify if the game has ended (bool)
    """
    if align4(board):
        return True
    if board_full():
        return True
    return False


def board_full():
    """
    Verify if 42 actions have occurred (bool)
    """
    global NB_ACTIONS
    if NB_ACTIONS == 42:
        print("----FULL BOARD----")
        return True
    return False

def align4(board):
    """
    Verify if 4 chips are aligned (line, column or diagonal) (bool)
    """
    nb_lines = len(board)
    nb_cols = len(board[0])

    # line
    for line in range(nb_lines):
        for col in range(nb_cols - 3):
            player = board[line][col]
            if player != 0 and all(board[line][col + k] == player for k in range(4)):
                print("---- WINNER :", player , "----")
                return True

    # col
    for line in range(nb_lines - 3):
        for col in range(nb_cols):
            player = board[line][col]
            if player != 0 and all(board[line + k][col] == player for k in range(4)):
                print("---- WINNER :", player, "----")
                return True

    # diag
    for line in range(nb_lines - 3):
        for col in range(nb_cols):
            player = board[line][col]
            if player != 0 and all(board[line + k][col + k] == player for k in range(4)): # diag droite
                print("---- WINNER :", player, "----")
                return True
            if player != 0 and all(board[line + k][col - k] == player for k in range(4)): # diag gauche
                print("---- WINNER :", player, "----")
                return True
    return False


def main_game():
    global NB_ACTIONS
    game_loop = True
    turn = int(input("Enter which player plays first (-1 = You | 1 = AI) :"))
    game = Puissance4()
    game.display()
    while game_loop:
        if turn == -1:
            print()
            move = int(input("Your turn ! Enter column :"))
            game.board = result(game.board, move, -1)
            turn = 1
        elif turn == 1:
            move = choose_random_move(game.board) #on va choisir le vrai move avec l'IA du morpion après
            print("AI plays column n°", move)
            game.board = result(game.board, move, 1)
            turn = -1
        NB_ACTIONS += 1 # incrémenter compteur d'actions
        game.display()
        if terminal_test(game.board):
            print("// END GAME \\\ ")
            game_loop = False



if __name__ == "__main__":
    b = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
    print(timeit.timeit(lambda: align4(b), number=100))

    main_game()
