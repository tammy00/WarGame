from unittest import TestCase
from WarGame.card import Card


class TestCard(TestCase):

    def SetUp(self):
        self.obj_card = Card('Diamond', 5)

    def test__init__(self):
        # when value is 'Jack'\ 'Queen'\ 'King'\ 'Ace' (extreme values)
        obj_card = Card('Diamond', 'Ace')
        self.assertEqual(obj_card.value, 14)
        obj_card = Card('Diamond', 'Jack')
        self.assertEqual(obj_card.value, 11)
        # when value is between 2 and 10
        obj_card = Card('Diamond', 3)
        self.assertEqual(obj_card.value, 3)
        # when suit is one of the following:['Diamond', 'Spade', 'Heart', 'Club']
        obj_card = Card('Diamond', 'Ace')
        self.assertEqual(obj_card.suit, 1)
        obj_card = Card('Club', 'Ace')
        self.assertEqual(obj_card.suit, 4)

    def test__init__invalid(self):
        # when value isn't one of the following:[2-10, 'Jack', 'Queen', 'King', 'Ace']
        with self.assertRaises(IndexError):
            obj_card = Card('Diamond', -5)
        with self.assertRaises(IndexError):
            obj_card = Card('Diamond', 11)
        with self.assertRaises(IndexError):
            obj_card = Card('Diamond', 'Princess')
        with self.assertRaises(IndexError):
            obj_card = Card('Star', 7)

    def test__gt__(self):
        # when self.suit = other.suit & when self.value < other.value
        obj_card1 = Card('Diamond', 10)
        obj_card2 = Card('Diamond', 'Ace')
        self.assertFalse(obj_card1 > obj_card2)
        # when self.suit = other.suit & self.value = other.value
        obj_card1 = Card('Diamond', 10)
        obj_card2 = Card('Diamond', 10)
        self.assertFalse(obj_card1 > obj_card2)
        # when self.suit = other.suit & self.value > other.value
        obj_card1 = Card('Diamond', 10)
        obj_card2 = Card('Diamond', 6)
        self.assertTrue(obj_card1 > obj_card2)
        # _____________________________________________________________________
        # when self.suit > other.suit & when self.value < other.value
        obj_card1 = Card('Club', 10)
        obj_card2 = Card('Diamond', 'Ace')
        self.assertTrue(obj_card1 > obj_card2)
        # when self.suit > other.suit & self.value = other.value
        obj_card1 = Card('Club', 10)
        obj_card2 = Card('Diamond', 10)
        self.assertTrue(obj_card1 > obj_card2)
        # when self.suit > other.suit & self.value > other.value
        obj_card1 = Card('Club', 10)
        obj_card2 = Card('Diamond', 6)
        self.assertTrue(obj_card1 > obj_card2)
        # _____________________________________________________________________
        # when self.suit < other.suit & when self.value < other.value
        obj_card1 = Card('Diamond', 10)
        obj_card2 = Card('Club', 'Ace')
        self.assertFalse(obj_card1 > obj_card2)
        # when self.suit < other.suit & self.value = other.value
        obj_card1 = Card('Diamond', 10)
        obj_card2 = Card('Club', 10)
        self.assertFalse(obj_card1 > obj_card2)
        # when self.suit < other.suit & self.value > other.value
        obj_card1 = Card('Diamond', 10)
        obj_card2 = Card('Club', 6)
        self.assertFalse(obj_card1 > obj_card2)

