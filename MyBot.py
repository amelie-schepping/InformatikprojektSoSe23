from Player import Player
import numpy as np

"""
Die Klasse MyBot ist eine Subklasse von der Klasse Player
"""


class MyBot(Player):
    """
    Konstruktor der Klasse Player
    - initialisiert folgende Instanzvariablen
    name: Name von Player
    player_number: Player 1 oder 2
    symbol: Symbol des Players für die Spielzüge
    """

    def __init__(self, player_number, symbol):
        self.name = "MyBot"
        self.player_number = player_number
        self.symbol = symbol

    """
    Funktion für den Spielzug des Bots
    """

    def make_move(self, board):

        # generiert so lange Zufallszahlen, bis eine gültige gefunden wurde
        while True:
            # random.randint erzeugt Zufallszahlen von 0 bis (exklusive) board.m (Zeilen)
            row = np.random.randint(board.m)
            col = np.random.randint(board.n)

            if board.fields[row][col] != 0:
                board.fields[row][col] = self.player_number
                break
