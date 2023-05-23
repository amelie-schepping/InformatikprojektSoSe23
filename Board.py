import numpy as np


class Board:
    """
    Konstruktor der Klasse Board
    - initialisiert die Instanzvariablen des Spielfelds
    - erstellt ein leeres Spielfeld
    :param _m: Zeilenanzahl des Spielfelds
    :param _n: Spaltenanzahl des Spielfelds
    """

    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.fields = np.zeros((m, n), dtype=int)
        self.k = k;

    """
    Funktion stellt das Spielfeld in einem nummerierten Raster dar
    """

    def display(self):
        print()
        # Überschrift Spalten
        print("\t", end='')
        for row in range(self.m):
            print(row + 1, "\t", end='')

        print()

        for row in range(self.m):
            # Überschrift Zeilen
            print(row + 1, "\t", end='')
            for col in range(self.n):
                print(self.fields[row][col], "\t", end='')
            print()

        print()

    """
    Funktion, die zurückgibt, wer das Spiel gewonnen hat
    0 = unentschieden
    1 = Sieg Spieler 1
    2 = Sieg Spieler 2
    :return: gibt an, wer gewonnen hat (s.o.)
    """

    def has_won(self, player_number):

        self.is_game_won_by(player_number)

        if player_number == 1:
            return 1

        if player_number == 2:
            return 2

        # unentschieden, es muss überprüft werden, ob alle Felder belegt sind
        else:
            for row in range(self.m):
                for col in range(self.n):
                    if self.fields[row][col] != 0:
                        return 0

    """
    Funktion, die zurückgibt, ob das Spiel gewonnen wurde
    :return: wurde das Spiel gewonnen (ja/nein)
    """

    def is_game_won_by(self, player_number):

        # Überprüfung in Zeilen
        for row in range(self.m):
            # Zähler
            count = 0
            for col in range(self.n):
                if self.fields[row, col] == player_number:
                    # Zähler wird hochgezählt, wenn player_number auftaucht
                    count += 1
                    if count == self.k:
                        return True
                        count = 0
                else:
                    # Zähler zurücksetzen bei Unterbrechung
                    count = 0

        # Überprüfung in Spalten
        for col in range(self.n):
            count = 0
            for row in range(self.m):
                if self.fields[row, col] == player_number:
                    count += 1
                    if count == self.k:
                        return True
                else:
                    count = 0

        # Überprüfung in Diagonale
        # sicherstellen, dass Startposition mindestens k Elemente von den Rändern der Zeilen und Spalten entfernt ist
        for row in range(self.m - self.k + 1):
            for col in range(self.n - self.k + 1):
                # Zähler
                count = 0
                for diagonal in range(self.k):
                    if self.fields[row + diagonal, col + diagonal] == player_number:
                        count += 1
                        if count == self.k:
                            return True
                            count = 0
                    else:
                        count = 0

        # Überprüfung in umgekehrten Diagonalen
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

    """
    Funktion prüft, ob ein Spielzug gültig ist, d.h.
    - ob die eingegebene Position im Spielfeld liegt
    - ob die eingegebene Position bereits belegt ist
    :return: gültig (ja/nein)
    """

    def is_move_valid(self, row, col):
        row = row - 1
        col = col - 1

        # eingegebene Zeile muss im Spielfeld liegen
        condition_rows = 0 <= row < self.m

        # eingegebene Spalte muss im Spielfeld liegen
        condition_cols = 0 <= col < self.n

        # eingegebene Position darf noch nicht belegt sein
        condition_position = self.fields[row][col] == 0

        # Abfrage, ob Bedingungen true oder false sind
        if condition_rows and condition_cols and condition_position:
            return True

        # falls eine der Bedingungen nicht true ist,
        # ist der Spielzug ungültig
        else:
            return False
