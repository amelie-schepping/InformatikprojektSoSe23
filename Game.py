from Player import Player
from Board import Board
from MyBot import MyBot

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
    Funktion, die das Spiel startet
    """
    def start(self):

        self.Game(5, 5, 4)

        # Darstellung des Spielfelds
        # wer fängt an?




    """
    Funktion, die einen Spielablauf regelt
    """
    def game_loop(self):

        # self.start()
        print(self.board.fields)
        self.player1.make_move(self.board)
        print(self.board.fields)

        self.player2.make_move(self.board)
        print(self.board.fields)


    # start aufrufen
    # make_move Spieler 1 / 2 abwechselnd,
    # wer hat gewonnen? has_won()
    # Ende: Spielfeld auf Null setzen