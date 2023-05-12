from Player import Player

"""
Die Klasse MyBot ist eine Subklasse von der Klasse Player
"""
class MyBot(Player):

    """
    Funktion für den Spielzug des Bots
    """
    def make_move(self, _board):
        self.row = 0
        self.col = 0

