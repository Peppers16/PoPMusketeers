import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

set_board(new_board)

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases

set_board(new_board)

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    
    #eventually add some board2 and at least 3 tests with it

set_board(new_board)

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

set_board(new_board)

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs

set_board(new_board)

def test_location_to_string():
    assert location_to_string((0,0)) == 'A1'
    assert location_to_string((1,1)) == 'B2'
    assert location_to_string((4,0)) == 'E1'
    assert location_to_string((0,4)) == 'A5'

set_board(new_board)

def test_at():
    pass
    # Replace with tests

set_board(new_board)

def test_all_locations():
    pass
    # Replace with tests

set_board(new_board)

def test_adjacent_location():
    pass
    # Replace with tests

set_board(new_board)

def test_is_legal_move_by_musketeer():
    pass
    # Replace with tests

set_board(new_board)

def test_is_legal_move_by_enemy():
    pass
    # Replace with tests

set_board(new_board)

def test_is_legal_move():
    pass
    # Replace with tests

set_board(new_board)

def test_can_move_piece_at():
    pass
    # Replace with tests

set_board(new_board)

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

set_board(new_board)

def test_possible_moves_from():
    pass
    # Replace with tests

set_board(new_board)

def test_is_legal_location():
    pass
    # Replace with tests

set_board(new_board)

def test_is_within_board():
    pass
    # Replace with tests

set_board(new_board)

def test_all_possible_moves_for():
    pass
    # Replace with tests

set_board(new_board)

def test_make_move():
    pass
    # Replace with tests

set_board(new_board)

def test_choose_computer_move():
    pass
    # Replace with tests; should work for both 'M' and 'R'

set_board(new_board)

def test_is_enemy_win():
    pass
    # Replace with tests


