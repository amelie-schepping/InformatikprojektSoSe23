class Player:

    def __init__(self, name, player_number):
        """
        Constructor for Player

        :param name: Name of the Player
        :param player_number: Number of the Player
        """

        self.name = name
        self.player_number = player_number

    def make_move(self, board):
        """
        Function to make a move on the game board.
        :param board:  Game board on which the move is made.
        :return: tuple (row: int, col: int)
        """

        # Use a while loop for continuous input until a valid move is obtained
        while True:
            try:
                # Prompt for user input
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))

                # Check if the input move is valid
                if board.is_move_valid(row - 1, col - 1):
                    # Ensure both row and column inputs are not empty
                    if row and col != "":
                        # Convert input to zero-based indexed array structure
                        row = row - 1
                        col = col - 1

                        move = (row, col)
                        # Return the valid move
                        return move

                # If the input move is not valid, prompt for a new input
                else:
                    print("Please enter a valid position!")

            # Handle error (ValueError) in case of invalid input
            except ValueError:
                # Prompt the player to enter a valid position
                print("Please enter a valid position!")
                continue

    def set_player_name(self):
        """
        Function prompts the Player to enter their name via the console
        and sets it as the Player's name.
        """
        
        while True:
            new_name = input(f"Player {self.player_number}, what's your name: ")

            # Check if the entered name is valid (should not be empty and must start with a letter)
            if new_name != "" and new_name[0].isalpha():
                self.name = new_name
                break
            else:
                print("Please enter your name (must start with a letter).")
