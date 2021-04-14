
# Code sample for the tournament...

game1 = Connect4()
game2 = Pow4()

def match(game1, game2):

    i = 0
    board = None
    while i < 1000:

        state, reward, terminal = game1.play_one(1, game1.player1, game2.get_board())
        if reward == 1:
            return 1
        if terminal:
            return 0

        state, reward, terminal = game2.play_one(-1, game2.player1, game1.get_board())
        if reward == 1:
            return -1
        if terminal:
            return 0

        i += 1


''' Connect4 Api

Game
----
-> reset () -> reset the board
-> get_board () -> returns the array representing the board.
-> play_one (value, player, [board]) -> returns the new state, the reward and the terminal state.

Player
------
-> act (state) -> return the action of a player in given state.
-> play (value, action) -> return the state, reward, terminale of the application of a given action.
'''


class Game():

    def __init__(self):
        self.reset()
        self.player1 = Player("human") # Use case example
        self.player2 = Player("dqn_bot")

    def reset(self):
        self.board = np.zeros(...)

    def get_board(self):
        return self.board

    def play_one(self, value, player, board=None):
        if board is None:
            board = self.board

        action = player.act(board)
        return player.play(value, action)


class Player():

    def act(self, state):
        ...
        return a

    def play(self, value, a):
        '''
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
        return next_state, reward, terminal

#
# Train loop example (pseudo code)
#

def train():
    for game in range(1000):
        cur_state = game.reset()
        for step in range(1000):

            new_state, reward, terminal = game.play_one(1, game.player1)
            if not terminal:
                new_state, reward, terminal = game.play_one(-1, game.player2)
                reward = -reward

            # train the player
            dqn_agent.remember(cur_state, action, reward, new_state, terminal)
            dqn_agent.replay()       # internally iterates default (prediction) model
            dqn_agent.target_train() # iterates target model

            cur_state = new_state
            if terminal:
                break

