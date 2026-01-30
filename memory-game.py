# ---- Imports ----
import random
from tkinter import *
from tkinter import ttk

# ---- Constants ----
# Board
BOARD_HEIGHT = 4
BOARD_WIDTH = 4
NB_PAIRS = (BOARD_HEIGHT * BOARD_WIDTH) // 2

board = [[-1 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

pairs = [i for i in range(NB_PAIRS)] * 2
#print(pairs)

# ---- Functions ----
def fill_board(board, pairs):
    while not pairs == []:
        x = random.randint(0, BOARD_WIDTH-1)
        y = random.randint(0, BOARD_HEIGHT-1)

        if board[x][y] == -1:
            board[x][y] = pairs.pop()
    
    return board

def print_board(board):
    for line in board:
        for value in line:
            print(f"{value} ", end="")
        print()

# ---- Tests ----
board = fill_board(board, pairs)
print_board(board)

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
