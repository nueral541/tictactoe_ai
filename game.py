from func import *

gamestate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
running = True
winner = None

print("Let's play tictactoe!")
print("To play, type in a number based on the scoring guide below!")
print_guide()
print("X goes first!")

while running:
    # Player X's turn
    gamestate = play_turn('X', gamestate)
    result = asess_turn(gamestate)
    if result != 0:
        winner = 'X' if result == 1 else 'O'
        break  # Exit the loop if there's a winner
    elif 0 not in gamestate:  # Check if the board is full
        break  # Exit the loop if it's a tie



print_board(gamestate)
if winner:
    print("Congratulations!")
    print(f"{winner} wins!")
else:
    print("It's a tie!")