# ---- Imports ----
import random
from tkinter import *
from tkinter import ttk

# ---- Constants ----
# Board
BOARD_HEIGHT = 4
BOARD_WIDTH = 4
NB_PAIRS = (BOARD_HEIGHT * BOARD_WIDTH) // 2

# ---- Classes ----
class MemoryGame:
    # TODO: add last revealed tile attribute + logic
    def __init__(self, root):
        self.root = root
        self.buttons = {}
        self.board = []
        self.last_revealed = None
        self.create_board_view()
    
    # ---- Functions ----
    def start_game(self):
        self.root.mainloop()

    # -- Button functions --
    def click_tile(self, x, y):
        btn = self.buttons[(x, y)]
        print(f"Clicked : {x}, {y} -> {self.board[x][y]}")
        # TODO: check if the tile is already revealed
        btn.config(text=str(self.board[x][y]))
        # TODO: check for matches
    
    # -- Board functions --
    # View
    def create_board_view(self):
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        
        for i in range(4):
            for j in range(4):
                btn = ttk.Button(frm, text="?", command=lambda x=i, y=j: self.click_tile(x, y))
                btn.grid(column=j, row=i)
                self.buttons[(i, j)] = btn
    
    # Logic
    def create_board(self, width, height):
        self.board = [[-1 for _ in range(width)] for _ in range(height)]

    def fill_board(self, pairs):
        while not pairs == []:
            x = random.randint(0, BOARD_WIDTH-1)
            y = random.randint(0, BOARD_HEIGHT-1)

            if self.board[x][y] == -1:
                self.board[x][y] = pairs.pop()

    def init_board(self, width, height, nb_pairs):
        pairs = [i for i in range(nb_pairs)] * 2
        self.create_board(width, height)
        self.fill_board(pairs)

    def print_board(self):
        for line in self.board:
            for value in line:
                print(f"{value} ", end="")
            print()


# ---- Main ----
if __name__ == '__main__':
    game = MemoryGame(Tk())

    game.init_board(BOARD_WIDTH, BOARD_HEIGHT, NB_PAIRS)
    game.print_board()      # Debugging

    game.start_game()
