from WarGame.player import Player
from unittest import TestCase, mock
from WarGame.deckofcard import DeckOfCard


class TestPlayer(TestCase):

    def setUp(self):
        self.obj_player = Player('moshe', 26)

    def test__init__invalid(self):
        # type number of cards isn't int
        with self.assertRaises(TypeError):
            obj_player = Player('moshe', '26')
        # type name isn't str
        with self.assertRaises(TypeError):
            obj_player = Player(11, 26)

    def test__init__valid(self):
        # num of cards = NULL
        obj_player = Player('moshe')
        self.assertEqual(obj_player.num_of_cards, 26)
        # num of cards < 10
        obj_player = Player('moshe', 9)
        self.assertEqual(obj_player.num_of_cards, 26)
        # num of cards > 26
        obj_player = Player('moshe', 30)
        self.assertEqual(obj_player.num_of_cards, 26)
        # is list = []
        obj_player = Player('moshe', 26)
        self.assertEqual(obj_player.player_Deckofcards, [])

    def test_set_hand_invalid(self):
        # invalid- card list's type isn't DeckOfCard
        with self.assertRaises(TypeError):
            self.obj_player.set_hand(23)

    @mock.patch('WarGame.deckofcard.DeckOfCard.deal_one', return_value=['card'])
    def test_set_hand(self, moked_del):
        # adding cards to player_Deckofcards
        obj_player = Player('moshe', 10)
        cards = DeckOfCard()
        obj_player.set_hand(cards)
        self.assertTrue(obj_player.player_Deckofcards.count(['card']) == 10)

    @mock.patch('WarGame.player.Player.get_card', return_value=['card2'])
    def test_get_card(self, moke_get):
        self.obj_player.player_Deckofcards = ['card1', 'card2', 'card3', 'card4', 'card5']
        removed_card = self.obj_player.get_card()
        print(removed_card)
        # does the method removes the card
        self.assertTrue(removed_card not in self.obj_player.player_Deckofcards)
        # does the method returns a card
        self.assertEqual(self.obj_player.get_card(), ['card2'])

    def test_add_card(self):
        # added card is like card
        with self.assertRaises(TypeError):
            self.obj_player.add_card('test')
        # the card is added
        obj_player = Player('moshe', 11)
        obj_player.player_Deckofcards = ['card1', 'card2', 'card3', 'card4', 'card5']
        obj_player.add_card(['Heart', 7])
        self.assertTrue(['Heart', 7] in obj_player.player_Deckofcards)

