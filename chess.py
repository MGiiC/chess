
import time

LAT_LIMIT = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]  # Sets board
LONG_LIMIT = ['1', '2', '3', '4', '5', '6', '7', '8', ]  # boundaries.

turn = 'White'  # Current player turn.

the_board = {  # All board locations with peices stored as values.
    'a8': 'b_rook1', 'b8': 'b_knight1', 'c8': 'b_bishop1', 'd8': 'b_queen', 
    'e8': 'b_king', 'f8': 'b_bishop2', 'g8': 'b_knight2', 'h8': 'b_rook2', 
    'a7': 'b_pawn1', 'b7': 'b_pawn2', 'c7': 'b_pawn3', 'd7': 'b_pawn4', 
    'e7': 'b_pawn5', 'f7': 'b_pawn6', 'g7': 'b_pawn7', 'h8': 'b_pawn8', 
    'a6': '', 'b6': '', 'c6': '', 'd6': '', 
    'e6': '', 'f6': '', 'g6': '', 'h6': '', 
    'a5': '', 'b5': '', 'c5': '', 'd5': '', 
    'e5': '', 'f5': '', 'g5': '', 'h5': '', 
    'a4': '', 'b4': '', 'c4': '', 'd4': '', 
    'e4': '', 'f4': '', 'g4': '', 'h4': '', 
    'a3': '', 'b3': '', 'c3': '', 'd3': '', 
    'e3': '', 'f3': '', 'g3': '', 'h3': '', 
    'a2': 'w_pawn1', 'b2': 'w_pawn2', 'c2': 'w_pawn3', 'd2': 'w_pawn4', 
    'e2': 'w_pawn5', 'f2': 'w_pawn6', 'g2': 'w_pawn7', 'h2': 'w_pawn8', 
    'a1': 'w_rook1', 'b1': 'w_knight1', 'c1': 'w_bishop1', 'd1': 'w_queen', 
    'e1': 'w_king', 'f1': 'w_bishop2', 'g1': 'w_knight2', 'h1': 'w_rook2', 
}

eliminated = [
]


def board_boundary_check(location):
    for char in location:
        if location[0] not in LAT_LIMIT:
            print('Invalid entry. Enter a location between a1 and h8.')
            game()
        if location[1] not in LONG_LIMIT:
            print('Invalid entry. Enter a location between a1 and h8.')
            game()


def game():
    global turn, eliminated
    print(the_board)
    print()
    print('It is ' + turn + '\'s move.')
    print(turn + ', enter the location of the peice you would like to move.')
    origin_location = input().lower()  # Selecting location of desired peice.
    board_boundary_check(origin_location)
    peice_selection = the_board[origin_location]  # Converting location to peice value.
    print('You have chosen ' + peice_selection + '. Where would you like to '
    'move it?')
    move_location = input().lower()  # Getting move location.
    board_boundary_check(move_location)
    if the_board[move_location] != '':  # If not empty, peice is eliminated.
        eliminated = the_board[move_location]
    the_board[origin_location] = ''                       # Clearing 
    the_board[move_location] = peice_selection            # and asigning
    print(peice_selection + ' to ' + move_location + '.') # location
    print('Eliminated Peices : ', eliminated)
    if turn == 'White':  # Changing current turn.
        turn = 'Black'
    else: 
        turn = 'White'
    game()


game()



# TO-DO
# Test.
# System to eliminate peices on moves.
# System to show eliminated peices.
# Sort eliminated peices by color.
# System to check if moves are legal.