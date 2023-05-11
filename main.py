class Board:
    """
    Instanzvariablen der Klasse Board
    m: Zeile
    n: Spalte
    k: Gewinnbedingung (Anzahl eines Symbols in einer Reihe für einen Gewinn)
    """
    m = 5
    n = 5
    k = 4

    """
    Konstruktor der Klasse Board
    - initialisiert die Instanzvariablen des Spielfelds
    :param _m: Zeilenanzahl des Spielfelds
    :param _n: Spaltenanzahl des Spielfelds
    """
    def initialize(_m, _n):
        m = _m
        n = _n
        #sollten wir hier evtl. auch k initialisieren?

    """
    Funktion, um das Spielfeld auf den Startzustand zurückzusetzen
    """
    def reset():

    """
    Funktion (wofür??)
    """
    def display():

    """
    Funktion, die zurückgibt, ob das Spiel gewonnen wurde
    0 = unentschieden
    1 = Sieg Spieler 1
    2 = Sieg Spieler 2
    :return: gibt an, wer gewonnen hat (s.o.)
    """
    def has_won():
        return 0


class Player:
    """
    Instanzvariablen der Klasse Player
    name: Name von Player
    player_number: Player 1 oder 2
    symbol: Symbol des Players für die Spielzüge
    """
    name = ""
    player_number = 0 # 1 or 2
    symbol = "" # x or o

    """
    Funktion für einen Spielzug eines Players
    - fordert eine Eingabe des/der Players über die Konsole ein
    - setzt die Konsoleneingabe als Spielzug auf dem Board 
    """
    def make_move(_board):
        row = 0
        col = 0

"""
Die Klasse MyBot ist eine Subklasse von der Klasse Player
"""
class MyBot(Player):

    """
    Funktion für den Spielzug des Bots
    """
    def make_move(_board):
        row = 0
        col = 0


class Game:
    """
    Instanzvariablen der Klasse Board
    m: Zeile
    n: Spalte
    k: Gewinnbedingung (Anzahl eines Symbols in einer Reihe für einen Gewinn)
    board: Spielfeld
    player1: Player 1
    player2: Player 2
    """
    m = 5
    n = 5
    k = 4

    board = Board
    player1 = Player
    player2 = Player

    """
    Funktion, die das Spiel startet
    """
    def start():

    """
    Konstruktor der Klasse Game
    - setzt die Instanzvariablen des Games
    """
    def initialize():


    """
    Funktion, die einen Spielablauf regelt
    """
    def game_loop():