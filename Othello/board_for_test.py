# 12/02/2019
#
# Board Class for testing Othello Game.
# Support 8x8 weighted AI design.


USER = 0
COMPUTER = 1
EMPTY = 2
SQUARE = 50
STYLE = ("Arial", 20, "normal")
FEEDBACK = ("Invalid", "Valid")
DIRECT = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
WEIGHTS = [[4, -3, 2, 2, 2, 2, -3, 4],
           [-3, -4, -1, -1, -1, -1, -4, -3],
           [2, -1, 1, 0, 0, 1, -1, 2],
           [2, -1, 0, 1, 1, 0, -1, 2],
           [2, -1, 0, 1, 1, 0, -1, 2],
           [2, -1, 1, 0, 0, 1, -1, 2],
           [-3, -4, -1, -1, -1, -1, -4, -3],
           [4, -3, 2, 2, 2, 2, -3, 4]]


class Board:

    # PURPOSE
    # Constructor for the Board class. size should be an even integer.
    # SIGNATURE
    # __init__ :: Board, Integer => Board
    def __init__(self, size, user):

        self.size = size
        self.high_bound = SQUARE * size / 2
        self.low_bound = 0 - self.high_bound
        self.player = USER
        self.matrix = [[EMPTY] * size for x in range(size)]
        self.score = [0, 0]
        self.role_lst = [user, "Computer"]

    # PURPOSE
    # Return the center coordinates of a square on the board.
    # SIGNATURE
    # get_center :: Board, Integer, Integer => (Float, Float)
    def get_center(self, col, row):

        x = col * SQUARE + SQUARE + self.low_bound
        y = (row * SQUARE + SQUARE / 2) + self.low_bound
        return (x, y)

    # PURPOSE
    # Draw a tile of a given color in a given square on the board.
    # SIGNATURE
    # draw_piece :: Board, Integer, Integer, String => None
    def draw_piece(self, col, row, role):

        cur = self.get_m(col, row)
        if cur != role:
            opp = int(role == USER)
            if cur == opp:
                self.score[opp] -= 1
            self.score[role] += 1
            self.set_m(col, row, role)

    # PURPOSE
    # Draws the 4 starting pieces on the board.
    # SIGNATURE
    # start_pieces :: Board => None
    def start_pieces(self):

        center_small = self.size // 2 - 1
        center_large = self.size // 2
        # Puts the start pieces in position
        self.draw_piece(center_small, center_large, COMPUTER)
        self.draw_piece(center_large, center_small, COMPUTER)
        self.draw_piece(center_large, center_large, USER)
        self.draw_piece(center_small, center_small, USER)

    # PURPOSE
    # Return and determine validity of given coordinate within board.
    # SIGNATURE
    # bound :: Board, Int, Int => Boolean
    def bound(self, x, y):

        return 0 <= x < self.size and 0 <= y < self.size

    # PURPOSE
    # Return and determine whether the chosen position can capture
    # opponent's piece, by surrounding opponent with self piece.
    # SIGNATURE
    # capture :: Board, Int, Int => Boolean
    def capture(self, x, y):

        flipped = False
        if self.bound(x, y) and self.get_m(x, y) == EMPTY:
            opp = int(self.player == USER)
            for i, j in DIRECT:
                dx, dy = x + i, y + j
                if self.bound(dx, dy) and self.get_m(dx, dy) == opp:
                    flip_s = set()
                    flip_s.add((x, y))
                    while self.bound(dx, dy):
                        btw = self.get_m(dx, dy)
                        if btw == self.player:
                            self.flip(flip_s)
                            flipped = True
                            break
                        elif btw == EMPTY:
                            break
                        else:
                            flip_s.add((dx, dy))
                        dx, dy = dx + i, dy + j
        return flipped

    # PURPOSE
    # Flip the given set piece into another color.
    # SIGNATURE
    # flip :: Board, Set => None
    def flip(self, flip_s):

        opp = int(self.player == USER)
        for i, j in flip_s:
            cur = self.get_m(i, j)
            if cur != self.player:
                self.draw_piece(i, j, self.player)

    # PURPOSE
    # Return and get board value at the given position.
    # SIGNATURE
    # get_m :: Board, Int, Int => Int
    def get_m(self, x, y):

        return self.matrix[self.size - 1 - y][x]

    # PURPOSE
    # Set board value at the given position.
    # SIGNATURE
    # set_m :: Board, Int, Int => None
    def set_m(self, x, y, val):

        self.matrix[self.size - 1 - y][x] = val

    # PURPOSE
    # Return and get a sorted list of empty spaces on the board,
    # sort by weights descendingly.
    # SIGNATURE
    # get_empty :: Board => List
    def get_empty(self):

        emp = []
        for i in range(self.size):
            for j in range(self.size):
                if self.get_m(i, j) == EMPTY:
                    emp.append((WEIGHTS[i][j], i, j))
        emp.sort(reverse=True)
        return emp

    # PURPOSE
    # Display game result on board graph.
    # i.e. black or white or tie.
    # SIGNATURE
    # get_winner :: Board => String
    def get_winner(self):

        win = "TIE"
        if self.score[0] < self.score[1]:
            win = self.role_lst[1]
        elif self.score[0] > self.score[1]:
            win = self.role_lst[0]
        else:
            return win
        return "Winner is {}!".format(win)

    # PURPOSE
    # Draws the board.
    # SIGNATURE
    # draw_board :: Board => None
    def draw_board(self):

        NUM_SIDES = 4
        RIGHT_ANGLE = 90

        # Draw the 4 start pieces
        self.start_pieces()

    # PURPOSE
    # Return a string, represent the board in matrix string.
    # SIGNATURE
    # to_string :: Board => String
    def to_string(self):

        size = len(self.matrix)
        s = ""
        for i in range(size):
            s += str(size - 1 - i) + " " + \
                ",".join([str(j) for j in self.matrix[i]]) + "\n"
        s += "  " + " ".join([str(i % 10) for i in range(size)]) + "\n"
        return s

    # PURPOSE
    # Return and get a Dict of legal moves on the board,
    # for both user and computer players.
    # SIGNATURE
    # move_legal :: Board => Dict
    def move_legal(self):

        res = {}
        emp = self.get_empty()
        for w, x, y in emp:
            if len(res) > 1:
                break
            for i, j in DIRECT:
                if len(res) > 1:
                    break
                dx, dy = x + i, y + j
                if self.bound(dx, dy):
                    opp = self.get_m(dx, dy)
                    if opp == EMPTY:
                        continue
                    cur = int(opp == USER)
                    if cur in res:
                        continue
                    dx, dy = dx + i, dy + j
                    while self.bound(dx, dy):
                        btw = self.get_m(dx, dy)
                        if btw == cur:
                            res[cur] = (x, y)
                            break
                        elif btw == EMPTY:
                            break
                        dx, dy = dx + i, dy + j
        return res
