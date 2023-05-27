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

    def make_move(self, board):
        # while-Schleife
        while True:
            # Error-Handling mit try-except
            try:
                # Eingabe fordern
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))

                # prüfen, ob Eingabe gültig ist
                if board.is_move_valid(row, col):
                    # Eingabe ist gültig:
                    # Eingabe in indexierte Array-Struktur umwandeln
                    row = row - 1
                    col = col - 1
                    # und Schleife mit break verlassen
                    break
                # Eingabe ist nicht gültig, Schleife beginnt von vorne
                else:
                    print("Please enter a valid position!")

            # es gibt einen Fehler (ValueError), weil ein falscher Wert eingegeben wurde
            except ValueError:
                # Spieler:in wird aufgefordert, eine gültige Position einzugeben
                print("Please enter a valid position!")
                # Schleife beginnt von vorne
                continue
        # die nun gültige Eingabe wird als Spielzug gesetzt
        board.fields[row][col] = self.player_number

    """
    Funktion fordert Namenseingabe von Player über die Konsole
    und setzt diesen als Namen des Players
    """

    def set_player_name(self):
        new_name = input("Type in your name: ")
        # prüfen, ob Name gültig ist (mind eine Zahl oder ein Buchstabe oder ein Zeichen)
        self.name = new_name
