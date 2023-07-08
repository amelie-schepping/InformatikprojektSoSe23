from Game import Game

gamemode1 = 2
gamemode2 = 2
number_of_rounds = 100

# initialize winner_count / draw_count
winner_count_player1 = 0
winner_count_player2 = 0
draw_count = 0

for rounds in range(number_of_rounds):

    newGame = Game(5, 5, 4)
    winner = newGame.collect_data(gamemode1, gamemode2)

    # Gewinner:in auf die Konsole ausgeben
    if winner == 1:
        winner_count_player1 += 1

    if winner == 2:
        winner_count_player2 += 1

    if winner == 0:
        draw_count += 1

print("MyBot 1, in gamemode ", gamemode1, " won: ", winner_count_player1, "times. ")
print("MyBot 2, in gamemode ", gamemode2, " won: ", winner_count_player2, "times. ")

print("The game ended in a draw: ", draw_count, "times.")
