"""
Tic Tac Toe Player
"""

import math

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
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)
    return X if count_X == count_O else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
      for j in range(3):
        if board[i][j] == EMPTY:
          possible_actions.append((i,j))
        return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    current_player = player(board)
    new_board = [row[:] for row in board]
    new_board[i][j] = current_player
    return new_board
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if any player has won
    if player(board) is not None:
      return True

    # Check if the board is full
    for row in board:
      if EMPTY in row:
         return False

    # If no winner and the board is full, the game is over
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
      return 1
    elif winner_player == O:
      return -1
    else:
      return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    if terminal(board):
      return utility(board), None
    
