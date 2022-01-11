from unittest import TestCase, mock
from WarGame.deckofcard import DeckOfCard


class TestDeckOfCard(TestCase):

    def setUp(self):
        self.obj_deck = DeckOfCard()

    def test__init__(self):
        # 4 suit with one of each value [2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King', 'Ace']
        # card structure is: ['suit','value']
        list_club = []
        list_heart = []
        list_diamond = []
        list_spade = []
        for i in self.obj_deck.cards:
            if i[0] == 'Heart':
                list_heart.append(i[1])
            if i[0] == 'Spade':
                list_spade.append(i[1])
            if i[0] == 'Diamond':
                list_diamond.append(i[1])
            if i[0] == 'Club':
                list_club.append(i[1])
        self.assertTrue(list_club == [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'])
        self.assertTrue(list_club == list_heart == list_spade == list_diamond)

    def test_cards_shuffle(self):
        self.obj_deck.cards = [['card1'], ['card2'], ['card3'], ['card4']]
        self.obj_deck.cards_shuffle()
        self.assertFalse(self.obj_deck.cards == [['card1'], ['card2'], ['card3'], ['card4']])

    def test_deal_one(self):
        self.obj_deck.cards = [['card1'], ['card2'], ['card3'], ['card4']]
        self.obj_deck.deal_one()
        self.assertTrue(len(self.obj_deck.cards) == 3)

