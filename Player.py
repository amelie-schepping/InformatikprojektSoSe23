class Player:
    """
    Konstruktor initialisiert Instanzvariablen
    name: Name von Player
    player_number: Player 1 oder 2
    symbol: Symbol des Players für die Spielzüge
    """
    def __init__(self, _name, _player_number, _symbol):
        self.name = _name
        self.player_number = _player_number
        self.symbol = _symbol

    """
    Funktion für einen Spielzug eines Players
    - fordert eine Eingabe des/der Players über die Konsole ein
    - setzt die Konsoleneingabe als Spielzug auf dem Board 
    """
    def make_move(self, _board):
        print("It's your turn! Make your move NOW!")
        my_input_row = input()
        my_input_col = input()
        print("You entered: ", my_input_row, my_input_col)

        #indizierter Zugriff auf Numpy Array
        _board.fields[int(my_input_row)][int(my_input_col)] = self.player_number


        # Eingabe gegenchecken (Int?)
        # Indexieren wie bei Schiffeversenken --> später in Array-Indexierung umwandeln

