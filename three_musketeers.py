# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

from random import choice
from copy import deepcopy

# lookups for row in string_to_location and location_to_string functions
row_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
num_to_row = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [[r, r, r, r, m],
             [r, r, r, r, r],
             [r, r, m, r, r],
             [r, r, r, r, r],
             [m, r, r, r, r]]


def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = deepcopy(new_board)  # deep copy used for unit testing; wish to retain 'original' new_board


def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board


def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    # Supplied row (first character: letter) and column (second character: number) are checked separately.
    # This is because of how row uses a dictionary lookup
    if len(s) != 2:
        raise ValueError('Input must be two characters in length: Row (A-E) and Column (1-5)')
    try:
        row = row_to_num[s[0].upper()]
    except KeyError:
        raise ValueError(s[0].upper(), 'is not a valid row. Please give a letter between A and E')
    col = int(s[1]) - 1
    if col not in list(range(0, 5)):
        raise ValueError(s[1], 'is not a valid column. Please give a number between 1 and 5')
    return (row, col)


def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    if not is_legal_location(location):
        raise ValueError('Location not on board. \n \
            Column and Row must both be integers from 0 to 4')
    return num_to_row[location[0]] + str(location[1] + 1)


def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]


def all_locations():
    """Returns a list of all 25 locations on the board."""
    locations = []
    for i in range(0, 5):
        for j in range(0, 5):
            locations.append((i, j))
    return locations


def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    row, column = location
    direction = direction.lower()
    if direction not in ['up', 'down', 'left', 'right']:
        raise ValueError('Direction must be one of: "up","down","left","right"')
    if direction == 'up':
        return (row - 1, column)
    elif direction == 'down':
        return (row + 1, column)
    elif direction == 'left':
        return (row, column - 1)
    elif direction == 'right':
        return (row, column + 1)


def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    if at(location) != 'M':
        raise ValueError('Given location does not contain a Musketeer')
    moving_to = adjacent_location(location, direction)
    # check move legality, THEN contents of destination (otherwise at() will error)
    if is_legal_location(moving_to) and at(moving_to) == 'R':
        return True
    else:
        return False


def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    if at(location) != 'R':
        raise ValueError('Given location does not contain an Enemy')
    moving_to = adjacent_location(location, direction)
    # check move legality, THEN contents of destination (otherwise at() will error)
    if is_legal_location(moving_to) and at(moving_to) == '_':
        return True
    else:
        return False


def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    player = at(location)
    if player == 'M':
        return is_legal_move_by_musketeer(location, direction)
    elif player == 'R':
        return is_legal_move_by_enemy(location, direction)
    else:
        raise ValueError('Given location does not contain a Musketeer or an Enemy')


def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range."""
    for direction in ['up', 'down', 'left', 'right']:
        if is_legal_move(location, direction):
            return True
    return False


def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    for location in all_locations():
        if at(location) == who:
            if can_move_piece_at(location):
                return True
    return False


def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    possible_moves = []
    for direction in ['up', 'down', 'left', 'right']:
        if is_legal_move(location, direction):
            possible_moves.append(direction)
    return possible_moves


def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will always be a pair of integers."""
    return location in all_locations()


def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    moving_to = adjacent_location(location, direction)
    return is_legal_location(moving_to)


def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    possible_moves = []
    for location in all_locations():
        if at(location) == player:
            # list comprehension returns list of tuples containing piece's location with each direction it can move
            possible_moves = possible_moves + [(location, direction) for direction in possible_moves_from(location)]
    return possible_moves


def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    print(board)
    moving_to = adjacent_location(location, direction)
    if at(location) == 'M':
        board[moving_to[0]][moving_to[1]] = 'M'  # piece appears in destination
        board[location[0]][location[1]] = '_'  # former location now empty
    elif at(location) == 'R':
        board[moving_to[0]][moving_to[1]] = 'R'  # piece appears in destination
        board[location[0]][location[1]] = '_'  # former location now empty
    else:
        raise ValueError("Given Location did not contain a piece")
    print(board)


def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    # First implementation simply picks a random, legal move
    return choice(all_possible_moves_for(who))


def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    rows = set()
    cols = set()
    for location in all_locations():
        if at(location) == 'M':
            rows.add(location[0])
            cols.add(location[1])
    # if either rows or cols sets have a length of 1, this indicates that all musketeers shared the same row or column
    # if true for either set, enemy has won
    return len(rows) == 1 or len(cols) == 1


# ---------- Communicating with the user ----------
# ----you do not need to modify code below unless you find a bug
# ----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end=" ")
        for j in range(0, 5):
            print(board[i][j] + " ", end=" ")
        print()
        ch = chr(ord(ch) + 1)
    print()


def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()


def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user


def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""
    directions = {'L': 'left', 'R': 'right', 'U': 'up', 'D': 'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()


def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else:  # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')
        make_move(location, direction)
        describe_move("Musketeer", location, direction)


def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else:  # Computer plays enemy
        (location, direction) = choose_computer_move('R')
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board


def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from', \
          location_to_string(location), 'to', \
          location_to_string(new_location) + ".\n")


def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break
