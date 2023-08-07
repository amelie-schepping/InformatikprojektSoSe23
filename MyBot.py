from Player import Player
import numpy as np
import random


class MyBot(Player):
    """
    The MyBot class is a subclass of the Player class.
    """

    def __init__(self, name, player_number, game_mode):
        """
         Constructor for MyBot.

        :param name: Name of the Bot
        :param player_number: Number of the Player
        :param symbol: Symbol of the player
        """

        # Call the base class constructor
        super().__init__(name, player_number)

        # Set the game mode for the bot
        self.game_mode = game_mode

        # Indicates whether a move has been made in this turn
        self.move_made = False

    def make_move(self, board):
        """
        Determines the bot's move based on the game mode.

        :param board: The game board
        :return: A tuple representing the chosen move (row, col)
        """
        
        # Reset the move_made flag at the beginning of each turn
        self.move_made = False

        # Game Mode 1: Random Move
        if self.game_mode == 1:
            return self.make_random_move(board)

        # Game Mode 2: Strategic Moves
        if self.game_mode == 2:

            # Try to make a winning move
            if not self.move_made:
                winning_move = self.make_winning_move(board)
                if winning_move is not None:
                    return winning_move

            # Try to make a defensive move
            if not self.move_made:
                defense_move = self.make_defense_move(board)
                if defense_move is not None:
                    return defense_move

            # Try to make an offensive move
            if not self.move_made:
                offense_move = self.make_offense_move(board)
                if offense_move is not None:
                    return offense_move

            # Try to make a center move
            if not self.move_made:
                center_move = self.make_center_move(board)
                return center_move

            # If no strategic move was possible, make a random move
            if not self.move_made:
                random_move = self.make_random_move(board)
                return random_move

    def make_center_move(self, board):
        """
        Attempts to make a move towards the center of the board.

        :param board: The game board
        :return: A tuple representing the chosen move (row, col)
        """

        # Calculate the coordinates of the center of the board
        row_mid = board.m // 2
        col_mid = board.n // 2

        starting_position = (row_mid, col_mid)

        # Try to make a move in the exact center
        if board.is_move_valid(starting_position[0], starting_position[1]):
            self.move_made = True
            print(f"in die mitte gesetzt {self.player_number}")
            return starting_position

        # If the center is not available, attempt to make a move near the center
        else:
            mid_positions = [(row_mid, col_mid + 1), (row_mid + 1, col_mid + 1), (row_mid + 1, col_mid),
                             (row_mid + 1, col_mid - 1), (row_mid, col_mid - 1), (row_mid - 1, col_mid - 1),
                             (row_mid - 1, col_mid), (row_mid - 1, col_mid + 1)]

            while True:
                # Choose a random position from the list of mid_positions
                starting_position = random.choice(mid_positions)
                if board.is_move_valid(starting_position[0], starting_position[1]):
                    self.move_made = True
                    return starting_position

    def make_defense_move(self, board):
        """
        Makes a defensive move based on current game board and player's number.

        :param board: The game board
        :return: A tuple representing the row and column of the defensive move.
        """

        # Check rows for possible winning moves for the opponent
        for row in range(board.m):
            count = 0
            for col in range(board.n):
                if board.fields[row][col] != self.player_number and board.fields[row][col] != 0:
                    count += 1

                if count == (board.k - 1):
                    # If a winning move is detected, block it by placing a move on the adjacent spot
                    if board.is_move_valid(row, col + 1):
                        self.move_made = True
                        print(f"defense row rechts {self.player_number}")
                        return row, col + 1
                    else:
                        if board.is_move_valid(row, col - (board.k - 1)):
                            self.move_made = True
                            print(f"defense row links {self.player_number}")
                            return row, col - (board.k - 1)

        # Check columns
        for col in range(board.n):
            count = 0
            for row in range(board.m):
                if board.fields[row][col] != self.player_number and board.fields[row][col] != 0:
                    count += 1

                if count == (board.k - 1):
                    # If a winning move is detected, block it by placing a move on the adjacent spot
                    if board.is_move_valid(row + 1, col):
                        self.move_made = True
                        print(f"defense col unten {self.player_number}")
                        return row + 1, col
                    else:
                        if board.is_move_valid(row - (board.k - 1), col):
                            self.move_made = True
                            print(f"defense col oben {self.player_number}")
                            return row - (board.k - 1), col

        # Check diagonals
        for row in range(board.m - board.k + 1):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row + diagonal][col + diagonal] != self.player_number and \
                            board.fields[row + diagonal][col + diagonal] != 0:
                        count += 1

                    if count == (board.k - 1):
                        if board.is_move_valid(row + (board.k - 1), col + (board.k - 1)):
                            self.move_made = True
                            print(f"defense diagonale rechts unten {self.player_number}")
                            return row + (board.k - 1), col + (board.k - 1)
                        else:
                            if board.is_move_valid(row - 1, col - 1):
                                self.move_made = True
                                print(f"defense diagonale links oben {self.player_number}")
                                return row - 1, col - 1

        # Check reversed diagonals
        for row in range(board.k - 1, board.m):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row - diagonal][col + diagonal] != self.player_number and \
                            board.fields[row - diagonal][col + diagonal] != 0:
                        count += 1

                    if count == (board.k - 1):
                        if board.is_move_valid(row - (board.k - 1), col + (board.k - 1)):
                            self.move_made = True
                            print(f"defense diagonale rechts oben {self.player_number}")
                            return row - (board.k - 1), col + (board.k - 1)
                        else:
                            if board.is_move_valid(row + 1, col - 1):
                                self.move_made = True
                                print(f"defense diagonale links unten {self.player_number}")
                                return row + 1, col - 1

    def make_offense_move(self, board):
        """
        Makes an offensive move based on current game board and player's number.

        :param board: The game board object.
        :return: A tuple representing the row and column of the offensive move.
        """

        # Check rows for potential offensive moves
        for row in range(board.m):
            count = 0
            for col in range(board.n):
                if board.fields[row][col] == self.player_number:
                    count += 1

                if count == (board.k - 2):
                    # If k-2 player's symbols are found in a row, place a move to complete the winning sequence
                    if board.is_move_valid(row, (col + 1)):
                        self.move_made = True
                        print(f"offense row rechts {self.player_number}")
                        return row, (col + 1)
                    else:
                        if board.is_move_valid(row, (col - (board.k - 2))):
                            self.move_made = True
                            print(f"offense row links {self.player_number}")
                            return row, (col - (board.k - 2))

        # Check columns for potential offensive moves
        for col in range(board.n):
            count = 0
            for row in range(board.m):
                if board.fields[row][col] == self.player_number:
                    count += 1

                if count == (board.k - 2):
                    if board.is_move_valid((row + 1), col):
                        self.move_made = True
                        print(f"offense col unten {self.player_number}")
                        return (row + 1), col
                    else:
                        if board.is_move_valid((row - (board.k - 2)), col):
                            self.move_made = True
                            print(f"offense col oben {self.player_number}")
                            return (row - (board.k - 2)), col

        # Check diagonals
        for row in range(board.m - board.k + 1):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row + diagonal][col + diagonal] == self.player_number:
                        count += 1

                    if count == (board.k - 2):
                        if board.is_move_valid((row - (board.k - 2)), (col + (board.k - 2))):
                            self.move_made = True
                            print(f"offense diagonale rechts unten {self.player_number}")
                            return (row - (board.k - 2)), (col + (board.k - 2))
                        else:
                            if board.is_move_valid((row - 1), (col - 1)):
                                self.move_made = True
                                print(f"offense diagonale links oben {self.player_number}")
                                return row - 1, col - 1

        # Check reversed diagonals
        for row in range(board.k - 1, board.m):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row - diagonal][col + diagonal] == self.player_number:
                        count += 1

                    if count == (board.k - 2):
                        if board.is_move_valid((row - (board.k - 2)), (col + (board.k - 2))):
                            self.move_made = True
                            print(f"offense diagonale rechts oben {self.player_number}")
                            return (row - (board.k - 2)), (col + (board.k - 2))
                        else:
                            if board.is_move_valid(row, col):
                                self.move_made = True
                                print(f"offense diagonale links unten {self.player_number}")
                                return row, col

    def make_random_move(self, board):
        """
        Makes a random move for the Bot.

        :param board: The game board.
        :return: A tuple representing the row and column of the random move.
        """

        # Keep generating random positions until a valid one is found
        while True:
            # Generate random row and column indices using numpy's randint
            row = np.random.randint(board.m)
            col = np.random.randint(board.n)

            # Check if the randomly chosen position is empty
            if board.fields[row][col] == 0:
                # Mark the move as made
                self.move_made = True
                print(f"random move {self.player_number}")

                # Return the chosen move
                return row, col

    def make_winning_move(self, board):
        """
        Makes a winning move if possible.

        :param board: The game board.
        :return: A tuple representing the row and column of the winning move.
        """

        # Check rows for potential winning move
        for row in range(board.m):
            count = 0
            for col in range(board.n):
                if board.fields[row][col] == self.player_number:
                    count += 1

                if count == (board.k - 1):
                    # If k-1 player's symbols are found in a row, place a move to complete the winning sequence
                    if board.is_move_valid(row, (col + 1)):
                        self.move_made = True
                        print(f"winning row rechts {self.player_number}")
                        return row, (col + 1)
                    else:
                        if board.is_move_valid(row, (col - (board.k - 1))):
                            self.move_made = True
                            print(f"winning row links {self.player_number}")
                            return row, (col - (board.k - 1))

        # Check columns
        for col in range(board.n):
            count = 0
            for row in range(board.m):
                if board.fields[row][col] == self.player_number:
                    count += 1

                if count == (board.k - 1):
                    if board.is_move_valid((row + 1), col):
                        self.move_made = True
                        print(f"winning col unten {self.player_number}")
                        return (row + 1), col
                    else:
                        if board.is_move_valid((row - (board.k - 1)), col):
                            self.move_made = True
                            print(f"winning col oben {self.player_number}")
                            return (row - (board.k - 1)), col

        # Check diagonals
        for row in range(board.m - board.k + 1):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row + diagonal][col + diagonal] == self.player_number:
                        count += 1

                    if count == (board.k - 1):
                        if board.is_move_valid(row - (board.k - 1), col + (board.k - 1)):
                            self.move_made = True
                            print(f"winning diagonale rechts unten {self.player_number}")
                            return row - (board.k - 1), col + (board.k - 1)
                        else:
                            if board.is_move_valid(row - 1, col - 1):
                                self.move_made = True
                                print(f"winning diagonale links oben {self.player_number}")
                                return row - 1, col - 1

        # Check reversed diagonals
        for row in range(board.k - 1, board.m):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row - diagonal][col + diagonal] == self.player_number:
                        count += 1

                    if count == (board.k - 1):
                        if board.is_move_valid((row - (board.k - 1)), (col + (board.k - 1))):
                            self.move_made = True
                            print(f"winning diagonale rechts oben {self.player_number}")
                            return (row - (board.k - 1)), (col + (board.k - 1))
                        else:
                            if board.is_move_valid((row + 1), (col - 1)):
                                self.move_made = True
                                print(f"winning diagonale links unten {self.player_number}")
                                return (row + 1), (col - 1)
