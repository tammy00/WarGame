from WarGame.card import Card
from WarGame.cardgame import CardGame

name1 = input("enter players name: ")
name2 = input("enter players name: ")
obj_cardgame = CardGame(name1, name2)
print(f"{name1}'s cards:\n{obj_cardgame.player1.player_Deckofcards}")
print(f"{name2}'s cards:\n {obj_cardgame.player2.player_Deckofcards}")
for i in range(10):
    card_player1 = obj_cardgame.player1.get_card()
    card_player2 = obj_cardgame.player2.get_card()
    obj_card1 = Card(card_player1[0], card_player1[1])
    obj_card2 = Card(card_player2[0], card_player2[1])
    if obj_card2 > obj_card1:
        obj_cardgame.player2.add_card(card_player1)
        obj_cardgame.player2.add_card(card_player2)
        print(name2, 'is the winner in this round!')
    else:
        obj_cardgame.player1.add_card(card_player1)
        obj_cardgame.player1.add_card(card_player2)
        print(name1, 'is the winner in this round!')
    print('this round cards:', card_player1, 'v.s', card_player2)
a = obj_cardgame.getwinner()
if a is None:
    print(f"it's a tie\ntry again")
else:
    print(f"the winner is: {a.name.upper()} !!!\nwith total cards of ={len(a.player_Deckofcards)}")
