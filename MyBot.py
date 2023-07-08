from Player import Player
import numpy as np
import random


class MyBot(Player):
    """
    Die Klasse MyBot ist eine Subklasse von der Klasse Player
    """

    def __init__(self, name, player_number, game_mode):
        """
        Konstruktor der Klasse MyBot
        - initialisiert folgende Instanzvariablen
        name: Name vom Bot
        player_number: Bot ist Player 1 oder 2
        symbol: Symbol des Bots für die Spielzüge
        """
        super().__init__(name, player_number)

        # neue Instanzvariable game_mode
        self.game_mode = game_mode

        # wurde bereits ein zug gemacht?
        self.move_made = False

    def make_move(self, board):
        """
        Spielzug abhängig vom GameMode
        """
        self.move_made = False

        # if game mode 1 --> Zufallszug
        if self.game_mode == 1:
            return self.make_random_move(board)

        # if game mode 2 --> strategischer Zug
        if self.game_mode == 2:
            # Prioritäten setzen
            # 1. Methode aufrufen, die KReuz in mitte setzt --> von mitte aus setzt
            # 2. Methode für offensiven Move --> neben Mitte? --> diagnoal fehlt noch!
            # 3. Methode für defensiven Move --> 2er/3er Ketten ermitteln
            #       --> advanced: xxoxx erkennen als fast gewonnen

            # make_defense_move returned True, wenn sie einen Zug setzen kann; wenn er verteidigen muss
            if not self.move_made:
                defense_move = self.make_defense_move(board)
                if defense_move is not None:
                    return defense_move

            if not self.move_made:
                random_move = self.make_random_move(board)
                return random_move

            # if not self.move_made:
            #     return self.make_center_move(board)

    def make_random_move(self, board):
        """
        Funktion für den Zufallsspielzug des Bots
        """
        print("make_random_move()")

        # generiert so lange Zufallszahlen, bis eine gültige gefunden wurde
        while True:
            # random.randint erzeugt Zufallszahlen von 0 bis (exklusive) board.m (Zeilen)
            row = np.random.randint(board.m)
            # random.randint erzeugt Zufallszahlen von 0 bis (exklusive) board.n (Spalten)
            col = np.random.randint(board.n)

            # prüft, ob Zufallsposition noch nicht belegt ist
            if board.fields[row][col] == 0:
                # setzt Zufallsposition auf freies Feld
                self.move_made = True
                return (row, col)
                # board.fields[row][col] = self.player_number
                # beendet Schleife, da Bot seinen Zug nun gesetzt hat

    def make_center_move(self, board):
        """
        VORLÄUFIGE METHODE
        :param board:
        :return:
        """

        print("make_center_move()")

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
            self.move_made = True

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
                    self.move_made = True
                    return

        # Fallunterscheidung, wenn es keine eindeutige Mitte gibt?

        # Überlegung 1: SmartBot soll erkennen, wenn der Gegner kurz davor ist zu gewinnen und dann den Zug verhindern (Verteidigung)
        # Überlegung 2: SmartBot sollte selbst versuchen in einer geraden Linie zu setzen (Angriff)
        # mit Schleife arbeiten? was wenn, Feld belegt ist?

        # random_seat setzen --> macht immer dieselben Zufallszüge --> um Zufall zu bergenzen
        # Bot vs. Bot random, wer anfängt

        # statistiken: Schleife mit bot 100 mal laufen lassen und ergebnisse rausschreiben --> damit evtl in excel weiterarbeiten

    def make_defense_move(self, board):
        """
        :param board:
        :return:
        """

        print("make_defense_move()")

        # check rows
        for row in range(board.m):
            count = 0
            for col in range(board.n):
                if board.fields[row][col] != self.player_number and board.fields[row][col] != 0:
                    count += 1
                    print(count)

                if count == (board.k - 1):
                    print("DEFENSE!! ROW")
                    if board.fields[row][col + 1] == 0:
                        self.move_made = True
                        return (row, (col + 1))
                    else:
                        if board.fields[row][col - (board.k - 1)] == 0:
                            self.move_made = True
                            return (row, (col - (board.k - 1)))
                    break

        # Überprüfung der Spalten
        for col in range(board.n):
            count = 0
            for row in range(board.m):
                if board.fields[row][col] != self.player_number and board.fields[row][col] != 0:
                    count += 1
                    print(count)

                if count == (board.k - 1):
                    print("DEFENSE!! COL")
                    if board.fields[row + 1][col] == 0:
                        self.move_made = True
                        return ((row + 1), col)
                    else:
                        if board.fields[row - (board.k - 1)][col] == 0:
                            self.move_made = True
                            return ((row - (board.k - 1)), col)
                    break

        # Überprüfung der Diagonalen (von links oben nach rechts unten)
        for row in range(board.m - board.k + 1):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row + diagonal][col + diagonal] != self.player_number and \
                            board.fields[row + diagonal][col + diagonal] != 0:
                        count += 1
                        print(count)

                    if count == (board.k - 1):
                        print("DEFENSE!! DIAGONAL")
                        if board.fields[row + (board.k - 1)][col + (board.k - 1)] == 0:
                            self.move_made = True
                            return ((row + (board.k - 1)), (col + (board.k - 1)))
                        else:
                            if board.fields[row - 1][col - 1] == 0:
                                self.move_made = True
                                return ((row - 1), (col - 1))
                        break

        # Überprüfung der umgekehrten Diagonalen (von links unten nach rechts oben)
        for row in range(board.k - 1, board.m):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row - diagonal][col + diagonal] != self.player_number and \
                            board.fields[row - diagonal][col + diagonal] != 0:
                        count += 1

                    if count == (board.k - 1):
                        print("DEFENSE!! REVERSED DIAGONAL")
                        if board.fields[row - (board.k - 1)][col + (board.k - 1)] == 0:
                            self.move_made = True
                            return ((row - (board.k - 1)), (col + (board.k - 1)))
                        else:
                            if board.fields[row + 1][col - 1] == 0:
                                self.move_made = True
                                return ((row + 1), (col - 1))
                        break
