class Board:
    """
    Instanzvariablen der Klasse Board
    m: Zeile
    n: Spalte
    k: Gewinnbedingung (Anzahl des eigenen Symbols in einer Reihe)
    """
    m = 5
    n = 5
    k = 4

    """
    Konstruktor
    - initialisiert die Instanzvariablen des Spielfelds
    :param _m: Zeilenanzahl des Spielfelds
    :param _n: Spaltenanzahl des Spielfelds
    """
    def initialize(_m, _n):
        m = _m
        n = _n

    def reset():


    def display():

    """
    Funktion, die zurückgibt, ob das Spiel gewonnen wurde
    :return: gibt an, wer gewonnen hat
    """
    def has_won():
        return 0
class Player:
    name = ""
    player_number = 0 # 1 or 2
    symbol = "" # x or o

    def make_move(_board):
        row = 0
        col = 0

class MyBot(Player):
    def make_move(_board):
        row = 0
        col = 0

class Game:
    m = 5
    n = 5
    k = 4

    Board
    Player

    def start():

    def initialize():



    def game_loop():