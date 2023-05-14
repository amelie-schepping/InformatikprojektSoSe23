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
    Funktion, die zurückgibt, ob das Spiel gewonnen wurde
    0 = unentschieden
    1 = Sieg Spieler 1
    2 = Sieg Spieler 2
    :return: gibt an, wer gewonnen hat (s.o.)
    """
    # def has_won(self, k):
        # check in rows
        # for row in range(self.m):
        # check in cols
        # for col in range(self.n):
        # check in diagonal
        # muss k übergeben werden? dynamische Anpassung, falls gewinn methode geändert wird
