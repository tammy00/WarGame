from WarGame.deckofcard import DeckOfCard
from WarGame.player import Player


class CardGame:
    def __init__(self, player1, player2, cards_number=26):
        if cards_number > 26 or cards_number < 10:
            cards_number = 26
        self.player1 = Player(player1, cards_number)
        self.player2 = Player(player2, cards_number)
        self.deckofcards = DeckOfCard()
        self.newgame()

    def newgame(self):
        if self.player1.player_Deckofcards == [] and self.player2.player_Deckofcards == []:
            self.deckofcards.cards_shuffle()
            self.player1.set_hand(self.deckofcards)
            self.deckofcards.cards_shuffle()
            self.player2.set_hand(self.deckofcards)
        else:
            raise SystemError("game already started")

    def __str__(self):
        pass

    def getwinner(self):
        if len(self.player1.player_Deckofcards) > len(self.player2.player_Deckofcards):
            return self.player1
        if len(self.player1.player_Deckofcards) < len(self.player2.player_Deckofcards):
            return self.player2
        else:
            return None
