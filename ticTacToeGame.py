import random


def display_board(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def choose_first():
    if random.randint(1, 2) == 1:
        print('Player1 shall start the game')
        return 'Player1'
    else:
        print('Player2 shall start the game')
        return 'Player2'


def choose_marker(first_player):
    marker = ''
    player_1, player_2 = '', ''
    while marker != 'X' and marker != 'O':
        marker = input(first_player + ' choose the marker-X or O:')
        if first_player == 'Player1' and marker == 'X':
            player_1, player_2 = ('X', 'O')
        elif first_player == 'Player1' and marker == 'O':
            player_1, player_2 = ('O', 'X')
        elif first_player == 'Player2' and marker == 'X':
            player_1, player_2 = ('O', 'X')
        elif first_player == 'Player2' and marker == 'O':
            player_1, player_2 = ('X', 'O')
        else:
            continue
    print('Player1 marker is: {0} and Player2 marker is: {1}'.format(player_1, player_2))
    return player_1, player_2


def place_marker(board, position, marker):
    board[position] = marker


def win_check(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[3] == marker and board[5] == marker and board[7] == marker))


def board_not_full(board):
    return ' ' in board[1:]


def choose_marker_position(board):
    is_position_valid = True
    position = 0
    while is_position_valid:
        try:
            position = int(input('Choose the marker position- 1 to 9:'))
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")

        if position not in range(1, 10):
            print('Please choose the marker position from 1 to 9')
            continue
        elif board[position] != ' ':
            print('The position provided is already chosen. So, please select the available position to '
                  'place the marker')
            continue
        else:
            is_position_valid = False
    return position


def play_again():
    return input('Do you want to play again?- Yes or No:').lower().startswith('y')


print('Welcome to Tic Tac Toe game!')
while True:

    theBoard = [' '] * 10
    print('Here is your board')
    display_board(theBoard)
    turn = choose_first()
    player1_marker, player2_marker = choose_marker(turn)
    print(turn+', place the marker')
    game_on = True

    while game_on:

        if turn == 'Player1':
            marker_position = choose_marker_position(theBoard)
            place_marker(theBoard, marker_position, player1_marker)
            display_board(theBoard)
            if win_check(theBoard, player1_marker):
                print('Congratulations, Player1! you won the match.')
                game_on = False
            else:
                if board_not_full(theBoard):
                    print("Player2's turn to place the marker")
                    turn = 'Player2'
                else:
                    print('The game is a draw!')
                    game_on = False
        else:
            marker_position = choose_marker_position(theBoard)
            place_marker(theBoard, marker_position, player2_marker)
            display_board(theBoard)
            if win_check(theBoard, player2_marker):
                print('Congratulations, Player2! you won the match.')
                game_on = False
            else:
                if board_not_full(theBoard):
                    print("Player1's turn to place the marker")
                    turn = 'Player1'
                else:
                    print('The game is a draw!')
                    game_on = False

    if not play_again():
        break
