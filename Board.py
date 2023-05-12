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
        self.fields = np.zeros((m, n))

    """
    Funktion, um das Spielfeld darzustellen
    """
        # def display():
    """
    Funktion, die zurückgibt, ob das Spiel gewonnen wurde
    0 = unentschieden
    1 = Sieg Spieler 1
    2 = Sieg Spieler 2
    :return: gibt an, wer gewonnen hat (s.o.)
    """
        # def has_won():