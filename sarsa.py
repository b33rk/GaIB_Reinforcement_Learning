import numpy as np
import random as rd

class SARSA:
    def __init__(self, Q, R, exploration_proba=1, gamma=0.99, min_exploration_proba = 0.01, exploration_decreasing_decay = 0.001):
        self.Q = Q
        self.R = R
        self.exploration_proba = exploration_proba
        self.gamma = gamma
        self.min_exploration_proba = min_exploration_proba
        self.exploration_decreasing_decay = exploration_decreasing_decay
        
    def next(self, position):
        current_position = position
        if np.random.uniform(0,1) < self.exploration_proba:
            action = rd.randint(0,1)
            next_action = rd.randint(0,1)
        else:
            action = np.argmax(self.Q[current_position,:])
            next_action = np.argmax(self.Q[current_position,:])

        if action:
            next_state = current_position + 1
        else:
            next_state = current_position - 1
        
        score = self.getScore(current_position, action)
        self.updateQValue(self.Q, 0.8, current_position, action, score, next_state, next_action)
        return next_state, action if action == 1 else -1
    
    def getScore(self, state, action):
        return self.R[state][action]
    
    def updateQValue(self, Q, lr, current_position, action, score, next_state, next_action):
        Q[current_position][action] = (1-lr) * Q[current_position][action] + lr *(score + self.gamma * Q[next_state, next_action])

    def updateProba(self, e):
        self.exploration_proba = max(self.min_exploration_proba, np.exp(-self.exploration_decreasing_decay*e))