class ConnectFour:
    def __init__(self, width=7, height=6, goal=4):
        self.width = width
        self.height = height
        self.goal = goal
        self.board = [0, 0]  # [bitboard for player 1, bitboard for player 2]
        self.player = 0
        self.moves = [0] * width  # Number of moves played in each column

    def make_move(self, col):
        if not self.is_valid_move(col):
            return False

        self.board[self.player] |= (1 << (col * (self.height + 1) + self.moves[col]))
        self.moves[col] += 1
        self.player ^= 1  # Switch player
        return True

    def is_valid_move(self, col):
        return self.moves[col] < self.height

    def has_won(self, player):
        directions = [1, self.height, self.height + 1, self.height + 2]
        bitboard = self.board[player]

        for direction in directions:
            bb = bitboard & (bitboard >> direction)
            if bb & (bb >> (2 * direction)):
                return True
        return False

    def print_board(self):
        for row in range(self.height - 1, -1, -1):
            for col in range(self.width):
                pos = 1 << (col * (self.height + 1) + row)
                if self.board[0] & pos:
                    print("1", end=" ")
                elif self.board[1] & pos:
                    print("2", end=" ")
                else:
                    print(".", end=" ")
            print("\n", end="")

        print('-' * 13)
        print(" ".join(map(str, range(self.width))))

    def play(self):
        self.print_board()
        total_moves = 0  # Add a variable to count total moves played
        while True:
            try:
                col = int(input(f"Player {self.player + 1}, choose a column: "))
                if self.is_valid_move(col):
                    self.make_move(col)
                    total_moves += 1  # Increment the total moves counter
                    if self.has_won(self.player ^ 1):
                        print(f"Player {self.player ^ 1 + 1} wins!")
                        break
                    elif total_moves == self.width * self.height:  # Check for draw
                        print("It's a draw!")
                        break
                    self.print_board()
            except:
                continue

if __name__ == "__main__":
    game = ConnectFour()
    game.play()