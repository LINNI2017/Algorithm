# 12/02/2019
#
# PURPOSE
# Play an Othello Game, prompt user to enter a name,
# report player and score to a score file, sort descendingly.
# Draw Othello board with Turtle and allow user to play via
# clicking on the board.


from os import path
from board import Board
SCORE_FILE = "scores.txt"
SIZE = 8


# PURPOSE
# Write player and score to the given file,
# append and sort all score pairs.
# SIGNATURE
# draw_board :: List, String => None
def write_score(score, fname):

    lines = None
    if path.exists(fname):
        read = open(fname, "r+")
        lines = [line.rstrip('\n').split(" ") for line in read]
        lines.append(score)
        lines.sort(key=lambda x: (-int(x[1]), x[0]))
        read.truncate(0)
        read.close()
    else:
        lines = [score]

    write = open(fname, "a")
    for i in lines:
        s = " ".join(i) + "\n"
        write.write(s)
    write.close()


def main():

    user = input("Enter your name to start Othello: ")
    b = Board(SIZE, user)
    b.draw_board()
    print("{}(B:{}) - {}(W:COMPUTER)".format(b.score[0], user, b.score[1]))
    print(b.get_winner())
    write_score([user, str(b.score[0])], SCORE_FILE)


main()
