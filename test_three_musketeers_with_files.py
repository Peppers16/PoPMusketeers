import pytest
from three_musketeers_with_files import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '_'

board1 = [[_, _, _, M, _],
          [_, _, R, M, _],
          [_, R, M, R, _],
          [_, R, _, _, _],
          [_, _, _, R, _]]

# enemy win
board2 = [[_, _, _, R, _],
          [_, _, _, _, _],
          [M, _, M, _, M],
          [_, _, _, R, _],
          [_, _, _, _, _]]

# musketeer win
board3 = [[_, _, _, _, _],
          [_, _, _, _, _],
          [_, _, _, _, _],
          [_, _, M, _, _],
          [_, M, R, M, _]]

set_board(board1)


def test_create_board():
    create_board()
    assert at((0, 0)) == R
    assert at((0, 4)) == M
    # test board is full of enemies, except for the 3 known musketeer locations
    for i, location in enumerate(all_locations()):
        if i in [4, 12, 20]:
            assert at(location) == M
        else:
            assert at(location) == R


def test_set_board():
    set_board(board1)
    assert at((0, 0)) == _
    assert at((1, 2)) == R
    assert at((1, 3)) == M
    set_board(board2)
    assert at((0, 3)) == R
    assert at((2, 0)) == M
    assert at((2, 2)) == M
    assert at((2, 4)) == M


def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    set_board(board2)
    assert board2 == get_board()


def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == (0, 0)
    with pytest.raises(ValueError):
        string_to_location('A6')
    with pytest.raises(ValueError):
        string_to_location('A12')
    with pytest.raises(ValueError):
        string_to_location('B22')
    assert string_to_location('E5') == (4, 4)
    assert string_to_location('B2') == (1, 1)


def test_location_to_string():
    assert location_to_string((0, 0)) == 'A1'
    assert location_to_string((1, 1)) == 'B2'
    assert location_to_string((4, 0)) == 'E1'
    assert location_to_string((0, 4)) == 'A5'
    assert location_to_string((4, 4)) == 'E5'
    assert location_to_string((1, 1)) == 'B2'


def test_at():
    set_board(board1)
    assert at((0, 0)) == _
    assert at((0, 3)) == M
    assert at((1, 2)) == R
    assert at((4, 1)) == _
    assert at((4, 3)) == R


def test_all_locations():
    assert all_locations()[0] == (0, 0)
    assert all_locations()[5] == (1, 0)
    assert all_locations()[24] == (4, 4)
    assert len(all_locations()) == 25


def test_adjacent_location():
    assert adjacent_location((0, 1), left) == (0, 0)
    assert adjacent_location((2, 2), down) == (3, 2)
    assert adjacent_location((0, 0), right) == (0, 1)
    assert adjacent_location((0, 0), down) == (1, 0)
    assert adjacent_location((4, 4), up) == (3, 4)
    assert adjacent_location((4, 4), left) == (4, 3)
    assert adjacent_location((2, 2), up) == (1, 2)


def test_is_legal_move_by_musketeer():
    set_board(board1)
    assert is_legal_move_by_musketeer((0, 3), up) is False
    assert is_legal_move_by_musketeer((0, 3), down) is False
    assert is_legal_move_by_musketeer((1, 3), left) is True
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((1, 2), up)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((1, 2), right)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((0, 0), right)

def test_is_legal_move_by_enemy():
    set_board(board1)
    assert is_legal_move_by_enemy((2, 1), right) is False
    assert is_legal_move_by_enemy((2, 1), down) is False
    assert is_legal_move_by_enemy((2, 1), up) is True
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((1, 3), left)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((0, 0), right)

def test_is_legal_move():
    set_board(board1)
    assert is_legal_move((3, 1), up) is False
    assert is_legal_move((3, 1), right) is True
    assert is_legal_move((1, 3), up) is False
    assert is_legal_move((1, 3), left) is True
    assert is_legal_move((4, 3), down) is False

def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((0, 3)) is False
    assert can_move_piece_at((1, 3)) is True
    assert can_move_piece_at((1, 2)) is True

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') is True
    assert has_some_legal_move_somewhere('R') is True
    set_board(board2)
    assert has_some_legal_move_somewhere('M') is False
    assert has_some_legal_move_somewhere('R') is True
    set_board(board3)
    assert has_some_legal_move_somewhere('M') is True
    assert has_some_legal_move_somewhere('R') is False


def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((2, 2)) == ['up', 'left', 'right']
    assert possible_moves_from((0, 3)) == []
    assert possible_moves_from((4, 3)) == ['up', 'left', 'right']
    set_board(board3)
    assert possible_moves_from((4, 2)) == []
    assert possible_moves_from((4, 1)) == ['right']


def test_is_legal_location():
    set_board(board1)
    assert is_legal_location((0, 3)) is True
    assert is_legal_location((0, 0)) is True
    assert is_legal_location((4, 4)) is True
    assert is_legal_location((0, 5)) is False
    assert is_legal_location((5, 0)) is False
    assert is_legal_location((1.5, 0)) is False  # test float
    assert is_legal_location((-1, 0)) is False  # test negative int
    assert is_legal_location((1, -1)) is False


def test_is_within_board():
    set_board(board1)
    assert is_within_board((0, 3), up) is False
    assert is_within_board((0, 3), left) is True
    assert is_within_board((4, 4), right) is False
    assert is_within_board((4, 4), down) is False
    assert is_within_board((4, 4), left) is True
    assert is_within_board((4, 4), up) is True


def test_all_possible_moves_for():
    set_board(board1)
    assert ((1, 3), left) in all_possible_moves_for('M')
    assert ((1, 3), up) not in all_possible_moves_for('M')
    assert ((2, 3), right) in all_possible_moves_for('R')
    assert ((2, 3), left) not in all_possible_moves_for('R')
    # comprehensive test
    set_board(board3)
    assert all_possible_moves_for('M') == [((3, 2), down), ((4, 1), right), ((4, 3), left)]
    assert all_possible_moves_for('R') == []


def test_make_move():
    set_board(board1)
    make_move((1, 3), left)
    assert at((1, 3)) == _
    assert at((1, 2)) == M
    # test enemy
    set_board(board1)
    make_move((1, 2), up)
    assert at((1, 2)) == _
    assert at((0, 2)) == R
    assert possible_moves_from((0, 3)) == ['left']  # Musketeer should now be able to move
    # test non-piece
    set_board(board1)
    with pytest.raises(ValueError):
        make_move((0, 0), right)


def test_choose_computer_move():
    # Check for Musketeer players
    set_board(board1)
    choice = choose_computer_move(M)
    assert is_legal_location(choice[0])
    assert is_legal_move(*choice)
    # Check for enemy players
    set_board(board1)
    choice = choose_computer_move(R)
    assert is_legal_location(choice[0])
    assert is_legal_move(*choice)


def test_is_enemy_win():
    set_board(board1)
    assert not is_enemy_win()
    set_board(board2)
    assert is_enemy_win()  # enemy win board
    set_board(board3)
    assert not is_enemy_win()


def test_save_delete_exists():
    set_board(board1)
    save_state(get_board())
    assert save_exists() == True
    delete_save()
    assert save_exists() == False
    # currently save_games directory must before function is used. Suggest adding a 'create_save_directory' function
    # in future iterations

def test_load_state():
    set_board(board1)
    save_state(get_board())
    assert load_state() == board1

def test_delete_state():
    if save_exists():
        delete_save()
        assert not save_exists()
