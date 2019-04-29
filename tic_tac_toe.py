from math import copysign, floor
from copy import deepcopy

def check_win(board, rows, cols):
    # do we have three in a row, of either kind?
    winner = sum([board[i[0]][i[1]] for i in zip(rows, cols)])

    if winner == -3:
        return -1
    elif winner == 3:
        return 1
    else:
        return 0

def who_wins(board):
    
    winners = [0] * 9
    # check both diagonals
    winners[0] = check_win(board, range(3), range(3))
    winners[1] = check_win(board, range(3), [2,1,0])

    # check columns 
    for i in range(3):
        winners[2 + i] = check_win(board, range(3), [i, i, i])

    # check rows 
    for i in range(3):
        winners[6 + i] = check_win(board, [i, i, i], range(3))
    
    # the sum trick only works because there will only be one winner and everything else will be zero
    winners = sum(winners)

    if winners == 0:
        return 0
    elif winners < 0:
        return -1
    elif winners > 0:
        return 1

# need to be careful about manipulate array by reference or by value?
def all_possible_boards(board, player):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                old = board[i][j]
                board[i][j] = player
                yield deepcopy(board)
                board[i][j] = old

def opponent(player):
    return -1 * player;

def argmax(l):
    return max((v, i) for i, v in enumerate(l))[1]

def argmin(l):
    return min((v, i) for i, v in enumerate(l))[1]


def make_best_move(board, player):
    boards = all_possible_boards(board, player)
    
    if player == 1:
        return max(boards, key = lambda b: score_move(b, player))
    elif player == -1:
        return min(boards, key = lambda b: score_move(b, player)) 
    
def score_move(board, player):
    # assumed that the opponent just made a move 
    winner = who_wins(board)
    
    if winner != 0 or board_is_full(board):
        return winner 
    else:
        # look down one level of the game tree 
        boards = all_possible_boards(board, opponent(player))
        scores = map(lambda b: score_move(b, opponent(player)), boards)
     
        if player == 1:
            return min(scores) 
        elif player == -1:
            return max(scores) 

def board_is_full(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return False

    return True

def check_if_game_over(board):
    winner = who_wins(board);
    if winner == 0:
        return False
    elif winner == 1:
       print 'I won'
       return True
    elif winner == -1:
        print 'You won'
        return True

def make_move(board, i, j, move):
   board[i][j] = move
   return board

def print_board(board):
    chars = {-1: 'o', 1: 'x', 0: '.'}
    for i in range(3):
        print '|'.join([chars[board[i][j]] for j in range(3)])
        

def play():
    board = [[1,0,0],[0,0,0], [0,0,0]]
    print_board(board)
    # computer gets first move 
    while True: 
        l = raw_input('Enter zero-index coordinates "row, column": ')
        parts = l.split(',')
        board = make_move(board, int(parts[0]), int(parts[1]), -1)
        print_board(board) 

        if check_if_game_over(board):
            break

        print( 'Response:')
        board = make_best_move(board, 1)
        print_board(board) 

        if check_if_game_over(board):
            break


if __name__ == '__main__':
    play() 
