import numpy as np


class Board:


    def __init__(self, m, n, k):
        """
        Konstruktor der Klasse Board
        - initialisiert die Instanzvariablen des Spielfelds
        - erstellt ein leeres Spielfeld
        :param m: Zeilenanzahl des Spielfelds
        :param n: Spaltenanzahl des Spielfelds
        :param k: Gewinnbedingung (Anzahl von Treffern in einer Reihe)
        """
        self.m = m
        self.n = n
        self.k = k
        self.fields = np.zeros((m, n), dtype=int)



    def display(self):
        """
        Funktion stellt das Spielfeld in einem nummerierten Raster dar
        und erstellt ein 'zweites' Spielfeld mit Symbolen, das das erste Spielfeld
        mit den Zahlen überlagert (der Code arbeitet weiterhin mit player_number,
        nur die Darstellung/das darüber liegende Display wird mit Symbolen angezeigt)
        """
        print()
        # Überschrift Spalten
        print("\t", end='')
        for row in range(self.n):
            print(row + 1, "\t", end='')

        print()

        for row in range(self.m):
            # Überschrift Zeilen
            print(row + 1, "\t", end='')
            for col in range(self.n):
                # Erzeugung eines neuen Arrays mit den entsprechenden Strings
                # das neue Array 'überlagert' das alte Array, löscht das alte Array aber nicht
                # 1 in X, 2 in O, 0 in "[ ]"
                # fields_strings = np.where(self.fields == 1, "X", np.where(self.fields == 2, "O", "/"))
                # print(fields_strings[row][col], "\t", end='')

                print(self.fields[row][col], "\t", end='')

            print()

        print()



    def has_won(self, current_player_number):
        """
        Funktion, die zurückgibt, wer das Spiel gewonnen hat
        0 = unentschieden
        1 = Sieg Spieler 1
        2 = Sieg Spieler 2
        :param current_player_number: Spielernummer des Spielers, der den letzten Zug gesetzt hat
        :return: gibt an, wer gewonnen hat (s.o.)
        """
        # Methode has_won wird aufgerufen, falls das Spielfeld voll ist
        # oder falls es eine Gewinnerin gibt

        # daher als erstes noch einmal überprüfen, ob es einen Gewinner gibt
        if self.is_game_won_by(current_player_number):
            # der Spieler, der als letztes dran war, hat gewonnen
            if current_player_number == 1:
                return 1

            if current_player_number == 2:
                return 2
        # es gibt keinen Gewinner, d. h. das Feld ist voll
        else:
            return 0



    def is_board_full(self):
        """
        Funktion prüft, ob das Spielfeld voll ist, d.h.
        jedes Feld im Spielfeld ist mit einem Symbol besetzt
        :return: ja, Spielfeld ist voll/nein, Spielfeld ist nicht voll
        """

        # doppelte Schleife durch 2D-Array/Spielfeld
        for row in range(self.m):
            for col in range(self.n):

                # für jede Position prüfen, ob das Feld unbelegt ist (also gleich 0)
                if self.fields[row, col] == 0:
                    # falls mind. ein Feld unbelegt: nein, das Spielfeld ist noch nicht voll
                    return False
        # da, wie oben geprüft, kein Feld mehr frei, müssen alle Felder belegt sein
        # ja, das Spielfeld ist voll
        return True



    def is_game_won_by(self, player_number):
        """
        Funktion gibt zurück, ob ein Player das Spiel gewonnen hat
        :param player_number: Nummer von Player, für den/die geprüft wird, ob er/sie gewonnen hat
        :return: der angegeben Player hat das Spiel gewonnen (ja/nein)
        """
        # Überprüfung in Zeilen
        for row in range(self.m):
            # Zähler
            count = 0
            for col in range(self.n):
                if self.fields[row, col] == player_number:
                    # Zähler wird hochgezählt, wenn player_number auftaucht
                    count += 1
                    if count == self.k:
                        return True
                        count = 0
                else:
                    # Zähler zurücksetzen bei Unterbrechung
                    count = 0

        # Überprüfung in Spalten
        for col in range(self.n):
            count = 0
            for row in range(self.m):
                if self.fields[row, col] == player_number:
                    count += 1
                    if count == self.k:
                        return True
                else:
                    count = 0

        # Überprüfung in Diagonale
        # sicherstellen, dass Startposition mindestens k Elemente von den Rändern der Zeilen und Spalten entfernt ist
        for row in range(self.m - self.k + 1):
            for col in range(self.n - self.k + 1):
                # Zähler
                count = 0
                for diagonal in range(self.k):
                    if self.fields[row + diagonal, col + diagonal] == player_number:
                        count += 1
                        if count == self.k:
                            return True
                            count = 0
                    else:
                        count = 0

        # Überprüfung in der umgekehrten Diagonalen
        for row in range(self.m - self.k + 1):
            for col in range(self.n - 1, self.k - 2, -1):
                count = 0
                for diagonal in range(self.k):
                    if self.fields[row + diagonal, col - diagonal] == player_number:
                        count += 1
                        if count == self.k:
                            return True
                    else:
                        count = 0

        return False



    def is_move_valid(self, row, col):
        """
        Funktion prüft, ob ein Spielzug gültig ist, d.h.
        - ob die eingegebene Position im Spielfeld liegt
        - ob die eingegebene Position bereits belegt ist
        :param row: Zeile der eingegebenen Position
        :param col: Spalte der eingegebenen Position
        :return: gültig (ja/nein)
        """
        # die von Computer/Mensch eingegebenen Werte
        # orientieren sich am gewählten Display
        # und müssen zuerst zu korrekten Array-Indexen umgeformt werden
        row = row - 1
        col = col - 1

        # eingegebene Zeile muss im Spielfeld liegen
        condition_rows = (0 <= row < self.m)

        # eingegebene Spalte muss im Spielfeld liegen
        condition_cols = (0 <= col < self.n)

        # eingegebene Position darf noch nicht belegt sein
        condition_position = (self.fields[row][col] == 0)

        # Abfrage, ob Bedingungen true oder false sind
        if condition_rows and condition_cols and condition_position:
            return True

        # falls eine der Bedingungen nicht true ist,
        # ist der Spielzug ungültig
        else:
            return False
