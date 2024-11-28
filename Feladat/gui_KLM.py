import tkinter as tk
from tkinter import messagebox
from logic import GameBoard

class TicTacToeGUIKLM:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.game = GameBoard()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        # Létrehozzuk a 3x3 gombokat
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2,
                                   command=lambda r=row, c=col: self.player_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def player_move(self, row, col):
        # Játékos lépésének kezelése
        if self.game.make_move(row, col):
            self.buttons[row][col].config(text=self.game.current_player)
            winner = self.game.check_winner()
            if winner:
                self.show_winner_klm(winner)
            elif self.game.is_draw():
                self.show_winner_klm("Döntetlen")
            else:
                self.game.switch_player()
                self.ai_move()

    def ai_move(self):
        # AI lépés kezelése
        self.game.ai_move()
        for row in range(3):
            for col in range(3):
                if self.game.board[row][col] is not None:
                    self.buttons[row][col].config(text=self.game.board[row][col])

        winner = self.game.check_winner()
        if winner:
            self.show_winner(winner)
        elif self.game.is_draw():
            self.show_winner("Döntetlen")
        else:
            self.game.switch_player()

    def show_winner_klm(self, winner):
        # Győztes kijelzése és új játék indítási lehetőség
        result = f"Győztes: {winner}" if winner != "Döntetlen" else "Döntetlen!"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state="disabled")
        messagebox.showinfo("Játék vége", result)
        self.reset_board()

    def reset_board(self):
        # Tábla alaphelyzetbe állítása az új játékhoz
        self.game = GameBoard()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state="normal")

# Főprogram indítása
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUIKLM(root)
    root.mainloop()
