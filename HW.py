import random
import math
global N,M,F,X,T,count_list

def state():
    return {(i, j): 0 for i in range(N) for j in range(M)}

def update_state(board,move,piece):
    board[(count_list[move], move)] = piece

def all_posible_move():
    return [i for i in range(M) if count_list[i] != N]

def scoring_method(piece):
    def check_sequence(seq):
        if seq.count(piece) == int(X):
            if piece == 1 :
                return 100
            elif piece == 2 :
                return -100
        elif seq.count(piece) == int(X)-1 and seq.count(0) == 1 :
            if piece == 1 :
                return 10
            elif piece == 2 :
                return -50
        return 0 
    score = 0
    for row in range(N):
        for col in range(M - int(X) + 1):
                score += check_sequence(state[(row, col + i)] for i in range(int(X)))
    for row in range(N - int(X) + 1):
        for col in range(M):
            score += check_sequence(state[(row, col + i)] for i in range(int(X)))
    for row in range(N - int(X) + 1):
        for col in range(M - int(X) + 1):
            score += check_sequence(state[(row, col + i)] for i in range(int(X)))
    for row in range(N - int(X) + 1):
        for col in range(int(X) - 1, M):
            score += check_sequence(state[(row, col + i)] for i in range(int(X)))
    return score

def best_move(board, piece):
    best_score = -math.inf
    best_move = None
    for move in all_posible_move():
        sim_board = board.copy()
        update_state(sim_board, move, piece)
        score = scoring_method(piece)
        if score > best_score :
            best_score = score
            best_move = move
    return best_move



print("ready")

N,M,F,X,T = input("").strip().split(" ")
N = int(N)
M = int(M)
F = int(F)
T = float(T)
count_list = [0] * M
board = state()
my_piece = 1
oppo_piece = 2


if F == 0:
    oppo_move = int(input(""))
    update_state(board,oppo_move,oppo_piece)
    count_list[oppo_move] +=1
    

while True:
    while True:
        my_move = best_move(board,my_piece)
        if count_list[my_move] != N:
            update_state(board,my_move,my_piece)
            count_list[my_move] += 1
            print(my_move)
            break
    oppo_move = int(input(""))
    update_state(board,oppo_move,oppo_piece)
    count_list[oppo_move] +=1
