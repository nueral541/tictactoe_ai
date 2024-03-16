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