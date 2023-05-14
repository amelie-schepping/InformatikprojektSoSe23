from Player import Player
from Board import Board
from MyBot import MyBot

import random

class Game:
    """
    Konstruktor der Klasse Game
    - setzt die Instanzvariablen des Games
    m: Zeile
    n: Spalte
    k: Gewinnbedingung (Anzahl eines Symbols in einer Reihe für einen Gewinn)
    board: Spielfeld
    player1: Player 1
    player2: Player 2
    """

    def __init__(self, m, n, k):
        self.board = Board(m, n)
        self.player1 = Player("Player1", 1, 'X')
        self.player2 = Player("Player2", 2, 'O')



    """
    Funktion bestimmt den/die Startspieler:in
    :return: gibt Startspieler:in zurück
    """
    def determing_starting_player(self):
        starting_player = random.choice([self.player1, self.player2])
        return starting_player

    """
    Funktion regelt Spielablauf
    """

    def game_loop(self):

        print("Welcome to Break - a Game for Smart Minds", "\n")
        self.start()

        # welcher Spieler fängt an
        starting_player_in_game = self.determing_starting_player()
        print(f"The starting player is: {starting_player_in_game.name}\n")


        # beginn while schleife
        # statt player1 --> current player

        # current player?? its ... turn
        # while schleife mit welcher Bedingung --> board.has_won() != Null (is not None?)
        # make_move Spieler 1 / 2 abwechselnd,
        # solange es keinen Gewinner gibt
        # Ende: Spielfeld auf Null setzen


        # -1 für Indexierung
        row = int(input("Enter row: ")) - 1
        col = int(input("Enter column: ")) - 1
        #Startpieler:in soll ersten Zug machen
        starting_player_in_game.make_move(self.board, row, col)
        self.board.display()

        # nach jeder eingabe muss gecheckt werden, ob es einen Gewinner gibt
        # if self.board.has_won == 0: print("unentschieden") ...



    """
    Funktion startet das Spiel
    - die Spielenden geben sich ihre Namen
    - das Spielfeld wird angezeigt
    """
    def start(self):

        #Spieler:innen geben sich Namen
        print("Player 1! ")
        self.player1.set_player_name()
        print("Player 2!")
        self.player2.set_player_name()

        print("THE GAME STARTS....NOW!")
        # Feld ausgeben
        self.board.display()
