import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.root.resizable(False, False)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        
        self.init_db()
        self.create_board()

    def init_db(self):
        """Создает таблицу для истории игр, если она не существует."""
        self.conn = sqlite3.connect("tictactoe_history.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                winner TEXT,
                date TEXT
            )
        ''')
        self.conn.commit()

    def on_closing(self):
        """Корректно закрывает соединение с БД перед выходом."""
        if hasattr(self, 'conn'):
            self.conn.close()
        self.root.destroy()

    def save_result(self, winner):
        """Сохраняет результат игры в БД."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO games (winner, date) VALUES (?, ?)", (winner, current_time))
        self.conn.commit()

    def show_stats(self):
        """Отображает статистику побед из БД."""
        self.cursor.execute("SELECT winner, COUNT(*) FROM games GROUP BY winner")
        stats = self.cursor.fetchall()
        
        if not stats:
            messagebox.showinfo("Статистика", "История игр пока пуста.")
            return
            
        stat_msg = "Статистика игр:\n\n"
        for row in stats:
            winner_name = row[0] if row[0] != "Draw" else "Ничья"
            stat_msg += f"{winner_name}: {row[1]} раз(а)\n"
            
        messagebox.showinfo("Статистика", stat_msg)

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
        reset_btn.grid(row=3, column=0, columnspan=3, sticky="we", pady=2, padx=2)
        
        stats_btn = tk.Button(
            self.root, text="Статистика", 
            font=('Arial', 14), bg="lightblue",
            command=self.show_stats
        )
        stats_btn.grid(row=4, column=0, columnspan=3, sticky="we", pady=2, padx=2)

    def on_click(self, row, col):
        index = row * 3 + col
        
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            
            color = "blue" if self.current_player == "X" else "red"
            self.buttons[row][col].config(text=self.current_player, fg=color)

            if self.check_winner():
                self.save_result(self.current_player)
                messagebox.showinfo("Конец игры", f"Игрок {self.current_player} победил!")
            elif "" not in self.board:
                self.save_result("Draw")
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