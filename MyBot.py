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
        gibt ein Tupel zurück
        :param board:
        :return: tuple (row:int col: int)
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

            #if not self.move_made:
                #offense_move = self.make_offense_move(board)
                #if offense_move is not None:
                    #return offense_move

            if not self.move_made:
                center_move = self.make_center_move(board)
                return center_move

            if not self.move_made:
                random_move = self.make_random_move(board)
                return random_move


    def make_center_move(self, board):
        """
        VORLÄUFIGE METHODE
        :param board:
        :return:
        """

        # Berechne die Mitte des Spielfelds
        # wird automatisch gerundet
        rowMid = board.m // 2
        colMid = board.n // 2

        starting_position = (rowMid, colMid)

        # versuche zunächst in die Mitte zu setzen
        if board.is_move_valid(starting_position[0], starting_position[1]):
            self.move_made = True
            print(f"in die mitte gesetzt {self.player_number}")
            return starting_position

        # postions next to the middle
        else:
            mid_positions = []

            mid_positions.append((rowMid, colMid + 1))
            mid_positions.append((rowMid + 1, colMid + 1))
            mid_positions.append((rowMid + 1, colMid))
            mid_positions.append((rowMid + 1, colMid - 1))
            mid_positions.append((rowMid, colMid - 1))
            mid_positions.append((rowMid - 1, colMid - 1))
            mid_positions.append((rowMid - 1, colMid))
            mid_positions.append((rowMid - 1, colMid + 1))

            while True:
                starting_position = random.choice(mid_positions)
                if board.is_move_valid(starting_position[0], starting_position[1]):
                    self.move_made = True
                    print(f"fast in die mitte gesetzt {self.player_number}")
                    return starting_position

    def make_defense_move(self, board):
        """
        :param board:
        :return:
        """

        # check rows
        for row in range(board.m):
            count = 0
            for col in range(board.n):
                if board.fields[row][col] != self.player_number and board.fields[row][col] != 0:
                    count += 1

                if count == (board.k - 1):
                    if board.is_move_valid(row, col + 1):
                        self.move_made = True
                        print(f"defense row rechts {self.player_number}")
                        return (row, col + 1)
                    else:
                        if board.is_move_valid(row, col - (board.k - 1)):
                            self.move_made = True
                            print(f"defense row links {self.player_number}")
                            return (row, col - (board.k - 1))

        # Überprüfung der Spalten
        for col in range(board.n):
            count = 0
            for row in range(board.m):
                if board.fields[row][col] != self.player_number and board.fields[row][col] != 0:
                    count += 1

                if count == (board.k - 1):
                    if board.is_move_valid(row + 1, col):
                        self.move_made = True
                        print(f"defense col unten {self.player_number}")
                        return (row + 1, col)
                    else:
                        if board.is_move_valid(row - (board.k - 1), col):
                            self.move_made = True
                            print(f"defense col oben {self.player_number}")
                            return (row - (board.k - 1), col)

        # Überprüfung der Diagonalen (von links oben nach rechts unten)
        for row in range(board.m - board.k + 1):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row + diagonal][col + diagonal] != self.player_number and \
                            board.fields[row + diagonal][col + diagonal] != 0:
                        count += 1

                    if count == (board.k - 1):
                        if board.is_move_valid(row + (board.k - 1), col + (board.k - 1)):
                            self.move_made = True
                            print(f"defense diagonale rechts unten {self.player_number}")
                            return (row + (board.k - 1), col + (board.k - 1))
                        else:
                            if board.is_move_valid(row - 1, col - 1):
                                self.move_made = True
                                print(f"defense diagonale links oben {self.player_number}")
                                return (row - 1, col - 1)

        # Überprüfung der umgekehrten Diagonalen (von links unten nach rechts oben)
        for row in range(board.k - 1, board.m):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row - diagonal][col + diagonal] != self.player_number and \
                            board.fields[row - diagonal][col + diagonal] != 0:
                        count += 1

                    if count == (board.k - 1):
                        if board.is_move_valid(row - (board.k - 1), col + (board.k - 1)):
                            self.move_made = True
                            print(f"defense diagonale rechts oben {self.player_number}")
                            return row - (board.k - 1), col + (board.k - 1)
                        else:
                            if board.is_move_valid(row + 1, col - 1):
                                self.move_made = True
                                print(f"defense diagonale links unten {self.player_number}")
                                return row + 1, col - 1

    def make_offense_move(self, board):
        # check rows
        for row in range(board.m):
            count = 0
            for col in range(board.n):
                if board.fields[row][col] == self.player_number:
                    count += 1

                if count == (board.k - 2):
                    if board.is_move_valid(row, (col + 1)):
                        self.move_made = True
                        print(f"offense row rechts {self.player_number}")
                        return (row, (col + 1))
                    else:
                        if board.is_move_valid(row, (col - (board.k - 2))):
                            self.move_made = True
                            print(f"offense row links {self.player_number}")
                            return (row, (col - (board.k - 2)))

        # Überprüfung der Spalten
        for col in range(board.n):
            count = 0
            for row in range(board.m):
                if board.fields[row][col] == self.player_number:
                    count += 1

                if count == (board.k - 2):
                    if board.is_move_valid((row + 1), col):
                        self.move_made = True
                        print(f"offense col unten {self.player_number}")
                        return ((row + 1), col)
                    else:
                        if board.is_move_valid((row - (board.k - 2)), col):
                            self.move_made = True
                            print(f"offense col oben {self.player_number}")
                            return ((row - (board.k - 2)), col)

        # Überprüfung der Diagonalen (von links oben nach rechts unten)
        for row in range(board.m - board.k + 1):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row + diagonal][col + diagonal] == self.player_number:
                        count += 1

                    if count == (board.k - 2):
                        if board.is_move_valid((row + (board.k - 1)), (col + (board.k - 1))):
                            self.move_made = True
                            print(f"offense diagonale rechts unten {self.player_number}")
                            return ((row + (board.k - 1)), (col + (board.k - 1)))
                        else:
                            if board.is_move_valid((row - 1), (col - 1)):
                                self.move_made = True
                                print(f"offense diagonale links oben {self.player_number}")
                                return ((row - 1), (col - 1))

        # Überprüfung der umgekehrten Diagonalen (von links unten nach rechts oben)
        for row in range(board.k - 1, board.m):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row - diagonal][col + diagonal] == self.player_number:
                        count += 1

                    if count == (board.k - 2):
                        if board.is_move_valid((row - (board.k - 1)), (col + (board.k - 1))):
                            self.move_made = True
                            print(f"offense diagonale rechts oben {self.player_number}")
                            return ((row - (board.k - 1)), (col + (board.k - 1)))
                        else:
                            if board.is_move_valid(row, col):
                                self.move_made = True
                                print(f"offense diagonale links unten {self.player_number}")
                                return (row , col)

    def make_random_move(self, board):
        """
        Funktion für den Zufallsspielzug des Bots
        """

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
                print(f"random move {self.player_number}")
                return (row, col)
                # board.fields[row][col] = self.player_number
                # beendet Schleife, da Bot seinen Zug nun gesetzt hat

    def make_winning_move(self, board):
        """
        :param board:
        :return:
        """

        # check rows
        for row in range(board.m):
            count = 0
            for col in range(board.n):
                if board.fields[row][col] == self.player_number:
                    count += 1

                if count == (board.k - 1):
                    if board.is_move_valid(row, (col + 1)):
                        self.move_made = True
                        print(f"winning row rechts {self.player_number}")
                        return (row, (col + 1))
                    else:
                        if board.is_move_valid(row, (col - (board.k - 1))):
                            self.move_made = True
                            print(f"winning row links {self.player_number}")
                            return (row, (col - (board.k - 1)))

        # Überprüfung der Spalten
        for col in range(board.n):
            count = 0
            for row in range(board.m):
                if board.fields[row][col] == self.player_number:
                    count += 1

                if count == (board.k - 1):
                    if board.is_move_valid((row + 1), col):
                        self.move_made = True
                        print(f"winning col unten {self.player_number}")
                        return ((row + 1), col)
                    else:
                        if board.is_move_valid((row - (board.k - 1)), col):
                            self.move_made = True
                            print(f"winning col oben {self.player_number}")
                            return ((row - (board.k - 1)), col)

        # Überprüfung der Diagonalen (von links oben nach rechts unten)
        for row in range(board.m - board.k + 1):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row + diagonal][col + diagonal] == self.player_number:
                        count += 1

                    if count == (board.k - 1):
                        if board.is_move_valid(row - (board.k - 1), col + (board.k - 1)):
                            self.move_made = True
                            print(f"winning diagonale rechts unten {self.player_number}")
                            return row - (board.k - 1), col + (board.k - 1)
                        else:
                            if board.is_move_valid(row - 1, col - 1):
                                self.move_made = True
                                print(f"winning diagonale links oben {self.player_number}")
                                return row - 1, col - 1

        # Überprüfung der umgekehrten Diagonalen (von links unten nach rechts oben)
        for row in range(board.k - 1, board.m):
            for col in range(board.n - board.k + 1):
                count = 0
                for diagonal in range(board.k):
                    if board.fields[row - diagonal][col + diagonal] == self.player_number:
                        count += 1

                    if count == (board.k - 1):
                        if board.is_move_valid((row - (board.k - 1)), (col + (board.k - 1))):
                            self.move_made = True
                            print(f"winning diagonale rechts oben {self.player_number}")
                            return ((row - (board.k - 1)), (col + (board.k - 1)))
                        else:
                            if board.is_move_valid((row + 1), (col - 1)):
                                self.move_made = True
                                print(f"winning diagonale links unten {self.player_number}")
                                return ((row + 1), (col - 1))
