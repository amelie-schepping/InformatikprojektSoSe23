from Player import Player
import numpy as np
import random

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

        # Erstelle eine Liste aller Positionen auf dem Spielfeld
        positions = []
        for row in range(board.m):
            for col in range(board.n):
                positions.append((row, col))

        # Berechne die Mitte des Spielfelds
        rowMid = board.m // 2
        colMid = board.n // 2

        # fügt die Mitte 15-mal der Liste aller Positionen hinzu, um die Wahrscheinlichkeit zu erhöhen, dass er in die Mitte setzt
        mid = (rowMid, colMid)
        positions.extend([mid] * 15)

        # Wähle zufällig eine Position aus der Liste aller Positionen
        random_position = random.choice(positions)

        row = random_position[0]
        col = random_position[1]

        # setze den Zug
        if board.fields[row][col] == 0:
            board.fields[row][col] = self.player_number

        # Fallunterscheidung, wenn es keine eindeutige Mitte gibt?

        # Überlegung 1: SmartBot soll erkennen, wenn der Gegner kurz davor ist zu gewinnen und dann den Zug verhindern (Verteidigung)
        # Überlegung 2: SmartBot sollte selbst versuchen in einer geraden Linie zu setzen (Angriff)
