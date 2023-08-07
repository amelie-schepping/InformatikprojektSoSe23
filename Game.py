from Player import Player
from Board import Board
from MyBot import MyBot

import random


class Game:

    def __init__(self, m, n, k):
        """
        Constructor for Game.

        :param m: Number of rows in the game board
        :param n: Number of columns in the game board
        :param k: Winning condition
        """

        self.m = m
        self.n = n
        self.k = k

        # Initialize the game components
        self.board = Board(m, n, k)
        self.player1 = Player("Player1", 1)
        self.player2 = Player("Player2", 2)

        # Player currently taking their turn - initially set to Player 1
        self.current_player = self.player1

    def change_current_player(self):
        """
        Function switches the current player.
        """

        if self.player1 == self.current_player:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def collect_data(self, gamemode1, gamemode2, starting_player):
        """
        Function collects data from the game, including the game mode and starting conditions.

        :param gamemode1: Game mode for player 1.
        :param gamemode2: Game mode for player 2.
        :param starting_player: Specifies the starting player (1, 2, or random).
        :return: The winner of the game (1, 2, or 0 for draw).
        """

        # Initialize bots for players
        self.player1 = MyBot("MyBot 1", 1, gamemode1)
        self.player2 = MyBot("MyBot 2", 2, gamemode2)

        # Set the starting player
        if starting_player == 1:
            self.current_player = self.player1

        if starting_player == 2:
            self.current_player = self.player2

        # If the starting player is not 1 or 2, determine the starting player randomly
        if starting_player not in [1, 2]:
            starting_player_in_game = self.determine_starting_player()
            self.current_player = starting_player_in_game

        # Start the game loop
        while not self.board.is_game_won_by(self.current_player.player_number):
            # Set the current player's move
            self.set_move()

            # Check for a winner after each move
            if self.board.is_game_won_by(self.current_player.player_number):
                break

            # Check for a draw
            if self.board.is_board_full():
                break

            # Switch to the other player for the next move
            self.change_current_player()

        # Display the final state of the board
        self.board.display()

        # Determine the winner and display the result
        winner = self.board.has_won(self.current_player.player_number)
        print(winner, "has won!")

        # Reset the game board
        self.board = None
        return winner

    def determine_starting_player(self):
        """
        Function randomly determines the starting player.

        :return: The randomly chosen starting player.
        """

        starting_player = random.choice([self.player1, self.player2])
        return starting_player

    def game_loop(self):
        """
        Function manages the game loop.
        """

        # Start the game before the actual game loop
        self.start()

        # Choose the starting player randomly and display their name
        starting_player_in_game = self.determine_starting_player()
        print(f"The starting player is: {starting_player_in_game.name}\n")

        # Set the starting player as the current player
        self.current_player = starting_player_in_game

        # As long as no one has won:
        while not self.board.is_game_won_by(self.current_player.player_number):

            # Display the name of the current player
            print(f"{self.current_player.name}, it's your turn!")

            # Current player makes a move
            self.set_move()

            # Display the game board
            self.board.display()

            # Check if there is a winner
            if self.board.is_game_won_by(self.current_player.player_number):
                # The game has been won, exit the game loop with break
                break

            # Check if the game board is full
            if self.board.is_board_full():
                # The game board is full, exit the game loop with break
                break

            # The game hasn't been won yet
            # Switch to the other player and continue the while loop
            self.change_current_player()

        # Determine the winner of the game
        winner = self.board.has_won(self.current_player.player_number)

        # Display the winner's name or indicate a draw
        if winner == 1:
            print(f"Congratulations {self.player1.name}! You have won!")

        if winner == 2:
            print(f"Congratulations {self.player2.name}! You have won!")

        if winner == 0:
            print("This game ended in a draw. Try again!")

        # Reset the game board and end the game
        self.board = None
        input("\n ----------> Press Enter to end the game. <----------")

    def set_move(self):
        """
        Function sets the current player's move on the game board.
        """

        # Get the current move from the current player's make_move function
        current_move = self.current_player.make_move(self.board)

        # Extract the row and column from the current move
        row = current_move[0]
        col = current_move[1]

        # Set the current player's symbol on the specified row and column
        self.board.fields[row][col] = self.current_player.player_number

    def start(self):
        """
        Function starts the game by setting up players' names and displaying the game board.
        """

        # Welcome message at the start of the game
        print("Welcome to Break - a Game for Smart Minds", "\n")

        # Game mode selection:
        # The possible game modes are displayed on the console
        print("GAME MODE")
        print("-- 1: Player vs Player -- ")
        print("-- 2: Player vs. Bot --")
        print("-- 3: Bot vs. Bot --")

        # Input must be valid: Catch ValueError exception
        ans = None

        while True:
            try:
                # Prompt the player to enter a game mode choice
                ans = int(input("Enter the number of your choice: "))

                if ans not in [1, 2, 3]:
                    raise ValueError
                break

            except ValueError:
                print("Please enter a valid choice!")
                continue

        # Game mode 1 (Player vs. Player)
        if ans == 1:
            # Players input their names
            self.player1.set_player_name()
            self.player2.set_player_name()

        # Game mode 2 (Player vs. Bot)
        if ans == 2:
            # Solo player inputs their name
            self.player1.set_player_name()

            # Solo player chooses the strength of the bot opponent
            print("Choose the strength of your opponent:")
            print("for level 1 press -- 1")
            print("for level 2 press -- 2")

            gamemode = None

            while True:
                try:
                    gamemode = int(input("Enter your choice: "))

                    if gamemode not in [1, 2]:
                        raise ValueError
                    break

                except ValueError:
                    print("Please enter a valid choice!")
                    continue

            # Player 2 is initialized as a bot with the chosen strength
            self.player2 = MyBot("MyBot", 2, gamemode)

        # Game mode 3 (Bot vs. Bot)
        if ans == 3:
            # Choose the strengths of the bot opponents
            print("Choose the strength of the opponents: ")
            print("for level 1 press -- 1")
            print("for level 2 press -- 2")

            gamemode1 = None
            gamemode2 = None
            
            while True:
                try:
                    gamemode1 = int(input("Enter your choice for your first Bot: "))
                    gamemode2 = int(input("Enter your choice for your second Bot: "))

                    if gamemode1 not in [1, 2] or gamemode2 not in [1, 2]:
                        raise ValueError

                    break

                except ValueError:
                    print("Please enter a valid choice!")
                    continue

            # Both players are automatically set as (possibly strategic) bots
            self.player1 = MyBot("MyBot 1", 1, gamemode1)
            self.player2 = MyBot("MyBot 2", 2, gamemode2)

        # Announce the start of the game
        print("YOUR GAME STARTS....NOW!")

        # Display the game board
        self.board.display()
