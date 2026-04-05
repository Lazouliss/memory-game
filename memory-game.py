# ---- Imports ----
import random
from tkinter import *
from tkinter import ttk
# for tests
import sys

# ---- Constants ----
# Board
BOARD_HEIGHT = 2
BOARD_WIDTH = 2
NB_PAIRS = (BOARD_HEIGHT * BOARD_WIDTH) // 2

# ---- Classes ----
class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.buttons = {}
        self.board = []
        self.last_revealed_pos = None
        self.create_board_view()
    
    # ---- Functions ----
    def start_game(self):
        self.root.mainloop()

    def check_victory(self):
        print("Checking victory...")
        if len(self.buttons) == 0:
            label = ttk.Label(self.root, text="Victory!")
            label.grid(column=0, row=5)
            btn_quit = ttk.Button(self.root, text="Quit", command=self.root.destroy)
            btn_quit.grid(column=0, row=6)

    # -- Button functions --
    def update_buttons(self, x, y, btn):
        last_revealed_btn = self.buttons[self.last_revealed_pos]

        if last_revealed_btn.cget('text') == btn.cget('text'):
            # Match found, remove the buttons
            self.buttons.pop((x, y))
            self.buttons.pop(self.last_revealed_pos)
            self.last_revealed_pos = None

            # TODO: don't shrink the board, just hide the buttons (or at least keep the board size the same)
            # does not work so i should just use a fixed size for the window : https://github.com/Lazouliss/memory-game/issues/2
            last_revealed_btn.destroy()
            btn.destroy()

            self.check_victory()
            return
        
        last_revealed_btn.config(text="?")
        self.last_revealed_pos = None
        btn.config(text="?")
        # TODO: add a counter to show the number of pairs already found : https://github.com/Lazouliss/memory-game/issues/1

    def click_tile(self, x, y):
        btn = self.buttons[(x, y)]
        print(f"Clicked : {x}, {y} -> {self.board[x][y]}")
        # Check if the button is already revealed
        # TODO: ajouter un check pour savoir si un click est en cours (car le after n'est pas bloquant donc on peut enchainer les clics) : https://github.com/Lazouliss/memory-game/issues/3
        if btn.cget('text') != "?":
            return
        # Reveal tile
        btn.config(text=str(self.board[x][y]))
        if not self.last_revealed_pos:
            print("no revealed tiles")
            self.last_revealed_pos = (x, y)
            return      # No tiles currently revealed, nothing more to do
        
        self.root.after(500, lambda: self.update_buttons(x, y, btn))       # show the value for a short time
        
    
    
    # -- Board functions --
    # View
    def create_board_view(self):
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        
        for i in range(BOARD_WIDTH):
            for j in range(BOARD_HEIGHT):
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
    # Change the value of the board size if passed in arguments
    if len(sys.argv) == 3:
        BOARD_WIDTH = int(sys.argv[1])
        BOARD_HEIGHT = int(sys.argv[2])

    game = MemoryGame(Tk())

    game.init_board(BOARD_WIDTH, BOARD_HEIGHT, NB_PAIRS)
    game.print_board()      # Debugging

    game.start_game()
