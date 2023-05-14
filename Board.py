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
        if is_game_won_by(self, player1.player_number, k) == True:
            return 1
        else:
            if is_game_won_by(self, player2.player_number, k) == True:
                return 2
            else:
                return 0

    """
    Funktion, die zurückgibt, ob das Spiel gewonnen wurde
    :return: wurde das Spiel gewonnen (ja/nein)
    """
    def is_game_won_by(self,  player_number, k):
        return False
        # check in rows
        # for row in range(self.m):
        # check in cols
        # for col in range(self.n):
        # check in diagonal
        # muss k übergeben werden? dynamische Anpassung, falls gewinn methode geändert wird

    """
    Funktion prüft, ob ein Spielzug gültig ist
    :return: gültig (ja/nein)
    """
    def is_move_valid(self, row, col):
        if row >= 0 and row < self.m and col >= 0 and col < self.n and self.fields[row][col] == 0:
            return True
        else:
            return False