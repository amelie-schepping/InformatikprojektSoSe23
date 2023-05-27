from Player import Player

"""
Die Klasse MySmartBot ist eine Subklasse von der Klasse Player
"""

class MySmartBot(Player):
    """
    Konstruktor der Klasse MySmartBot
    - initialisiert folgende Instanzvariablen
    name: Name vom Bot
    player_number: Bot ist Player 1 oder 2
    symbol: Symbol des Bots für die Spielzüge
    """

    def __init__(self, name, player_number, symbol):
        self.name = name
        self.player_number = player_number
        self.symbol = symbol

    """
    Funktion für den strategischen Spielzug des Bots
    """
    #def make_move(self, board):

