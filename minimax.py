import math
from func import winner, count_X, count_O

def find_winning_combos(gamestate):
    
    # Check for 3 in a row horizontally, vertically, and diagonally
    # Horizontal
    for i in range(0, 9, 3):
        if gamestate[i] == gamestate[i+1] != 0 and gamestate[i+2] == 0:
            if gamestate[i] == 1:
                count_X += 1
            else:
                count_O += 1
        elif gamestate[i] == gamestate[i+2] != 0 and gamestate[i+1] == 0:
            if gamestate[i] == 1:
                count_X += 1
            else:
                count_O += 1
        elif gamestate[i+1] == gamestate[i+2] != 0 and gamestate[i] == 0:
            if gamestate[i+1] == 1:
                count_X += 1
            else:
                count_O += 1

    # Vertical
    for i in range(3):
        if gamestate[i] == gamestate[i+3] != 0 and gamestate[i+6] == 0:
            if gamestate[i] == 1:
                count_X += 1
            else:
                count_O += 1
        elif gamestate[i] == gamestate[i+6] != 0 and gamestate[i+3] == 0:
            if gamestate[i] == 1:
                count_X += 1
            else:
                count_O += 1
        elif gamestate[i+3] == gamestate[i+6] != 0 and gamestate[i] == 0:
            if gamestate[i+3] == 1:
                count_X += 1
            else:
                count_O += 1

    # Diagonals
    if gamestate[0] == gamestate[4] != 0 and gamestate[8] == 0:
        if gamestate[0] == 1:
            count_X += 1
        else:
            count_O += 1
    elif gamestate[0] == gamestate[8] != 0 and gamestate[4] == 0:
        if gamestate[0] == 1:
            count_X += 1
        else:
            count_O += 1
    elif gamestate[4] == gamestate[8] != 0 and gamestate[0] == 0:
        if gamestate[4] == 1:
            count_X += 1
        else:
            count_O += 1

    if gamestate[2] == gamestate[4] != 0 and gamestate[6] == 0:
        if gamestate[2] == 1:
            count_X += 1
        else:
            count_O += 1
    elif gamestate[2] == gamestate[6] != 0 and gamestate[4] == 0:
        if gamestate[2] == 1:
            count_X += 1
        else:
            count_O += 1
    elif gamestate[4] == gamestate[6] != 0 and gamestate[2] == 0:
        if gamestate[4] == 1:
            count_X += 1
        else:
            count_O += 1

    return count_X, count_O

def evaluate(gamestate):
    if winner == 'O':
        eval = 100
    elif winner == 'X':
        eval = -100
    else:
        find_winning_combos(gamestate)

        eval = ((count_X - count_O) * 100)

def minimax(gamestate, depth, alpha, beta, maximizing_player):
    # Base case: if the maximum depth is reached
    if depth == 0:
        return evaluate(gamestate)
    
    # Check if the game is over
    if winner != None:
        return evaluate(gamestate)
    
    if maximizing_player:
        max_eval = -math.inf
        for move in possible_moves(gamestate):
            new_gamestate = make_move(gamestate, move, 1)  # Player 1 (X) makes the move
            eval = minimax(new_gamestate, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in possible_moves(gamestate):
            new_gamestate = make_move(gamestate, move, -1)  # Player -1 (O) makes the move
            eval = minimax(new_gamestate, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def find_best_move(gamestate, depth):
    best_move = None
    alpha = -math.inf
    beta = math.inf
    max_eval = -math.inf
    for move in possible_moves(gamestate):
        new_gamestate = make_move(gamestate, move, 1)  # Player 1 (X) makes the move
        eval = minimax(new_gamestate, depth - 1, alpha, beta, False)
        if eval > max_eval:
            max_eval = eval
            best_move = move
            alpha = max(alpha, eval)
    return best_move

def make_move(board, move, is_x):
    move -= 1
    board[move] = 1 if is_x else 0

def possible_moves(board):
    legal_moves = []
    for i in board:
        if board[i] == 0:
            legal_moves.append(i + 1)