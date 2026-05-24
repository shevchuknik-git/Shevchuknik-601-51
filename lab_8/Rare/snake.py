import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.root.resizable(False, False)
        
        self.current_player = "X"
        
        self.board = [""] * 9
        
        self.buttons = []
        
        self.create_board()

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    self.root, text="", font=('Arial', 40, 'bold'), 
                    width=5, height=2, bg="white",
                    command=lambda r=i, c=j: self.on_click(r, c)
                )
                btn.grid(row=i, column=j, padx=2, pady=2)
                row.append(btn)
            self.buttons.append(row)

        reset_btn = tk.Button(
            self.root, text="Перезапустить игру", 
            font=('Arial', 14), bg="lightgray",
            command=self.reset_game
        )
        reset_btn.grid(row=3, column=0, columnspan=3, sticky="we", pady=5, padx=2)

    def on_click(self, row, col):
        index = row * 3 + col
        
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            
            color = "blue" if self.current_player == "X" else "red"
            self.buttons[row][col].config(text=self.current_player, fg=color)

            if self.check_winner():
                messagebox.showinfo("Конец игры", f"Игрок {self.current_player} победил!")
            elif "" not in self.board:
                messagebox.showinfo("Конец игры", "Ничья!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                self.highlight_winner(combo)
                return True
        return False

    def highlight_winner(self, combo):
        for index in combo:
            row = index // 3
            col = index % 3
            self.buttons[row][col].config(bg="lightgreen")

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", bg="white")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
