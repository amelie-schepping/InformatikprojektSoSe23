from Player import Player
import numpy as np

"""
Die Klasse MySmartBot ist eine Subklasse von der Klasse Player
"""


class MySmartBot(Player):
    """
    Konstruktor der Klasse MySmartBot
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
    Funktion für den strategischen Spielzug des Bots
    """

    def make_move(self, board):
        # Mitte errechnen
        # m Zeile
        # n Spalten

        rowMid = board.m // 2
        colMid = board.n // 2

        # wenn Mitte frei ist, setze in die Mitte
        if board.fields[rowMid][colMid] == 0:
            board.fields[rowMid][colMid] = self.player_number

        # hier evtl. Fallunterscheidung, wenn es keine eindeutige Mitte gibt

        # wenn nicht random Zug
        else:
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
