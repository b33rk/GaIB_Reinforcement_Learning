import numpy as np
from qlearn import Qlearn
from sarsa import SARSA
from game import Game
import matplotlib.pyplot as plt

def Play_Game(next=None):
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
    exit = False
    while not exit:
        print("1. Normal")
        print("2. Reinforcement Learning")
        mode = int(input("Pilih mode permainan: "))

        cli = True
        if mode == 1:
            r_learning = None
        elif mode == 2:
            print("1. Qlearning")
            print("2. SARSA")
            r_learning = int(input("Pilih jenis reinforcement learning (1 atau 2): "))
            Cli = input("Apakah ingin menampilkan UI ketika training? (y/n) ")
            if next != 2:
                Q = np.zeros((10,2))
            if Cli == "n":
                cli = False
            print("=====================================================")
            print("Terdapat 6 parameter:")
            print("(Num Episodes, Max Episode, Exploration Proba, Gamma, Min Exploration Proba, Exploration Decreasing Decay)")
            print("Isi parameter secara berurutan: (harus diisi semua, dipisah dengan koma tanpa spasi, isi -1 jika default)")
            user_input = input()
            params = user_input.split(',')
            params = [float(x) for x in params]

        if r_learning == 1:
            r_learning = Qlearn(Q, R, *params[2:])
        elif r_learning == 2:
            r_learning = SARSA(Q, R, *params[2:])

        game = Game(cli=cli, r_learning=r_learning)
        total_step, win_lose = game.playGame(*params[:2])

        if r_learning:

            isVisualization = input("Apakah ingin menampilkan visualisasi hasil training? (y/n) ")
            if isVisualization == "y":
                colors = ['green' if wl else 'red' for wl in win_lose]

                plt.figure(figsize=(12, 6))

                plt.scatter(range(len(total_step)), total_step, c=colors, s=5)
                plt.title('Qlearn Total Step vs Iteration')
                plt.xlabel('Iteration')
                plt.ylabel('Total Step')

                plt.show()
        
        print("1. Ulangi permainan dari Nol")
        print("2. Ulangi permainan dengan Q disimpan")
        print("3. Exit")
        next = int(input("Pilih apa yang mau kamu lakukan: "))
        if next == 3:
            exit = True

Play_Game()