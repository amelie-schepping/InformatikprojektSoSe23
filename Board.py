import numpy as np


class Board:

    def __init__(self, m, n, k):
        """
        Constructor for Board

        :param m: Number of rows in the game board.
        :param n: Number of columns in the game board.
        :param k: Winning condition (number of hits in a row).
        """
        self.m = m
        self.n = n
        self.k = k

        # Initialize the game board with zeros using NumPy
        self.fields = np.zeros((m, n), dtype=int)

    def display(self):
        """
        Function displays the game board in a numbered grid format.

        It also creates a 'second' game board using symbols, overlaying it on top of the original board.
        The code continues to work with player_number, only the display is shown with symbols overlay.
        """

        print()

        # Print column header
        print("\t", end='')
        for row in range(self.n):
            print(row + 1, "\t", end='')

        print()

        for row in range(self.m):

            # Print row header
            print(row + 1, "\t", end='')

            for col in range(self.n):
                # Create a new array with corresponding strings
                # The new array 'overlays' the original array, but doesn't modify the original
                # -> 1 becomes "X", 2 becomes "O", 0 becomes "[ ]"

                fields_strings = np.where(self.fields == 1, "X", np.where(self.fields == 2, "O", "."))
                print(fields_strings[row][col], "\t", end='')

            print()

        print()

    def has_won(self, current_player_number):
        """
        Function that determines who has won the game.
        0 = draw
        1 = Player 1 wins
        2 = Player 2 wins

        :param current_player_number: Player number of the player who made the last move
        :return: Indicates the winner (as described above)
        """

        # The 'has_won' method is called when the game board is full or when there is a winner

        # Therefore, first check again if there is a winner
        if self.is_game_won_by(current_player_number):
            # The player who made the last move has won
            if current_player_number == 1:
                return 1

            if current_player_number == 2:
                return 2

        # There is no winner, thus the board is full and the game has ended in a draw
        else:
            return 0

    def is_board_full(self):
        """
        Function checks if the game board is full, meaning
        every cell in the game board is occupied by a number.

        :return: True if the board is full, False if not.
        """

        for row in range(self.m):
            for col in range(self.n):
                # Check if each position is unoccupied (equal to 0)
                if self.fields[row, col] == 0:
                    # If at least one cell is unoccupied the board is not full
                    return False

        # Since no cell is unoccupied (as checked above) the Board is full
        return True

    def is_game_won_by(self, player_number):
        """
        Function determines if a player has won the game.

        :param player_number: Number of the player being checked for a win.
        :return: True if the specified player has won the game, False otherwise.
        """

        # Check in rows
        for row in range(self.m):
            # Initialize a counter for consecutive numbers in a row
            count = 0
            for col in range(self.n):
                # Check if the number at the current position matches the player's number
                if self.fields[row, col] == player_number:
                    # Increment counter when player_number is found
                    count += 1
                    # Check if the required consecutive numbers (k) have been reached
                    if count == self.k:
                        return True
                else:
                    # Reset counter when interrupted
                    count = 0

        # Check in columns
        for col in range(self.n):
            count = 0
            for row in range(self.m):
                if self.fields[row, col] == player_number:
                    count += 1
                    if count == self.k:
                        return True
                else:
                    count = 0

        # Check in diagonals
        # Make sure starting position is at least k elements away from the edges of rows and columns
        for row in range(self.m - self.k + 1):
            for col in range(self.n - self.k + 1):
                count = 0
                for diagonal in range(self.k):
                    if self.fields[row + diagonal, col + diagonal] == player_number:
                        count += 1
                        if count == self.k:
                            return True
                    else:
                        count = 0

        # Check in reverse diagonals
        for row in range(self.m - self.k + 1):
            for col in range(self.n - 1, self.k - 2, -1):
                count = 0
                for diagonal in range(self.k):
                    if self.fields[row + diagonal, col - diagonal] == player_number:
                        count += 1
                        if count == self.k:
                            return True
                    else:
                        count = 0

        return False

    def is_move_valid(self, row, col):
        """
        Function checks if a move is valid, i.e.
        - if the entered position is within the game board
        - if the entered position is unoccupied

        :param row: Row of the entered position
        :param col: Column of the entered position
        :return: True if the move is valid, False otherwise.
        """

        # Check if the entered row is within the game board
        condition_rows = 0 <= row < self.m

        # Check if the entered column is within the game board
        condition_cols = 0 <= col < self.n

        # Check if the entered column is within the game board and if the conditions above are true or false
        if condition_rows and condition_cols and self.fields[row][col] == 0:
            return True

        # If any of the conditions is not true, the move is invalid
        else:
            return False
