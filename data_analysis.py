N = 6
M = 7

board = {(i, j): 0 for i in range(N) for j in range(M)}
print(board)

for i in range(N):
    for j in range(M):
        cell_value = board[(i, j)]
        print("Value at cell ({}, {}):".format(i, j), cell_value)

        # Modifying a specific cell
        board[(i, j)] = 1
