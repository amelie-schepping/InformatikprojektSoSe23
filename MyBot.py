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

            if not self.move_made:
                winning_move = self.make_winning_move(board)
                if winning_move is not None:
                    return winning_move

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
                print(row, col)
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

        # Berechne die Mitte des Spielfelds
        # wird automatisch gerundet
        rowMid = board.m // 2
        colMid = board.n // 2

        # versuche zunächst in die Mitte zu setzen
        if board.fields[rowMid][colMid] == 0:
            self.move_made = True
            return (rowMid, colMid)

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
                    if board.is_move_valid(row, (col + 1)):
                        self.move_made = True
                        return (row, (col + 1))
                    else:
                        if board.is_move_valid(row, (col - (board.k - 1))):
                            self.move_made = True
                            return (row, (col - (board.k - 1)))

        # Überprüfung der Spalten
        for col in range(board.n):
            count = 0
            for row in range(board.m):
                if board.fields[row][col] != self.player_number and board.fields[row][col] != 0:
                    count += 1
                    print(count)

                if count == (board.k - 1):
                    print("DEFENSE!! COL")
                    if board.is_move_valid((row + 1), col):
                        self.move_made = True
                        return ((row + 1), col)
                    else:
                        if board.is_move_valid((row - (board.k - 1)), col):
                            self.move_made = True
                            return ((row - (board.k - 1)), col)

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
                        if board.is_move_valid((row + (board.k - 1)), (col + (board.k - 1))):
                            self.move_made = True
                            return ((row + (board.k - 1)), (col + (board.k - 1)))
                        else:
                            if board.is_move_valid((row - 1), (col - 1)):
                                self.move_made = True
                                return ((row - 1), (col - 1))

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
                        if board.is_move_valid((row - (board.k - 1)), (col + (board.k - 1))):
                            self.move_made = True
                            return ((row - (board.k - 1)), (col + (board.k - 1)))
                        else:
                            if board.is_move_valid((row + 1), (col - 1)):
                                self.move_made = True
                                return ((row + 1), (col - 1))

    def make_winning_move(self, board):
        """
        :param board:
        :return:
        """

        print("make_winning_move()")

        # check rows
        for row in range(board.m):
            count = 0
            for col in range(board.n):
                if board.fields[row][col] == self.player_number:
                    count += 1
                    print(count)

                if count == (board.k - 1):
                    print("OFFENSE!! ROW")
                    if board.is_move_valid(row, (col + 1)):
                        self.move_made = True
                        return (row, (col + 1))
                    else:
                        if board.is_move_valid(row, (col - (board.k - 1))):
                            self.move_made = True
                            return (row, (col - (board.k - 1)))

        # Überprüfung der Spalten
        for col in range(board.n):
            count = 0
            for row in range(board.m):
                if board.fields[row][col] == self.player_number:
                    count += 1
                    print(count)

                if count == (board.k - 1):
                    print("OFFENSE!! COL")
                    if board.is_move_valid((row + 1), col):
                        self.move_made = True
                        return ((row + 1), col)
                    else:
                        if board.is_move_valid((row - (board.k - 1)), col):
                            self.move_made = True
                            return ((row - (board.k - 1)), col)

        # Überprüfung der Diagonalen (von links oben nach rechts unten)
        for row in range(board.m - board.k + 1):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row + diagonal][col + diagonal] == self.player_number:
                        count += 1
                        print(count)

                    if count == (board.k - 1):
                        print("OFFENSE!! DIAGONAL")
                        if board.is_move_valid((row + (board.k - 1)), (col + (board.k - 1))):
                            self.move_made = True
                            return ((row + (board.k - 1)), (col + (board.k - 1)))
                        else:
                            if board.is_move_valid((row - 1), (col - 1)):
                                self.move_made = True
                                return ((row - 1), (col - 1))

        # Überprüfung der umgekehrten Diagonalen (von links unten nach rechts oben)
        for row in range(board.k - 1, board.m):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row - diagonal][col + diagonal] == self.player_number:
                        count += 1

                    if count == (board.k - 1):
                        print("OFFENSE!! REVERSED DIAGONAL")
                        if board.is_move_valid((row - (board.k - 1)), (col + (board.k - 1))):
                            self.move_made = True
                            return ((row - (board.k - 1)), (col + (board.k - 1)))
                        else:
                            if board.is_move_valid((row + 1), (col - 1)):
                                self.move_made = True
                                return ((row + 1), (col - 1))
