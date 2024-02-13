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
    
def scoring_method(state, N, M, player, oppo,X):
    def check_sequence(seq):
        if seq.count(player) == X:
            return 100
        elif seq.count(player) == X-1 and seq.count(0) == 1 :
            return 10
        elif seq.count(oppo) == X:
            return -100
        elif seq.count(oppo) == X-1 and seq.count(0) == 1 :
            return -50
        return 0 
    score = 0
    for row in range(N):
        for col in range(M - X + 1):
                score += check_sequence(state[(row, col + i)] for i in range(X))
    for row in range(N - X + 1):
        for col in range(M):
            score += check_sequence(state[(row, col + i)] for i in range(X))
    for row in range(N - X + 1):
        for col in range(M - X + 1):
            score += check_sequence(state[(row, col + i)] for i in range(X))
    for row in range(N - X + 1):
        for col in range(X - 1, M):
            score += check_sequence(state[(row, col + i)] for i in range(X))
    return score


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
    print(state)

while True:
    while True:
        my_move = random.randint(0,M-1)
        if count_list[my_move] != N:
            state[(count_list[my_move],my_move)] = 'x'
            count_list[my_move] += 1
            print(my_move)
            break
    oppo_move = int(input(""))
    state[(count_list[oppo_move],oppo_move)] = 'o'
    count_list[oppo_move] +=1
    print(state)