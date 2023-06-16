from Player import Player
from Board import Board
from MyBot import MyBot
from MySmartBot import MySmartBot

import random


class Game:


    def __init__(self, m, n, k):
        """
        Konstruktor der Klasse Game
        - setzt die Instanzvariablen des Games
        board: Spielfeld
        player1: Player 1
        player2: Player 2
        :param m: Zeilen des Spielfelds
        :param n: Spalten des Spielfelds
        :param k: Gewinnbedingung (Anzahl eines Symbols in einer Reihe für einen Gewinn)
        """
        self.k = k
        self.board = Board(m, n, k)
        self.player1 = Player("Player1", 1, 'X')
        self.player2 = Player("Player2", 2, 'O')

        # Spieler:in, der/die gerade dran ist - wird zunächst mit Player 1 initialisiert
        self.current_player = self.player1



    def change_current_player(self):
        """
        Funktion wechselt den/die aktuelle:n Spieler:in
        """
        if self.player1 == self.current_player:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    """
    Funktion wandelt Player.player_number in Player.symbol um
    """

    # def convert_to_symbol(self):



    def determing_starting_player(self):
        """
           Funktion bestimmt den/die Startspieler:in zufällig
           :return: gibt Startspieler:in zurück
        """
        starting_player = random.choice([self.player1, self.player2])
        return starting_player



    def game_loop(self):
        """
        Funktion regelt Spielablauf
        """
        # vor dem eigentlichen Gameloop wird das Spiel gestartet
        self.start()

        # Startspieler:in wird zufällig gewählt und auf Konsole ausgegeben
        starting_player_in_game = self.determing_starting_player()
        print(f"The starting player is: {starting_player_in_game.name}\n")

        # Startspieler:in wird als aktuelle Spieler:in gesetzt
        self.current_player = starting_player_in_game

        # Beginn des Gameloops
        while not self.board.is_game_won_by(self.current_player.player_number):
            # solange niemand gewonnen hat:

            # Name des aktuellen Spielers wird auf die Konsole ausgegeben
            print(f"{self.current_player.name}, it's your turn!")

            # aktueller Spieler macht einen Spielzug
            self.current_player.make_move(self.board)

            # Anzeigen des gesetzten Spielzugs
            # in display wird auch die player_number vom Symbol überlagert
            self.board.display()

            # checken, ob es einen Gewinner gibt
            if self.board.is_game_won_by(self.current_player.player_number):
                # das Spiel wurde gewonnen, der Gameloop wird mit break verlassen
                break

            # checken, ob das Spielfeld voll ist
            if self.board.is_board_full():
                # das Spielfeld ist voll, der Gameloop wird mit break verlassen
                break

            # das Spiel wurde noch nicht gewonnen
            # aktueller Spieler wird gewechselt, while-Schleife beginnt von vorne
            self.change_current_player()

        # Ende des Gameloops

        # das Spiel wurde gewonnen, Gewinner:in ermitteln
        winner = self.board.has_won(self.current_player.player_number)

        # Gewinner:in auf die Konsole ausgeben
        if winner == 1:
            print(f"Congratulations {self.player1.name}! You have won!")

        if winner == 2:
            print(f"Congratulations {self.player2.name}! You have won!")

        if winner == 0:
            print("This game ended in a draw. Try again!")

        # Spiel beenden
        input("\n ----------> Press Enter to end the game. <----------")
        # Ende: Spielfeld auf null setzen
        self.board = None


    # def get_valid_move(self):
    """
       Funktion fordert einen gültigen Spielzug von current_player ein
       :return: gibt einen gültigen Spielzug zurück
    """


    def start(self):
        """
        Funktion startet das Spiel
        - die Spielenden geben sich ihre Namen
        - das Spielfeld wird angezeigt
        """

        # Willkommensnachricht zum Start des Spiels
        print("Welcome to Break - a Game for Smart Minds", "\n")

        # Spiel Modus-Abfrage
        # mögliche Spielmodi werden auf die Konsole ausgegeben
        print("GAME MODE")
        print("-- 1: Player vs Player -- ")
        print("-- 2: Player vs. Bot --")
        print("-- 3: Bot vs. Bot --")
        # print("-- 2: Player vs Bot (easy) -- ")
        # print("-- 3: Player vs Bot (hard) -- ")
        # print("-- 4: Bot vs Bot  -- ")

        # Eingabe muss valid sein: Value Error Exception!! catchen
        # Mensch wird aufgefordert, einen Spielmodus einzugeben
        ans = int(input("Enter the number of your choice: "))

        # je nachdem, welcher Spiel-Modus angefordert wird, passiert unterschiedliches

        # Spielmodus 1 (Mensch vs. Mensch)
        if ans == 1:
            # Spieler:innen geben sich Namen
            print("Player 1! ")
            self.player1.set_player_name()
            print("Player 2!")
            self.player2.set_player_name()

        if ans == 2:
            # Solo-Spieler:in gibt sich Namen
            print("Player 1! ")
            self.player1.set_player_name()

            # Solo-Spieler:in bestimmt, wie stark der Bot sein soll
            print("Choose the strength of your opponent:")
            print("for level 1 press -- 1")
            print("for level 2 press -- 2")

            gamemode = int(input("Enter your choice: "))
            # Player 2 wird als Bot initialisiert, der mit der gewählten Stärke spielt
            self.player2 = MyBot("MyBot",2,'0',gamemode)




        """
        # Spielmodus 2 (Mensch vs. Zufall)
        if ans == 2:
            # Solo-Spieler:in gibt sich Namen
            print("Player 1! ")
            self.player1.set_player_name()

            # Player 2 wird automatisch als (Zufalls-)Bot gesetzt
            self.player2 = MyBot("MyBot", 2, 'O')

        # Spielmodus 3 (Mensch vs. Bot)
        if ans == 3:
            print("Achtung! Dieser Spielmodus befindet sich in der Entwicklung.")

            # Solo-Spieler:in gibt sich Namen
            print("Player 1! ")
            self.player1.set_player_name()

            # Player 2 wird automatisch als (strategischer) Bot gesetzt
            self.player2 = MySmartBot("MySmartBot", 2, 'O')
                    # Spielmodus 4 (Bot vs. Bot)
        if ans == 4:
            # beide Player werden automatisch als (strategische) Bots gesetzt
            self.player1 = MyBot("MyBot 1", 1, 'X')
            self.player2 = MyBot("MyBot 2", 2, 'O')
        """

        # Spielmodus 4 (Bot vs. Bot)
        if ans == 3:
            # Stärke der Bots wählen
            print("Choose the strength of the opponents: ")
            print("for level 1 press -- 1")
            print("for level 2 press -- 2")

            gamemode1 = int(input("Enter your choice for your first Bot: "))
            gamemode2 = int(input("Enter your choice for your second Bot: "))

            # beide Player werden automatisch als (strategische) Bots gesetzt
            self.player1 = MyBot("MyBot 1", 1, 'X',gamemode1)
            self.player2 = MyBot("MyBot 2", 2, 'O',gamemode2)

        # Spielbeginn ankündigen
        print("YOUR GAME STARTS....NOW!")

        # Feld ausgeben
        self.board.display()