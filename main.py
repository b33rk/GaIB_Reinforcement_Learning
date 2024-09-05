import numpy as np
from qlearn import Qlearn
from sarsa import SARSA
from game import Game
import matplotlib.pyplot as plt

R = []    
for i in range(10):
    line = []
    if (i - 1 < 0):
        line.append(0)
    elif (i - 1 == 0):
        line.append(-100)
    else:
        line.append(-1)
    if (i + 1 < 0):
        line.append(0)
    elif (i + 1 == 9):
        line.append(100)
    else:
        line.append(-1)
    R.append(line)

Q = np.zeros((10,2))
qlearn = Qlearn(Q, R)
sarsa = SARSA(Q, R)

game1 = Game(cli=True, r_learning=qlearn)
total_step_1, win_lose_1 = game1.playGame()
game2 = Game(r_learning=sarsa, cli=False)
total_step_2, win_lose_2 = game2.playGame()

# Convert win_lose to colors
colors_1 = ['green' if wl else 'red' for wl in win_lose_1]
colors_2 = ['green' if wl else 'red' for wl in win_lose_2]

# Create a figure with two subplots side by side
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot for total_step_1
axs[0].scatter(range(len(total_step_1)), total_step_1, c=colors_1, s=5)
axs[0].set_title('Qlearn Total Step vs Iteration')
axs[0].set_xlabel('Iteration')
axs[0].set_ylabel('Total Step')

# Plot for total_step_2
axs[1].scatter(range(len(total_step_2)), total_step_2, c=colors_2, s=5)
axs[1].set_title('SARSA Total Step vs Iteration')
axs[1].set_xlabel('Iteration')
axs[1].set_ylabel('Total Step')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()