import random

class GameBoard:
    def __init__(self):
        # 3x3 üres tábla létrehozása (None értékekkel)
        self.board = [[None, None, None], 
                      [None, None, None], 
                      [None, None, None]]
        self.current_player = "X"  # A játékos kezd (X)

    def display_board(self):
        # Tábla megjelenítése a terminálban
        for row in self.board:
            print([cell if cell is not None else "-" for cell in row])
        print("\n")

    def make_move(self, row, col):
        # Lépés megvalósítása, ha az adott hely üres
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self):
        # Ellenőrzés, hogy van-e győztes (sorok, oszlopok, átlók)
        # Sorok ellenőrzése
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return row[0]
        
        # Oszlopok ellenőrzése
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                return self.board[0][col]

        # Átlók ellenőrzése
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]

        return None

    def is_draw(self):
        # Ellenőrzi, hogy minden cella foglalt-e, és nincs győztes
        for row in self.board:
            if None in row:
                return False
        return True

    def switch_player(self):
        # Játékos váltása
        self.current_player = "O" if self.current_player == "X" else "X"

    def ai_move(self):
        # AI véletlenszerűen választ egy üres cellát
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] is None]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = self.current_player
