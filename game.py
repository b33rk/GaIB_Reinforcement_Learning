class Board:
    def __init__(self):
        self.player = Player()
        self.map = [x for x in range(10)]

class Player:
    def __init__(self):
        self.score = 0
        self.position = 2
        self.endGame = False
    
    def Move(self, x):
        self.position += x

class Game:
    # you can turn on/off the ui with editing cli variable
    def __init__(self, r_learning=None, cli=True):
        self.r_learning = r_learning
        self.cli = cli
    
    def start(self):
        self.board = Board()
        self.player = Player()
        self.step = []

    def next(self):
        if self.cli:
            self.draw()
        
        if self.r_learning:
            next_state, action = self.r_learning.next(self.player.position)
        else:
            action = int(input("Choose your next move (-1 -> left, 1 -> right) : "))
            while action != -1 and action != 1:
                print("Please input move correctly!!")
                action = int(input("Choose your next move (-1 -> left, 1 -> right) : "))
            next_state = self.player.position + action
                
        self.player.Move(action)
        self.updatePlayerScore()
        self.step.append(next_state)
    
    def isWin(self):
        return self.player.score >= 500
    
    def isActionValid(self, action):
        next_position = self.player.position + action
        return next_position >= 0 and next_position < 10

    def updatePlayerScore(self):
        if (self.player.position == 0):
            self.player.score -= 100
            self.player.position = 3
        elif (self.player.position == 9):
            self.player.score += 100
            self.player.position = 3
        else:
            self.player.score -= 1
    
    def isEndGame(self):
        return  self.player.score >= 500 or self.player.score <= -200
    
    def draw(self):
        # Draw the game board
        board_display = ['_' for _ in range(10)]
        board_display[self.player.position] = 'P'
        print("Game Board: " + ' '.join(board_display))

        # Display the player's score
        print(f"Player's Score: {self.player.score}")

        # Check and display if the game is won or lost
        if self.isEndGame():
            if (self.isWin()):
                print("Congratulations! You've won the game!")
            else:
                print("Game Over. You've lost the game.")
        else:
            print("Keep playing!")

    def playGame(self, n_episodes=10000, max_iter_episode=100):
        if (self.r_learning):
            print("Q matrix before training:")
            print(self.r_learning.Q)
            total_step = []
            win_lose = []
            for e in range(n_episodes):
                self.start()
                for i in range(max_iter_episode):
                    self.next()
                    if self.isEndGame():
                        break

                total_step.append(len(self.step))
                win_lose.append(self.isWin())

                if self.r_learning:
                    self.r_learning.updateProba(e)
                if e % (n_episodes // 10) == 0:
                    print(f"Iteration {e}. Step needed:", len(self.step))
                    if self.isWin():
                        print("Win")
                    else:
                        print("Lose")
            
            print("Q matrix after training:")
            print(self.r_learning.Q)

            return total_step, win_lose
        else:
            self.start()
            for i in range(max_iter_episode):
                self.next()
                if self.isEndGame():
                    break
            if not self.isEndGame():
                print("Game Over!!")
                print("You play more than max iteration allowed!!")
