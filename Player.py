class Player:
    """
    Konstruktor der Klasse Player
    - initialisiert Instanzvariablen eines Players
    :param name: Name von Player
    :param player_number: Nummer von Player
    :param symbol: Symbol von Player für die Spielzüge
    """
    def __init__(self, name, player_number, symbol):
        self.name = name
        self.player_number = player_number
        self.symbol = symbol

    """
    Funktion setzt einen Spielzug
    :param board: Spielfeld, auf dem der Spielzug gesetzt wird
    :param row: Zeile des zu setzenden Spielzugs
    :param col: Spalte des zu setzenden Spielzugs
    """
    def make_move(self, board, row, col):
        board.fields[row][col] = self.player_number

    """
    Funktion fordert Namenseingabe von Player über die Konsole
    und setzt diesen als Namen des Players
    """
    def set_player_name(self):
        new_name = input("Type in your name: ")
        self.name = new_name