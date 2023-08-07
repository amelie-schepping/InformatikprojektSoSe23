from Game import Game

# Define the game modes, starting player, and number of rounds
gamemode1 = 2
gamemode2 = 2
starting_player = 1
number_of_rounds = 10

# Initialize winner_count / draw_count
winner_count_player1 = 0
winner_count_player2 = 0
draw_count = 0

# Iterate through the specified number of rounds
for rounds in range(number_of_rounds):

    # Initialize a new game
    newGame = Game(5, 5, 4)

    # Collect game data and determine the winner
    winner = newGame.collect_data(gamemode1, gamemode2, starting_player)

    # Increment the winner-count / draw-count
    if winner == 1:
        winner_count_player1 += 1

    if winner == 2:
        winner_count_player2 += 1

    if winner == 0:
        draw_count += 1

# Print the results
print("MyBot 1, in gamemode ", gamemode1, " won: ", winner_count_player1, "times. ")
print("MyBot 2, in gamemode ", gamemode2, " won: ", winner_count_player2, "times. ")
print("The game ended in a draw: ", draw_count, "times.")
