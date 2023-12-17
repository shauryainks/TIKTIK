"""
Tic Tac Toe Player
"""
import collections
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.

    """
    # we will check how many moves are already there, if x == o moves then we will let x go.
    if not any(EMPTY in row for row in board):
        return

    O_count = 0 
    X_count = 0

    for i in range (len(board)):
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

    # if EMPTY not in board:
    #     return

    # counts = collections.Counter(
    #     [element
    #      for row in board
    #      for element in row])

    # if counts['X'] == counts['O']:
    #     return X
    
    # elif counts['X'] > counts['O']:
    #     return O
    # else:
    #     return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    final = []
    # we will make two loops for checking every empty spot on the board
    for r in range(len(board)):
        for c in range(len(board)):

            if board[r][c] == EMPTY:

                final.append((r, c))
    return (final)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # we will deep copy the board so we don't mess the memory where orginal board variable is pointing at
    # we will change the chosen x,y coordinate, we will know whose turn it is by using the player function 
    try:
        test_board = copy.deepcopy(board)
        for i in range(len(test_board)):
            for f in range(len(test_board)):
                if (i,f) == action:
                    test_board[i][f] = player(board)
        return test_board
    except:
        raise Exception
    




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # all the possibilities of winning the game 
    if ('X' == board[0][0] and 'X' == board[0][1] and 'X' == board[0][2]):
        return 'X'
    elif ('X' == board[1][0] and 'X' == board[1][1] and 'X' == board[1][2]):
        return 'X'
    elif ('X' == board[2][0] and 'X' == board[2][1] and 'X' == board[2][2]):
        return 'X'
    elif ('X' == board[0][0] and 'X' == board[1][0] and 'X' == board[2][0]):
        return 'X'
    elif ('X' == board[0][0] and 'X' == board[1][1] and 'X' == board[2][2]):
        return 'X'
    elif ('X' == board[0][1] and 'X' == board[1][1] and 'X' == board[2][1]):
        return 'X'
    elif ('X' == board[0][2] and 'X' == board[1][1] and 'X' == board[2][0]):
        return 'X'
    elif ('X' == board[2][0] and 'X' == board[1][1] and 'X' == board[0][2]):
        return 'X'
    elif ('X' == board[2][2] and 'X' == board[1][1] and 'X' == board[0][0]):
        return 'X'
    elif ('X' == board[0][2] and 'X' == board[1][2] and 'X' == board[2][2]):
        return 'X'
    elif ('X' == board[2][2] and 'X' == board[1][2] and 'X' == board[0][2]):
        return 'X'
    elif ('X' == board[2][1] and 'X' == board[1][1] and 'X' == board[0][1]):
        return 'X'
    elif ('X' == board[0][1] and 'X' == board[1][1] and 'X' == board[2][1]):
        return 'X'
    elif ('X' == board[2][0] and 'X' == board[1][0] and 'X' == board[0][0]):
        return 'X'
    elif ('X' == board[0][0] and 'X' == board[1][0] and 'X' == board[2][0]):
        return 'X'
    elif ('X' == board[0][2] and 'X' == board[0][1] and 'X' == board[0][0]):
        return 'X'
    elif ('X' == board[1][2] and 'X' == board[1][1] and 'X' == board[1][0]):
        return 'X'
    elif ('X' == board[2][2] and 'X' == board[2][1] and 'X' == board[2][0]):
        return 'X'
    elif ('O' == board[0][0] and 'O' == board[0][1] and 'O' == board[0][2]):
        return 'O'
    elif ('O' == board[1][0] and 'O' == board[1][1] and 'O' == board[1][2]):
        return 'O' 
    elif ('O' == board[2][0] and 'O' == board[2][1] and 'O' == board[2][2]):
        return 'O' 
    elif ('O' == board[0][0] and 'O' == board[1][0] and 'O' == board[2][0]):
        return 'O' 
    elif ('O' == board[0][0] and 'O' == board[1][1] and 'O' == board[2][2]):
        return 'O' 
    elif ('O' == board[0][1] and 'O' == board[1][1] and 'O' == board[2][1]):
        return 'O' 
    elif ('O' == board[0][2] and 'O' == board[1][1] and 'O' == board[2][0]):
        return 'O' 
    elif ('O' == board[2][0] and 'O' == board[1][1] and 'O' == board[0][2]):
        return 'O' 
    elif ('O' == board[2][2] and 'O' == board[1][1] and 'O' == board[0][0]):
        return 'O' 
    elif ('O' == board[0][2] and 'O' == board[1][2] and 'O' == board[2][2]):
        return 'O' 
    elif ('O' == board[2][2] and 'O' == board[1][2] and 'O' == board[0][2]):
        return 'O' 
    elif ('O' == board[2][1] and 'O' == board[1][1] and 'O' == board[0][1]):
        return 'O' 
    elif ('O' == board[0][1] and 'O' == board[1][1] and 'O' == board[2][1]):
        return 'O' 
    elif ('O' == board[2][0] and 'O' == board[1][0] and 'O' == board[0][0]):
        return 'O' 
    elif ('O' == board[0][0] and 'O' == board[1][0] and 'O' == board[2][0]):
        return 'O'
    elif ('O' == board[0][2] and 'O' == board[0][1] and 'O' == board[0][0]):
        return 'O' 
    elif ('O' == board[1][2] and 'O' == board[1][1] and 'O' == board[1][0]):
        return 'O' 
    elif ('O' == board[2][2] and 'O' == board[2][1] and 'O' == board[2][0]):
        return 'O'
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # we will check if there is any empty spot left in the game or there is some winner already
    if not any(EMPTY in row for row in board):
        return True
    elif winner(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # will check the score, if x won then it will be 1, if nobody won then it will be 0 else it will be -1
    utility = 0
    if winner(board) == 'X':
        utility = 1
    elif winner(board) == 'O':
        utility = -1
    else:
        utility = 0
    return utility


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    """
    #max func
    def max_func(board):
        #game over or not
        if terminal(board):
            return utility(board)
        #worst possible value for v
        v = -50000
        # check all the possible actions
        for action in actions(board):
            # check the max score we can get
            v = max(v,min_func(result(board, action)))
        return v
    # mini func
    def min_func(board):
        #game over or not
        if terminal(board):
            return utility(board)
        #best possible value
        v = 500000
        #check all the possible actions
        for action in actions(board):
            # check the lowest score we can get
            v = min(v,max_func(result(board, action)))
        return v

#board = [
 # [EMPTY, X, O],
 # [O, X, EMPTY],
 # [X, EMPTY, O]]
 # max returned 1

    turn = player(board)
    i = None
    # yes because it is x
    if turn == 'X':
        #checking all the possible moves to find out which is the best
        for action in actions(board):
            # if the i,f action will make the utility score = to what max_fun  got as the highest value
            # we made a deep copy of the first move we have and we provided that to max function to see what is the score if it = to the original max function's score then it is the right mmove
            #("250")
            if int(min_func(result(board,action))) == int(1):
                #("252")
                return action
            elif int(min_func(result(board,action))) == int(0):
                #("255")
                i = action
        if i!=None:
            #("258")
            return i

    else:
        #("262")
        for action in actions(board):
            if int(max_func(result(board,action))) == int(-1):
                #("265")
                return action
            elif int(max_func(result(board,action))) == int(0):
                #("268")
                i = action
        if i!=None:
            #("271")
            return i
    #("273")
    try:
        return actions(board)[0]
    except:
        return Exception

    




    # #if both are same then we can make any move
    # if min_func(board) == max_func(board):
    #     action = actions(board)
    #     board = result(board, action[0])
        
    #     return board
    # #if both minifunc is smaller or equal to max func then we will go ahead with the highest score board
    # elif min_func(board) <= max_func(board):
    #     for i,f in actions(board):
    #         if utility(result(board,[i,f])) == max_func(board):
    #             return [i,f]
    # else:
    #     for i,f in actions(board):
    #         if utility(result(board,[i,f])) == min_func(board):
    #             return [i,f]




        

    

    


    # for i, f in test_actions:
    #     # we made anoter deepcopy, so, we are not going to mess up the original deepcopy
    #     test_board_1 = copy.deepcopy(test_board)
    #     # we did put the player's turn here, in the test_board to see if this is the winning case directly 
    #     test_board_1[i][f] = player(board)
    #     if utility(test_board_1) == 1 or terminal(test_board_1):
    #         the_move = [i, f]
    #         # 1
    #         # we returned the best move here, Now we will go to the else part if this is not the best move then
    #         return the_move
        





            # elif utility(test_board) != -1:
            #     # -1
            #     # do nothing and move ahead with the loop

            # elif (utility(test_board) == 0):
            #     # 0
            #     the_move = (i,f)
            #     return the_move

    # def maximizer(test_board):
    #     available_position = [][]
    #     for i in range(len(test_board)):
    #         for f in range(len(test_board[i])):
    #             if test_board[i][f] == EMPTY:
    #                 available_position.append[i,f]

    # # initialize an empty explored set
    # source_explored = set()

    #     best_moves = []
    #     score = 0
    #     for i, a in test_board:
    #         if test_board[i][a] == EMPTY:
    #             test_board[i][a] = 'O'
    #             if 'O' == winner(test_board):
    #                 best_moves += test_board[i][a]
    #                 score = 1

    # def minimizer(board):

