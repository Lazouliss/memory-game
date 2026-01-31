# ---- Imports ----
import random
from tkinter import *
from tkinter import ttk
import time

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
    def update_buttons(self, x, y, btn):
        if self.last_revealed.cget('text') == btn.cget('text'):
            # TODO: ajouter un temps d'attente ici (pour animation)
            self.last_revealed.destroy()
            self.last_revealed = None
            btn.destroy()
            return
        
        self.last_revealed.config(text="?")
        self.last_revealed = None
        btn.config(text="?")
        # TODO: add check of length of "buttons" to check for victory --> also add a counter to show the number of pairs already found

    def click_tile(self, x, y):
        btn = self.buttons[(x, y)]
        print(f"Clicked : {x}, {y} -> {self.board[x][y]}")
        # Check if the button is already revealed
        # TODO: ajouter un check pour savoir si un click est en cours (car le after n'est pas bloquant donc on peut enchainer les clics)
        if btn.cget('text') != "?":
            return
        # Reaveal tile
        btn.config(text=str(self.board[x][y]))
        if not self.last_revealed:
            print("no revealed tiles")
            self.last_revealed = btn
            return      # No tiles currently revealed, nothing more to do
        
        self.root.after(500, lambda: self.update_buttons(x, y, btn))       # show the value for at least one second
        
    
    
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
