from puissance4 import *

puissance4 = Puissance4(1)
puissance4.display()
"""
print("==========================")
print(puissance4.actions(puissance4.board))

puissance4.board = puissance4.result(puissance4.board, 2, 1)
puissance4.display()


moves = puissance4.actions(puissance4.board)
index = puissance4.minimax(puissance4.board, puissance4.player)

# with index we do the best move found
state = puissance4.result(puissance4.board, index, puissance4.player)
if puissance4.player:
    puissance4.player = -1
else:
    puissance4.player = 1
    puissance4.board = copy.deepcopy(state)

    puissance4.display()


#IA_Decision(puissance4)

puissance4.display()

"""
def main_game():
    game_loop = True
    turn = int(input("Entrez quel joueur commence en premier (-1 = Joueur | 1 = IA) :"))
    game = Puissance4(turn)
    while not game.align4(game.board)[0]:
        game.display()
        if turn == -1:
            print("Au tour du Joueur :")
            move = int(input("Entrez une colonne :"))
            game.board = game.result(game.board, move, -1)
            turn = 1
        if turn == 1:
            move = game.IA_Decision(game.board,1) #on va choisir le vrai move avec l'IA du morpion après
            print("L'IA joue la colonne", move)
            game.board = game.result(game.board, move, 1)
            turn = -1
        game.display()
    winner = game.align4(game.board)[1] #idéalement align4 renvoie un tuple (bool, gagnant)
    print("Partie terminée.")
    if winner is None:
        print("egalite")
    elif winner == 1:
        print("L'IA gagné")
    elif winner == -1:
        print("Le joueur a gagné")

main_game()









    def Terminal_Test(self, state):
        if self.nb_actions == 42: return True # full board
        # use align4
        # return True or false
        return self.align4(state)[0]

    def align4(self, state):
        nb_lines = len(self.board)
        nb_cols = len(self.board[0])

        # lignes
        for i in range(nb_lines):
            for j in range(nb_cols-3):
                player = self.board[i][j]
                if player != 0 and all(self.board[i][j + k] == player for k in range(4)):
                    return True, state[i][j]

        # col
        for i in range(nb_lines-3):
            for j in range(nb_cols):
                player = self.board[i][j]
                if player != 0 and all(self.board[i + k][j] == player for k in range(4)):
                    return True, state[i][j]

        # check diagonals
        for line in range(nb_lines - 3):
            for col in range(nb_cols - 3):
                if self.board[line][col] != 0:
                    # diagonale droite
                    if self.board[line][col] == self.board[line + 1][col + 1] == self.board[line + 2][
                        col + 2] == self.board[line + 3][col + 3]:
                        return True, state[line][col]
                    # diagonale gauche
                    if self.board[line][col] == self.board[line - 1][col - 1] == self.board[line - 2][
                        col - 2] == self.board[line - 3][col - 3]:
                        return True, state[line][col]
        return (False, None)

    def utility(self, state):
        if self.Terminal_Test(state):
            gagnant = self.align4(state)[1]
            if gagnant is None:
                return 0
            elif gagnant == 1:
                return 1
            else:
                return -1
        print("the game still runs")
        return


    def max_value(self, state):
        if self.Terminal_Test(state):
            return self.utility(state)
        v = -10e8
        if len(self.actions(state)) % 2 == 0:
            player = -1
        else:
            player = 1
        for move in self.actions(state):
            v = max(v, self.min_value(self.result(state, move, player)))

        #print("v return max=", v)
        #print("state max", state)
        #print("----------------------------")
        return v

    def min_value(self, state):
        if self.Terminal_Test(state):
            return self.utility(state)
        v = 10e8
        if len(self.actions(state)) % 2 == 0:
            player = -1
        else:
            player = 1
        for move in self.actions(state):
            v = min(v, self.max_value(self.result(state, move, player)))

        #print("v return min=", v)
        #print("state min", state)
        return v



    def IA_Decision(self, state, player):
        num_best_move = 0

        if player:
            best_move = -10
            for move in self.actions(state):
                score = self.min_value(self.result(state, move, 1))
                if score > best_move:
                    best_move = score
                    num_best_move = move
        """
        else:
            best_move = 10
            for move in self.actions(state):
                score = self.max_value(self.result(state, move, -1))
                if score < best_move:
                    best_move = score
                    num_best_move = move"""
        return num_best_move

#def IA_Decision(game, player):
    #game.minimax(game.board, player)

"""
def minimax_decision(game):
    #find the best action for max
    return max(game.actions(), key=lambda a: min_value(game.result(a, 1)))


def min_value(game):
    if game.Terminal_Test():
        return game.utility()
    v = float('inf')
    for a in game.actions():
        v = min(v, max_value(game.result(a, -1)))
    return v

def max_value(game):
    if game.Terminal_Test():
        return game.utility()
    v = float('-inf')
    for a in game.actions():
        v = max(v, min_value(game.result(a, 1)))
    return v


def play(g):
    #switch player until the end of the game
    current = 1
    while not g.Terminal_Test():
        a = minimax_decision(g)
        g.state[current].append(a)
        if g.player == 1:
            g.player = -1
        else:
            g.player = 1
    g.display()
"""
