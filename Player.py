class Player:

    def __init__(self, name, player_number):
        """
        Konstruktor der Klasse Player
        - initialisiert Instanzvariablen eines Players
        :param name: Name von Player
        :param player_number: Nummer von Player
        :param symbol: Symbol von Player für die Spielzüge
        """
        self.name = name
        self.player_number = player_number

    def make_move(self, board):
        """
        Funktion setzt einen Spielzug
        :param board: Spielfeld, auf dem der Spielzug gesetzt wird
        :param row: Zeile des zu setzenden Spielzugs
        :param col: Spalte des zu setzenden Spielzugs
        """
        # while-Schleife
        while True:
            # Error-Handling mit try-except
            try:
                # Eingabe fordern
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))

                # prüfen, ob Eingabe gültig ist
                if board.is_move_valid(row, col):
                    # Eingabe ist gültig
                    # prüfen, dass Eingabe != Enter/nicht leer ist
                    if row and col != "":
                        # Eingabe in indexierte Array-Struktur umwandeln
                        row = row - 1
                        col = col - 1

                        move = (row, col)
                        # die nun gültige Eingabe wird als Spielzug zurückgegeben
                        return move

                # Eingabe ist nicht gültig, Schleife beginnt von vorne
                else:
                    print("Please enter a valid position!")

            # es gibt einen Fehler (ValueError), weil ein falscher Wert eingegeben wurde
            except ValueError:
                # Spieler:in wird aufgefordert, eine gültige Position einzugeben
                print("Please enter a valid position!")
                # Schleife beginnt von vorne
                continue

        # board.fields[row][col] = self.player_number

    def set_player_name(self):
        """
        Funktion fordert Namenseingabe von Player über die Konsole
        und setzt diesen als Namen des Players
        """
        new_name = input("Type in your name: ")
        # prüfen, ob Name gültig ist (mind eine Zahl oder ein Buchstabe oder ein Zeichen)
        self.name = new_name
