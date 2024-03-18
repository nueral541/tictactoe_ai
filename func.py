def print_board(gamestate):
    symbols = [' ', 'X', 'O']
    board = [symbols[num] if num in [-1, 1] else symbols[0] for num in gamestate]
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print("_________")
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print("_________")
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print("_________")

def print_guide():
    print('1 | 2 | 3')
    print("_________")
    print("4 | 5 | 6")
    print("_________")
    print("7 | 8 | 9")

def play_turn(player, gamestate):
    global move
    move_made = False  # Flag to track if a valid move has been made
    while not move_made:
        print_board(gamestate)
        move = input(f"Play your turn, {player}. Type 'idk' to bring up the guide:")
        if move == 'idk':
            print_guide()
            print("Here's the guide...")
        else:
            try:
                move = int(move) - 1  # Convert move to int and adjust for 0-based indexing
                if 0 <= move <= 8 and gamestate[move] == 0:  # Check if move is within bounds and the cell is empty
                    gamestate[move] = 1 if player == 'X' else -1
                    move_made = True  # Valid move made, exit the loop
                else:
                    print("That's not a valid move")
            except ValueError:  # Catch ValueError if int conversion fails
                print("Please enter a number between 1 and 9, or type 'idk' for the guide.")

    return gamestate

def asess_turn(gamestate):
    # Check for 3 in a row horizontally, vertically, and diagonally
    # Horizontal
    for i in range(0, 9, 3):
        if gamestate[i] == gamestate[i+1] == gamestate[i+2] != 0:
            return gamestate[i]

    # Vertical
    for i in range(3):
        if gamestate[i] == gamestate[i+3] == gamestate[i+6] != 0:
            return gamestate[i]

    # Diagonals
    if gamestate[0] == gamestate[4] == gamestate[8] != 0:
        return gamestate[0]
    if gamestate[2] == gamestate[4] == gamestate[6] != 0:
        return gamestate[2]

    # No winner yet
    return 0
