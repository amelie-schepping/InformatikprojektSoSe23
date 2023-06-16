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

        # versuche zunächst in die Mitte zu setzen
        if board.fields[rowMid][colMid] == 0:
            board.fields[rowMid][colMid] = self.player_number

        # ansonsten "zufällige Position", wobei "smarte" Positionen größer gewichtet werden
        else:
            while True:
                # Fallunterscheidung: hat der Bot in der Mitte gesetzt?
                # von der Mitte aus eine gerade Linie setzen
                smart_positions = []

                # smart_positions für horizontale Linien
                for col in range(colMid - (board.k - 1), colMid + board.k):
                    if col >= 0 and col < board.n:  # Überprüfung der Gültigkeit des Spaltenindex
                        smart_positions.append((rowMid, col))

                # smart_positions für vertikale Linien
                for row in range(rowMid - (board.k - 1), rowMid + board.k):
                    if row >= 0 and row < board.m:  # Überprüfung der Gültigkeit des Zeilenindex
                        smart_positions.append((row, colMid))

                merged_list = positions + (smart_positions * 100)

                random_position = random.choice(merged_list)

                row = random_position[0]
                col = random_position[1]

                # setze den Zug
                if board.fields[row][col] == 0:
                    board.fields[row][col] = self.player_number
                    return

        # Fallunterscheidung, wenn es keine eindeutige Mitte gibt?

        # Überlegung 1: SmartBot soll erkennen, wenn der Gegner kurz davor ist zu gewinnen und dann den Zug verhindern (Verteidigung)
        # Überlegung 2: SmartBot sollte selbst versuchen in einer geraden Linie zu setzen (Angriff)
        # mit Schleife arbeiten? was wenn, Feld belegt ist?

        # random_seat setzen --> macht immer dieselben Zufallszüge --> um Zufall zu bergenzen
        # Bot vs. Bot random, wer anfängt

        # statistiken: Schleife mit bot 100 mal laufen lassen und ergebnisse rausschreiben --> damit evtl in excel weiterarbeiten
