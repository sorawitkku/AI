import random
import math
import time

def state(N,M):
    board_dict = {(row, col): 0 for row in range(N) for col in range(M)}
    return board_dict

def validmove(state,count_list,move):
    if state[(count_list[move],move)] != 0:
        return False
    else:
        return True

def minimax(state, depth, maximizing):
    pass


def bestmove():
    score = -math.inf

print("ready")

N,M,F,X,T = input("").strip().split(" ")
N = int(N)
M = int(M)
F = int(F)
T = float(T)
count_list = [0] * M

state = state(N,M)

if F == 0:
    oppo_move = int(input(""))
    state[(count_list[oppo_move],oppo_move)] = 'o'
    count_list[oppo_move] +=1

while True:
    while True:
        my_move = random.randint(0,M-1)
        if count_list[my_move] != N:
            state[(count_list[my_move],my_move)] = 'x'
            count_list[my_move] += 1
            print(my_move)
            break
    oppo_move = int(input(""))
    count_list[oppo_move] +=1