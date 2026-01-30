# ---- Imports ----
import random
from tkinter import *
from tkinter import ttk

# ---- Constants ----
# Board
BOARD_HEIGHT = 4
BOARD_WIDTH = 4
NB_PAIRS = (BOARD_HEIGHT * BOARD_WIDTH) // 2

# ---- Functions ----
def create_board(width, height):
    board = [[-1 for _ in range(width)] for _ in range(height)]
    return board

def fill_board(board, pairs):
    while not pairs == []:
        x = random.randint(0, BOARD_WIDTH-1)
        y = random.randint(0, BOARD_HEIGHT-1)

        if board[x][y] == -1:
            board[x][y] = pairs.pop()
    
    return board

def create_board_view(board):
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    for i, line in enumerate(board):
        for j, value in enumerate(line):
            ttk.Button(frm, text=str(value)).grid(column=j, row=i)

    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=j, row=i+1)

    return root

def print_board(board):
    for line in board:
        for value in line:
            print(f"{value} ", end="")
        print()

# ---- Variables ----
board = create_board(BOARD_WIDTH, BOARD_HEIGHT)
pairs = [i for i in range(NB_PAIRS)] * 2

# ---- Tests ----
board = fill_board(board, pairs)
print_board(board)

root = create_board_view(board)
root.mainloop()
