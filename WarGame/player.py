from random import *
from WarGame.deckofcard import DeckOfCard
from WarGame.card import Card


class Player:
    def __init__(self, name, num_of_cards=26):
        if type(name) != str or type(num_of_cards) != int:
            raise TypeError("name must be str and num of cards must be int")
        self.name = name
        self.player_Deckofcards = []
        self.num_of_cards = num_of_cards
        if 10 > self.num_of_cards or self.num_of_cards > 26:
            self.num_of_cards = 26

    def set_hand(self, card_list: DeckOfCard):
        if type(card_list) != DeckOfCard:
            raise TypeError("card list's type must be DeckOfCard")
        for i in range(self.num_of_cards):
            self.player_Deckofcards.append(card_list.deal_one())

    def get_card(self):
        e = choice(self.player_Deckofcards)
        self.player_Deckofcards.remove(e)
        return e

    def add_card(self, card1):
        if card1[1] not in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']:
            raise TypeError("card must be like card")
        if card1[0] not in ['Diamond', 'Spade', 'Heart', 'Club']:
            raise TypeError("card must be like card")
        self.player_Deckofcards.append(card1)

# player = Player('bob')
# cards = DeckOfCard()
# player.set_hand(cards)
# print(player.player_Deckofcards)
# print(player.get_card())
# # print(player.add_card(cards))
