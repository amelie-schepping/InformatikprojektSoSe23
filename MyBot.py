from Player import Player
import numpy as np

"""
Die Klasse MyBot ist eine Subklasse von der Klasse Player
"""


class MyBot(Player):
    """
    Konstruktor der Klasse MyBot
    - initialisiert folgende Instanzvariablen
    name: Name vom Bot
    player_number: Bot ist Player 1 oder 2
    symbol: Symbol des Bots für die Spielzüge
    """

    def __init__(self, name, player_number, symbol):
        self.name = name
        self.player_number = player_number
        self.symbol = symbol

    """
    Funktion für den Zufallsspielzug des Bots
    """

    def make_move(self, board):

        # generiert so lange Zufallszahlen, bis eine gültige gefunden wurde
        while True:
            # random.randint erzeugt Zufallszahlen von 0 bis (exklusive) board.m (Zeilen)
            row = np.random.randint(board.m)
            # random.randint erzeugt Zufallszahlen von 0 bis (exklusive) board.n (Spalten)
            col = np.random.randint(board.n)

            # prüft, ob Zufallsposition noch nicht belegt ist
            if board.fields[row][col] == 0:
                # setzt Zufallsposition auf freies Feld
                board.fields[row][col] = self.player_number
                # beendet Schleife, da Bot seinen Zug nun gesetzt hat
                break
