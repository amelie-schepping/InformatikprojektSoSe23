import numpy as np
class Board:
    """
    Konstruktor der Klasse Board
    - initialisiert die Instanzvariablen des Spielfelds
    - erstellt ein leeres Spielfeld
    :param _m: Zeilenanzahl des Spielfelds
    :param _n: Spaltenanzahl des Spielfelds
    """
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.fields = np.zeros((m, n), dtype=int)

    """
    Funktion stellt das Spielfeld in einem nummerierten Raster dar
    """
    def display(self):
        print()
        # Überschrift Spalten
        print("\t", end='')
        for row in range(self.m):
            print(row+1, "\t", end='')

        print()

        for row in range(self.m):
            #Überschrift Zeilen
            print(row+1, "\t", end='')
            for col in range(self.n):
                print(self.fields[row][col], "\t",  end='')
            print()

        print()

    """
    Funktion, die zurückgibt, wer das Spiel gewonnen hat
    0 = unentschieden
    1 = Sieg Spieler 1
    2 = Sieg Spieler 2
    :return: gibt an, wer gewonnen hat (s.o.)
    """
    def has_won(self):
        if self.is_game_won_by(self, player1.player_number, k) == True:
            return 1
        else:
            if self.is_game_won_by(self, player2.player_number, k) == True:
                return 2
            else:
                # unentschieden, es muss überprüft werden, ob alle Felder belegt sind
                return 0

    """
    Funktion, die zurückgibt, ob das Spiel gewonnen wurde
    :return: wurde das Spiel gewonnen (ja/nein)
    """
    def is_game_won_by(self,  player_number, k):

        # Überprüfung in Zeilen & Spalten
        for row in range(self.m):
            for col in range(self.n):
                # Zähler
                count = 0
                if self.fields[row][col] == player_number:
                    # Zähler wird hochgezählt, wenn player_number auftaucht
                    count += 1
                    if count == k:
                        print(f"{player_number} hat das Spiel gewonnen!")
                else:
                    # Zähler zurücksetzen bei Unterbrechung
                    count = 0

        # Überprüfung in Diagonale
        # sicherstellen, dass Startposition mindestens k Elemente von den Rändern der Zeilen und Spalten entfernt ist
        for row in range(self.m - k + 1):
            for col in range(self.n - k + 1):
                # Zähler
                count = 0
                for diagonal in range(k):
                    if self.fields[row + diagonal, col + diagonal] == player_number:
                        count += 1
                        if count == k:
                            print(f"{player_number} hat das Spiel gewonnen!")
                    else:
                        count = 0

    """
    Funktion prüft, ob ein Spielzug gültig ist
    :return: gültig (ja/nein)
    """
    def is_move_valid(self, row, col):
        if row >= 0 and row < self.m and col >= 0 and col < self.n and self.fields[row][col] == 0:
            return True
        else:
            return False