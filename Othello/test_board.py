# 12/02/2019
#
# Test for Othello game.
# Based on Board Class for testing version.


from board_for_test import Board


def test_get_center():
    b = Board(4, "user")
    assert(b.get_center(0, 0) == (-50.0, -75.0))
    assert(b.get_center(1, 0) == (0.0, -75.0))
    assert(b.get_center(2, 0) == (50.0, -75.0))
    assert(b.get_center(3, 3) == (100.0, 75.0))


def test_draw_piece():
    b = Board(4, "user")
    b.draw_piece(1, 1, 0)
    b.draw_piece(3, 1, 1)
    assert(b.get_m(1, 1) == 0)
    assert(b.get_m(3, 1) == 1)
    assert(b.get_m(2, 1) == 2)
    assert(b.get_m(1, 2) == 2)
    assert(b.get_m(3, 2) == 2)
    assert(b.get_m(2, 2) == 2)


def test_start_pieces():
    b = Board(4, "user")
    b.start_pieces()
    assert(b.get_m(2, 1) == 1)
    assert(b.get_m(1, 2) == 1)
    assert(b.get_m(2, 2) == 0)
    assert(b.get_m(1, 1) == 0)
    assert(b.get_m(3, 3) == 2)
    assert(b.get_m(1, 3) == 2)


def test_bound():
    b = Board(4, "user")
    assert(b.bound(0, 0) is True)
    assert(b.bound(1, 0) is True)
    assert(b.bound(2, 0) is True)
    assert(b.bound(3, 0) is True)
    assert(b.bound(3, 3) is True)
    assert(b.bound(3, 4) is False)
    assert(b.bound(4, 0) is False)
    assert(b.bound(110, 0) is False)


def test_get_board_value():
    b = Board(4, "user")
    b.draw_board()
    assert(b.get_m(1, 1) == 0)
    assert(b.get_m(1, 2) == 1)
    assert(b.get_m(2, 1) == 1)
    assert(b.get_m(2, 2) == 0)
    assert(b.get_m(2, 3) == 2)
    assert(b.get_m(3, 2) == 2)
    assert(b.get_m(3, 3) == 2)


def test_set_board_value():
    b = Board(4, "user")
    b.set_m(1, 1, 0)
    b.set_m(3, 1, 1)
    assert(b.get_m(1, 1) == 0)
    assert(b.get_m(3, 1) == 1)
    assert(b.get_m(2, 1) == 2)


def test_get_empty():
    b = Board(4, "user")
    cnt = 4**2
    emp = b.get_empty()
    assert(len(emp) == cnt)

    b.draw_board()
    cnt -= 4
    emp = b.get_empty()
    assert(len(emp) == cnt)

    b.set_m(0, 0, 0)
    cnt -= 1
    emp = b.get_empty()
    assert(len(emp) == cnt)

    b.set_m(0, 0, 1)
    emp = b.get_empty()
    assert(len(emp) == cnt)

    b.set_m(0, 0, 2)
    cnt += 1
    emp = b.get_empty()
    assert(len(emp) == cnt)


def test_get_winner():
    b = Board(4, "user")
    assert(b.score == [0, 0])
    b.start_pieces()
    assert(b.score == [2, 2])
    b.draw_piece(0, 0, 0)
    assert(b.score == [3, 2])
    b.draw_piece(3, 3, 1)
    assert(b.score == [3, 3])
    b.draw_piece(0, 0, 1)
    assert(b.score == [2, 4])
    b.draw_piece(3, 3, 1)
    assert(b.score == [2, 4])
    b.draw_piece(3, 3, 0)
    assert(b.score == [3, 3])


def test_flip():
    b = Board(4, "user")
    b.draw_piece(0, 0, 0)
    b.draw_piece(1, 1, 1)
    assert(b.get_m(0, 0) == 0)
    assert(b.get_m(1, 1) == 1)
    assert(b.get_m(2, 2) == 2)

    flip_s = set([(1, 1), (2, 2)])
    b.player = 0
    b.flip(flip_s)
    assert(b.get_m(0, 0) == 0)
    assert(b.get_m(1, 1) == 0)
    assert(b.get_m(2, 2) == 0)

    flip_s = set([(1, 1), (2, 2)])
    b.player = 1
    b.flip(flip_s)
    assert(b.get_m(0, 0) == 0)
    assert(b.get_m(1, 1) == 1)
    assert(b.get_m(2, 2) == 1)

    flip_s = set([(0, 0), (1, 1), (2, 2)])
    b.player = 1
    b.flip(flip_s)
    assert(b.get_m(0, 0) == 1)
    assert(b.get_m(1, 1) == 1)
    assert(b.get_m(2, 2) == 1)

    flip_s = set([(0, 0), (1, 1), (2, 2)])
    b.player = 0
    b.flip(flip_s)
    assert(b.get_m(0, 0) == 0)
    assert(b.get_m(1, 1) == 0)
    assert(b.get_m(2, 2) == 0)


def test_capture():
    b = Board(4, "user")
    b.draw_piece(0, 0, 0)
    b.draw_piece(0, 1, 1)
    b.draw_piece(1, 1, 1)
    b.draw_piece(1, 2, 1)
    b.draw_piece(2, 0, 0)
    b.draw_piece(2, 2, 0)
    b.player = 0
    b.capture(0, 2)
    assert(b.get_m(0, 0) == 0)
    assert(b.get_m(0, 1) == 0)
    assert(b.get_m(0, 2) == 0)
    assert(b.get_m(1, 1) == 0)
    assert(b.get_m(1, 2) == 0)
    assert(b.get_m(2, 0) == 0)
    assert(b.get_m(2, 2) == 0)


def test_move_legal():
    b = Board(4, "user")
    b.player = 0
    res = b.move_legal()
    assert(res == {})
    b.draw_piece(0, 0, 0)
    b.draw_piece(0, 1, 1)
    res = b.move_legal()
    assert(res == {0: (0, 2)})
    b.draw_piece(0, 0, 1)
    b.draw_piece(0, 1, 0)
    res = b.move_legal()
    assert(res == {1: (0, 2)})
    b.draw_piece(0, 0, 0)
    b.draw_piece(0, 1, 1)
    b.draw_piece(1, 1, 0)
    res = b.move_legal()
    assert(res == {0: (0, 2), 1: (2, 1)})


# def main():
#     test_get_center()
#     test_draw_piece()
#     test_start_pieces()
#     test_get_empty()
#     test_get_winner()
#     test_bound()
#     test_get_board_value()
#     test_set_board_value()
#     test_flip()
#     test_capture()
#     test_move_legal()


# main()
