from unittest import TestCase, mock
from WarGame.cardgame import CardGame
from WarGame.player import Player
from WarGame.deckofcard import DeckOfCard


class TestCardGame(TestCase):

    def setUp(self):
        self.obj_cardgame = CardGame('name1', 'name2', 26)

    def test__init(self):
        # when cards_number > 26
        # when cards_number < 10
        # 10 < when cards_number < 26
        # when cards_number is NULL
        # is players obj correct
        self.assertTrue(type(self.obj_cardgame.player1) == Player)
        # is deckofcards's type = DeckOfCard
        self.assertTrue(type(self.obj_cardgame.deckofcards) == DeckOfCard)

    def test_newgame_invalid(self):
        # when game already started
        self.obj_cardgame.player2.player_Deckofcards = [['card1']]
        self.obj_cardgame.player1.player_Deckofcards = [['card1']]
        with self.assertRaises(SystemError):
            self.obj_cardgame.newgame()

    def test_newgame_valid(self):
        # players Deckofcards gets cards- game yet been started
        obj_cardgame = CardGame('moshe', 'miri', 10)
        self.assertTrue(len(obj_cardgame.player1.player_Deckofcards) == 10)
        self.assertTrue(len(obj_cardgame.player2.player_Deckofcards) == 10)

    def test_getwinner(self):
        # when player 1's len deck of cards < player 2's len deck of cards
        self.obj_cardgame.player2.player_Deckofcards = [['card1'], ['card2'], ['card3'], ['card4']]
        self.obj_cardgame.player1.player_Deckofcards = [['card1'], ['card2']]
        self.assertEqual(self.obj_cardgame.getwinner(), self.obj_cardgame.player2)
        # when player 1's len deck of cards > player 2's len deck of cards
        self.obj_cardgame.player1.player_Deckofcards = [['card1'], ['card2'], ['card3'], ['card4']]
        self.obj_cardgame.player2.player_Deckofcards = [['card1'], ['card2']]
        self.assertEqual(self.obj_cardgame.getwinner(), self.obj_cardgame.player1)
        # when player 1's len deck of cards = player 2's len deck of cards
        self.obj_cardgame.player1.player_Deckofcards = [['card1'], ['card2']]
        self.obj_cardgame.player2.player_Deckofcards = [['card1'], ['card2']]
        self.assertEqual(self.obj_cardgame.getwinner(), None)
