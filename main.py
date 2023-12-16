import collections
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    if not any(EMPTY in row for row in board):
        return
    O_count = 0
    X_count = 0
    for i in range(len(board)):
        for f in range(len(board)):
            if board[i][f] == 'O':
                O_count += 1
            elif board[i][f] == 'X':
                X_count += 1
    if O_count == X_count:
        return X
    elif O_count < X_count:
        return O
    else:
        return X

def actions(board):
    final = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == EMPTY:
                final.append((r, c))
    return final

def result(board, action):
    try:
        test_board = copy.deepcopy(board)
        for i in range(len(test_board)):
            for f in range(len(test_board)):
                if (i, f) == action:
                    test_board[i][f] = player(board)
        return test_board
    except:
        raise Exception

def winner(board):
    if ('X' == board[0][0] and 'X' == board[0][1] and 'X' == board[0][2]) or \
       ('X' == board[1][0] and 'X' == board[1][1] and 'X' == board[1][2]) or \
       ('X' == board[2][0] and 'X' == board[2][1] and 'X' == board[2][2]) or \
       ('X' == board[0][0] and 'X' == board[1][0] and 'X' == board[2][0]) or \
       ('X' == board[0][0] and 'X' == board[1][1] and 'X' == board[2][2]) or \
       ('X' == board[0][1] and 'X' == board[1][1] and 'X' == board[2][1]) or \
       ('X' == board[0][2] and 'X' == board[1][1] and 'X' == board[2][0]) or \
       ('X' == board[2][0] and 'X' == board[1][1] and 'X' == board[0][2]) or \
       ('X' == board[2][2] and 'X' == board[1][1] and 'X' == board[0][0]) or \
       ('X' == board[0][2] and 'X' == board[1][2] and 'X' == board[2][2]) or \
       ('X' == board[2][2] and 'X' == board[1][2] and 'X' == board[0][2]) or \
       ('X' == board[2][1] and 'X' == board[1][1] and 'X' == board[0][1]) or \
       ('X' == board[0][1] and 'X' == board[1][1] and 'X' == board[2][1]) or \
       ('X' == board[2][0] and 'X' == board[1][0] and 'X' == board[0][0]) or \
       ('X' == board[0][0] and 'X' == board[1][0] and 'X' == board[2][0]) or \
       ('X' == board[0][2] and 'X' == board[0][1] and 'X' == board[0][0]) or \
       ('X' == board[1][2] and 'X' == board[1][1] and 'X' == board[1][0]) or \
       ('X' == board[2][2] and 'X' == board[2][1] and 'X' == board[2][0]):
        return 'X'
    elif ('O' == board[0][0] and 'O' == board[0][1] and 'O' == board[0][2]) or \
         ('O' == board[1][0] and 'O' == board[1][1] and 'O' == board[1][2]) or \
         ('O' == board[2][0] and 'O' == board[2][1] and 'O' == board[2][2]) or \
         ('O' == board[0][0] and 'O' == board[1][0] and 'O' == board[2][0]) or \
         ('O' == board[0][0] and 'O' == board[1][1] and 'O' == board[2][2]) or \
         ('O' == board[0][1] and 'O' == board[1][1] and 'O' == board[2][1]) or \
         ('O' == board[0][2] and 'O' == board[1][1] and 'O' == board[2][0]) or \
         ('O' == board[2][0] and 'O' == board[1][1] and 'O' == board[0][2]) or \
         ('O' == board[2][2] and 'O' == board[1][1] and 'O' == board[0][0]) or \
         ('O' == board[0][2] and 'O' == board[1][2] and 'O' == board[2][2]) or \
         ('O' == board[2][2] and 'O' == board[1][2] and 'O' == board[0][2]) or \
         ('O' == board[2][1] and 'O' == board[1][1] and 'O' == board[0][1]) or \
         ('O' == board[0][1] and 'O' == board[1][1] and 'O' == board[2][1]) or \
         ('O' == board[2][0] and 'O' == board[1][0] and 'O' == board[0][0]) or \
         ('O' == board[0][0] and 'O' == board[1][0] and 'O' == board[2][0]) or \
         ('O' == board[0][2] and 'O' == board[0][1] and 'O' == board[0][0]) or \
         ('O' == board[1][2] and 'O' == board[1][1] and 'O' == board[1][0]) or \
         ('O' == board[2][2] and 'O' == board[2][1] and 'O' == board[2][0]):
        return 'O'
    else:
        return None

def terminal(board):
    if not any(EMPTY in row for row in board) or winner(board):
        return True
    else:
        return False

def utility(board):
    utility = 0
    if winner(board) == 'X':
        utility = 1
    elif winner(board) == 'O':
        utility = -1
    else:
        utility = 0
    return utility

def minimax(board):
    def max_func(board):
        if terminal(board):
            return utility(board)
        v = -50000
        for action in actions(board):
            v = max(v, min_func(result(board, action)))
        return v

    def min_func(board):
        if terminal(board):
            return utility(board)
        v = 500000
        for action in actions(board):
            v = min(v, max_func(result(board, action)))
        return v

    turn = player(board)
    i = None
    if turn == 'X':
        for action in actions(board):
            if int(min_func(result(board, action))) == int(1):
                return action
            elif int(min_func(result(board, action))) == int(0):
                i = action
        if i != None:
            return i
    else:
        for action in actions(board):
            if int(max_func(result(board, action))) == int(-1):
                return action
            elif int(max_func(result(board, action))) == int(0):
                i = action
        if i != None:
            return i
    try:
        return actions(board)[0]
    except:
        return Exception
