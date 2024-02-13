import sys
import time

co = 3
ro = 3

f = 2
s = 3
# Dictionary representation
board_dict = {(row, col): 0 for row in range(ro) for col in range(co)}
print("Memory usage for dictionary representation:", sys.getsizeof(board_dict))
board_dict[(f,s)] = 4
print(board_dict)