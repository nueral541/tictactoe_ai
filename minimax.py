import math
from func import winner, count_X, count_O, make_move

def find_winning_combos(gamestate):
    count_X = count_O = 0

    # Define winning combinations (indices of squares)
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]

    for combo in winning_combinations:
        symbol_count = {'X': 0, 'O': 0, 'empty': 0}
        for index in combo:
            if gamestate[index] == 1:
                symbol_count['X'] += 1
            elif gamestate[index] == -1:
                symbol_count['O'] += 1
            else:
                symbol_count['empty'] += 1

        if symbol_count['X'] == 2 and symbol_count['empty'] == 1:
            count_X += 1
        elif symbol_count['O'] == 2 and symbol_count['empty'] == 1:
            count_O += 1

    return count_X, count_O

def evaluate(gamestate):
    count_X, count_O = find_winning_combos(gamestate)
    if winner == 'O':
        return 100
    elif winner == 'X':
        return -100
    else:
        return (count_X - count_O) * 10

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
    legal_moves = possible_moves(gamestate)
    if not legal_moves:
        return best_move  # No legal moves available
    for move in legal_moves:
        new_gamestate = make_move(gamestate, move, 1)  # Player 1 (X) makes the move
        eval = minimax(new_gamestate, depth - 1, alpha, beta, False)
        if eval > max_eval:
            max_eval = eval
            best_move = move
            alpha = max(alpha, eval)
    return best_move

def possible_moves(gamestate):
    legal_moves = []
    for i in range(len(gamestate)):
        if gamestate[i] == 0:
            legal_moves.append(i + 1)
    return legal_moves