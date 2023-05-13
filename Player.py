class Player:
    """
    Konstruktor initialisiert Instanzvariablen
    name: Name von Player
    player_number: Player 1 oder 2
    symbol: Symbol des Players für die Spielzüge
    """
    def __init__(self, name, player_number, symbol):
        self.name = name
        self.player_number = player_number
        self.symbol = symbol

    """
    Funktion für einen Spielzug eines Players
    - fordert eine Eingabe des/der Players über die Konsole ein
    - setzt die Konsoleneingabe als Spielzug auf dem Board 
    """
    def make_move(self, board, row, col):
        # checken, ob das Feld bereits belegt ist
        if board.fields[row][col] == 0:
            if row >= 0 and col >= 0:
                board.fields[row][col] = self.player_number
            else:
                print("Please enter a valid number!")

        else:
            print("This field is already taken!")

        # input erst im gameloop abfragen
        # Indexieren wie bei Schiffeversenken --> später in Array-Indexierung umwandeln


