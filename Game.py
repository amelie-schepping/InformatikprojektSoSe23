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
    Funktion startet das Spiel
    - gibt das Startfeld aus
    """

    def start(self):

        # Feld ausgeben
        self.board.display()

        # wer fängt an?

    """
    Funktion, die einen Spielablauf regelt
    """

    def game_loop(self):
        # current player?? its ... turn
        # while schleife mit welcher Bedingung --> board.has_won() != Null (is not None?)
        # solange es keinen Gewinner gibt

        # Player können sich eigene Namen geben?

        print("THE GAME STARTS....NOW!")
        self.start()
        # beginn while schleife
        # statt player1 --> current player

        # -1 für Indexierung
        row = int(input("Enter row: ")) - 1
        col = int(input("Enter column: ")) - 1
        self.player1.make_move(self.board, row, col)
        self.board.display()

        # nach jeder eingabe muss gecheckt werden, ob es einen Gewinner gibt
        # if self.board.has_won == 0: print("unentschieden") ...

    # start aufrufen
    # make_move Spieler 1 / 2 abwechselnd,
    # wer hat gewonnen? has_won()
    # Ende: Spielfeld auf Null setzen
