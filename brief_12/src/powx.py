#!/bin/python
import sys

class Tournament():
    ''' Code to run the tournament
    '''

    games = [
        dict(path="brief19-NovaAgency/app/",
             name= "Nova",
             module_name="game",
             class_name="Game",
             url="git@github.com:CLiNTPELiX/brief19-NovaAgency.git"),
        dict(path="brief19_connect4/classes",
             name="AI connect",
             module_name="plateau",
             class_name="Plateau",
             url="https://github.com/jpphi/brief19_connect4"),
        dict(path="connectx/",
             name="red 3",
             module_name="connect4",
             class_name="Connect4",
             url="git@github.com:archenju/connectx.git"),
        dict(path="puissance4/",
             name="green 4",
             module_name="ConnectFour1",
             class_name="Game",
             url="https://github.com/WiemHAD/puissance4"),
    ]

    def __init__(self):
        # Load all modules and classes from game repos
        for g in self.games:
            sys.path.append(g["path"])
            module = __import__(g["module_name"])
            g['class'] = getattr(module, g["class_name"])
            # test instanciantion
            g['class']()

    def run(self):
        ''' One tournament round. Everyone play againt each other 100 times.
        '''
        match_per_round = 100
        tournament_shape = (len(self.games), len(self.games))
        # There are 3 features in the last dimension:
        # [i][j][0] -> games[i] number of wins
        # [i][j][1] -> games[j] number of wins
        # [i][j][2] -> match nul
        result = np.zeros((tournament_shape[0], tournament_shape[1], 3))
        for i in range(np.multiply(tournament_shape)):
            # get the line and column index from the flat index
            c, l = np.unravel_index(i, tournament_shape)
            if c == l:
                # Don't run match against oneself
                continue

            game1 = self.games[l]["class"]("dqnxr")
            game2 = self.games[c]["class"]("dqnxr")
            res = self.match(game1, game2, match_per_round)
            result[c, l, res] += 1

        print("Tournament result")
        # @TODO: Sumarize the result in a table
        print(result)

    def match(self, game1, game2, nruns=1):
        '''Returns
            1 game1 win
            2 game2 win
            3 nul
        '''
        i = 0
        board = None
        while i < nruns:
            state, reward, terminal = game1.play_one(1, game1.player1, game2.get_board())
            if reward == 1:
                return 1
            if terminal:
                return 3

            state, reward, terminal = game2.play_one(-1, game2.player1, game1.get_board())
            if reward == 1:
                return 2
            if terminal:
                return 0

            i += 1

        return 0


class MyGame():

    '''Connect4 Main Interface'''

    def __init__(self, mode:str, line=6, col=7, power=4):
        '''
        mode: a str that encode the game mode in the form MxM where M can be a value among:
            h: Human player
            r: random player
            dqn: DQN player
        line: number of lines in the board
        col: number of columns in the board
        power: size of the power to win the game
        '''
        modes = mode.split("x")
        self.reset()
        self.player1 = self.get_player(modes[0])
        self.player2 = self.get_player(modes[1])

        self.line = line
        self.col = col
        self.power = 4

    def get_player(self, mode):
        if mode == "h":
            return MyPlayer() # HumanPlayer()
        elif mode == "r":
            return MyPlayer() # RandomtPlayer()
        elif mode == "dqn":
            return MyPlayer() # DqnAgent()

    def reset(self):
        '''Reset the board.'''
        self.board = np.zeros(self.line, self.col)

    def get_board(self):
        '''Returns the array representing the board.'''
        return self.board

    def play_one(self, value, player, board=None):
        '''Play_one (value, player, [board]) -> returns the new state, the reward and the terminal state.'''
        if board is None:
            board = self.board

        action = player.act(board)
        return player.play(value, action, board)


class MyPlayer():

    def act(self, state):
        '''Return the action of a player in a given state.'''
        pass
        return a

    def play(self, value, a, state):
        '''Return the state, reward, terminale of the application of a given action.

        Params
        ------
        a: the action play by a player (the colulns in the connect4)
        value: the value of the action (+1/-1)
        * The player play the action "a" (with value "value") into the environement (i.e. the board)
        * modifier l'état courant (état du plateau) en fonction de l'action `a`

        Returns
        -------
        next_state: état du plateau de jeu après l'application de l'action `a`
                    (@DEBUG;: plus maintenant avec la version play_one) ET de la réponse de l'adversaire (random par exemple)

        reward (int):
           1: gagné
           0: autre cas

        terminal (Bool): jeux terminé (True) ou en-cours (False)
        '''
        pass
        return next_state, reward, terminal

#
# Train loop example (pseudo code)
#

def train():

    game = MyGame("dqnxr")
    dqn_agent = game.player1

    for game in range(1000):
        cur_state = game.reset()
        for step in range(1000):
            # Interact with the environement and get the reward.
            new_state, reward, terminal = game.play_one(1, dqn_agent)
            if not terminal:
                new_state, reward, terminal = game.play_one(-1, game.player2)
                reward = -reward

            # train the player
            dqn_agent.remember(cur_state, action, reward, new_state, terminal)
            dqn_agent.replay()       # internally iterates default (prediction) model
            dqn_agent.target_train() # iterates target model


            cur_state = new_state
            if terminal:
                # Save weights sometimes
                # save data (to txt file for exemple): win/loose stats, hyperparameter, loss.
                break

if __name__ == "__main__":

    t = Tournament()
    t.run()
