import random
import math

def state(N, M):
    return {(i, j): 0 for i in range(N) for j in range(M)}

def update_state(board, move, piece, count_list):
    board[(count_list[move], move)] = piece

def all_possible_moves(count_list, N, M):
    return [i for i in range(M) if count_list[i] != N]

def scoring_method(board, piece, N, M, X):
    def check_sequence(seq):
        if seq.count(piece) == X:
            if piece == 1:
                return 100
            elif piece == 2:
                return -100
        elif seq.count(piece) == X - 1 and seq.count(0) == 1:
            if piece == 1:
                return 10
            elif piece == 2:
                return -50
        return 0

    score = 0
    for row in range(N):
        for col in range(M - X + 1):
            score += check_sequence([board[(row, col + i)] for i in range(X)])
    for row in range(N - X + 1):
        for col in range(M):
            score += check_sequence([board[(row + i, col)] for i in range(X)])
    for row in range(N - X + 1):
        for col in range(M - X + 1):
            score += check_sequence([board[(row + i, col + i)] for i in range(X)])
    for row in range(N - X + 1):
        for col in range(X - 1, M):
            score += check_sequence([board[(row + i, col - i)] for i in range(X)])
    return score

def best_move(board, count_list, my_piece, N, M, X):
    best_score = -math.inf
    best_move = None
    for move in all_possible_moves(count_list, N, M):
        sim_board = board.copy()
        update_state(sim_board, move, my_piece, count_list)
        score = scoring_method(sim_board, my_piece, N, M, X)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

print("ready")

N,M,F,X,T = input("").strip().split(" ")
N = int(N)
M = int(M)
F = int(F)
X = int(X)
T = float(T)
count_list = [0] * M
board = state(N, M)
my_piece = 1
oppo_piece = 2

if F == 0:
    oppo_move = int(input(""))
    update_state(board, oppo_move, oppo_piece, count_list)
    count_list[oppo_move] += 1

while True:
    while True:
        my_move = best_move(board, count_list, my_piece, N, M, X)
        if count_list[my_move] != N:
            update_state(board, my_move, my_piece, count_list)
            count_list[my_move] += 1
            print(my_move)
            break
    oppo_move = int(input(""))
    update_state(board, oppo_move, oppo_piece, count_list)
    count_list[oppo_move] += 1
