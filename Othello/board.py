# 12/02/2019
#
# Board Class for Othello Game.
# Support 8x8 weighted AI design.

import turtle
import time

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
        self.title = None
        self.role_lst = [user, "Computer"]

        self.tt_turt = turtle.Turtle()
        self.dr_turt = turtle.Turtle()

        self.tt_turt.speed(0)
        self.dr_turt.speed(0)

        self.tt_turt.hideturtle()
        self.dr_turt.hideturtle()

        self.show_player()
        self.show_exit()

    # PURPOSE
    # Draws the board.
    # SIGNATURE
    # draw_board :: Board => None
    def draw_board(self):

        NUM_SIDES = 4
        RIGHT_ANGLE = 90
        SIDE = 1.35

        turtle.setup(self.size * SQUARE + 2 * SQUARE,
                     (self.size * SQUARE + 2 * SQUARE) * SIDE)
        turtle.screensize(self.size * SQUARE, self.size * SQUARE)
        turtle.bgcolor("white")
        # Create the turtle to draw the board
        self.dr_turt.penup()
        # Line color is black, fill color is green
        self.dr_turt.color("black", "forest green")

        # Move the turtle to the upper left corner
        corner = -self.size * SQUARE / 2
        self.dr_turt.setposition(corner, corner)

        # Draw the green background
        self.dr_turt.begin_fill()
        for i in range(NUM_SIDES):
            self.dr_turt.pendown()
            self.dr_turt.forward(SQUARE * self.size)
            self.dr_turt.left(RIGHT_ANGLE)
        self.dr_turt.end_fill()

        # Draw the horizontal lines
        for i in range(self.size + 1):
            self.dr_turt.setposition(corner, SQUARE * i + corner)
            self.draw_lines()

        # Draw the vertical lines
        self.dr_turt.left(RIGHT_ANGLE)
        for i in range(self.size + 1):
            self.dr_turt.setposition(SQUARE * i + corner, corner)
            self.draw_lines()

        # Draw the 4 start pieces
        self.start_pieces()
        self.show_player()
        # Get the reference to the screen
        screen = turtle.Screen()
        # Listen for click events
        screen.onclick(self.board_click)
        # Stops the window from closing
        turtle.done()

    # PURPOSE
    # Draw the lines on the board
    # SIGNATURE
    # draw_lines :: Board, Turtle, Integer => None
    def draw_lines(self):

        self.dr_turt.pendown()
        self.dr_turt.forward(SQUARE * self.size)
        self.dr_turt.penup()

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

        RADIUS = SQUARE // 2
        COLORS = ("black", "white")

        center = self.get_center(col, row)
        self.dr_turt.penup()
        self.dr_turt.setposition(center[0], center[1])
        self.dr_turt.pendown()
        self.dr_turt.begin_fill()
        self.dr_turt.color("black", COLORS[role])
        self.dr_turt.circle(RADIUS)
        self.dr_turt.end_fill()
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
    # Return and determine validity of given coordinate within board.
    # SIGNATURE
    # bound :: Board, Int, Int => Boolean
    def bound(self, x, y):

        return 0 <= x < self.size and 0 <= y < self.size

    # PURPOSE
    # Display current player on board graph.
    # SIGNATURE
    # show_player :: Board => None
    def show_player(self):

        self.title = 'Current Player: ' + self.role_lst[self.player] + \
            " \n" + "Score: " + str(self.score[0]) + "(B) - " + \
            str(self.score[1]) + "(W)"
        self.show_title("")

    # PURPOSE
    # Display current title on board graph,
    # i.e. current player or game result.
    # SIGNATURE
    # show_title :: Board, String => None
    def show_title(self, title):

        self.tt_turt.clear()
        self.tt_turt.penup()
        self.tt_turt.setpos(0, self.high_bound + SQUARE // 2)
        self.tt_turt.pendown()
        self.tt_turt.color('black')
        self.tt_turt.write(self.title + title, font=STYLE, align='center')

    # PURPOSE
    # Display current feedback on board graph,
    # show validity of current chosen position.
    # SIGNATURE
    # show_feedback :: Board, String => None
    def show_feedback(self, valid, x, y):

        new_fb = "\n" + FEEDBACK[valid] + ": col=" + str(x) + ", row=" + str(y)
        self.show_title(new_fb)

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
    # Return and get a position of board matrix via the given screen position.
    # SIGNATURE
    # matrix_pos :: Board, Int => Int
    def matrix_pos(self, x):
        if x == 0:
            return 0
        return int(x // SQUARE + self.size // 2)

    # PURPOSE
    # Handles mouse clicks on the board. x is the x-coordinate of the mouse
    # click and y is the y-coordinate of the mouse click.
    # SIGNATURE
    # board_click :: Board, Float, Float => None
    def board_click(self, x, y):

        x = self.matrix_pos(x)
        y = self.matrix_pos(y)
        if x == -1 and y == self.size - 1:
            turtle.bye()
        else:
            self.player = USER
            self.show_player()
            move = self.capture(x, y)
            self.show_feedback(move, x, y)
            if move:
                res = self.move_legal()
                if USER in res:
                    res.pop(0)
                if COMPUTER in res:
                    self.player = COMPUTER
                    self.show_player()
                while USER not in res and COMPUTER in res:
                    if COMPUTER in res:
                        res = self.computer_move(res[1])
                self.player = USER
                self.show_player()
                if not res:
                    turtle.bye()

    # PURPOSE
    # Display a computer move, return latest legal moves.
    # SIGNATURE
    # computer_move :: Board => Dict
    def computer_move(self, res):

        x, y = res
        self.show_feedback(self.capture(x, y), x, y)
        return self.move_legal()

    # PURPOSE
    # Display an exit button, allow the user exit game when click it.
    # SIGNATURE
    # show_exit :: Board => None
    def show_exit(self):

        self.dr_turt.penup()
        self.dr_turt.setpos(self.low_bound - SQUARE / 2,
                            self.high_bound - SQUARE / 2)
        self.dr_turt.pendown()
        self.dr_turt.color('black')
        self.dr_turt.write("EXIT", font=STYLE, align='center')

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
