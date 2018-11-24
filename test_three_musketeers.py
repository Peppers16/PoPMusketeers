import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 = [[_, _, _, M, _],
          [_, _, R, M, _],
          [_, R, M, R, _],
          [_, R, _, _, _],
          [_, _, _, R, _]]

set_board(board1)


def test_create_board():
    create_board()
    assert at((0, 0)) == R
    assert at((0, 4)) == M
    # eventually add at least two more test cases


def test_set_board():
    set_board(board1)
    assert at((0, 0)) == _
    assert at((1, 2)) == R
    assert at((1, 3)) == M
    # eventually add some board2 and at least 3 tests with it


def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    # eventually add at least one more test with another board


def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == (0, 0)
    # eventually add at least one more exception test and two more
    # test with correct inputs


def test_location_to_string():
    assert location_to_string((0, 0)) == 'A1'
    assert location_to_string((1, 1)) == 'B2'
    assert location_to_string((4, 0)) == 'E1'
    assert location_to_string((0, 4)) == 'A5'


def test_at():
    set_board(board1)
    assert at((0, 0)) == _
    assert at((0, 3)) == M
    assert at((1, 2)) == R


def test_all_locations():
    assert all_locations()[0] == (0, 0)
    assert all_locations()[5] == (1, 0)
    assert all_locations()[24] == (4, 4)


def test_adjacent_location():
    assert adjacent_location((0, 1), left) == (0, 0)
    assert adjacent_location((2, 2), down) == (3, 2)


def test_is_legal_move_by_musketeer():
    set_board(board1)
    assert is_legal_move_by_musketeer((0, 3), up) is False
    assert is_legal_move_by_musketeer((0, 3), down) is False
    assert is_legal_move_by_musketeer((1, 3), left) is True
    # later: test non-musketeer exception


def test_is_legal_move_by_enemy():
    set_board(board1)
    assert is_legal_move_by_enemy((2, 1), right) is False
    assert is_legal_move_by_enemy((2, 1), down) is False
    assert is_legal_move_by_enemy((2, 1), up) is True
    # later: add non-enemy exception


def test_is_legal_move():
    set_board(board1)
    assert is_legal_move((3, 1), up) is False


def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((0, 3)) is False


def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') is True
    assert has_some_legal_move_somewhere('R') is True
    # Eventually put at least three additional tests here
    # with at least one additional board


def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((0, 3)) == ['left', 'right']


def test_is_legal_location():
    set_board(board1)
    assert is_legal_location((0, 3)) is True
    assert is_legal_location((0, 5)) is False
    assert is_legal_location((5, 0)) is False


def test_is_within_board():
    set_board(board1)
    assert is_within_board((0, 3), up) is False
    assert is_within_board((0, 3), left) is True


def test_all_possible_moves_for():
    set_board(board1)
    assert ((1, 3), left) in all_possible_moves_for('M')
    assert ((1, 3), up) not in all_possible_moves_for('M')
    assert ((2, 3), right) in all_possible_moves_for('R')
    assert ((2, 3), left) not in all_possible_moves_for('R')


def test_make_move():
    set_board(board1)
    make_move((1, 3), left)
    assert at((1, 3)) == _
    assert at((1, 2)) == M


def test_choose_computer_move():
    # Check for Musketeer players
    set_board(board1)
    choice = choose_computer_move(M)
    assert is_legal_location(choice[0])
    assert is_legal_move(choice)
    # Check for enemy players
    set_board(board1)
    choice = choose_computer_move(R)
    assert is_legal_location(choice[0])
    assert is_legal_move(choice)


def test_is_enemy_win():
    set_board(board1)
    assert not is_enemy_win()
