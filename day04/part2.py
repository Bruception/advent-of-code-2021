import sys
file = open(f'{sys.path[0]}/input.txt', 'r')

class Board:
    def __init__(self, board):
        self.n = len(board)
        self.m = len(board[0])
        self.board = board
        self.marked = [[False for j in range(self.m)] for i in range(self.n)]
        self.positions = {}
        self.hasWon = False
        for i in range(self.n):
            for j in range(self.m):
                number = board[i][j]
                self.positions[number] = (i, j)
                self.board[i][j] = int(self.board[i][j])

    def mark(self, number):
        if (number not in self.positions):
            return
        i, j = self.positions[number]
        self.marked[i][j] = True

    def checkWin(self):
        for row in self.marked:
            if (all(marked for marked in row)):
                self.hasWon = True
                return True

        for j in range(self.m):
            col_good = True
            for i in range(self.n):
                col_good &= self.marked[i][j]
            if (col_good):
                self.hasWon = True
                return True

        return False
    
    def getUnmarkedSum(self):
        return sum(self.board[i][j] if not self.marked[i][j] else 0 for j in range(self.m) for i in range(self.n))

number_draws = file.readline().strip().split(',')
boards = []

while (True):
    line = file.readline()
    if (line == ''):
        break
    board = []
    for i in range(5):
        row = file.readline().strip().split()
        board.append(row)
    boards.append(Board(board))

last_winner = None
last_number = 0

for number in number_draws:
    for board in boards:
        if (board.hasWon):
            continue
        board.mark(number)
        if (board.checkWin()):
            last_winner = board
            last_number = int(number)

print(last_winner.getUnmarkedSum() * last_number)
