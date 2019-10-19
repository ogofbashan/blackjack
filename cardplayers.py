import random
from deck import PlayingCards

class CardPlayers():
    def __init__(self, name, turn, hand, pot = 0):
        self.name = name
        self.hand = hand
        self.turn = turn
        self.pot = pot
    def getCard(self, deck):
        new_card = deck.pop(random.randint(0,len(deck)))
        self.addtoHand(new_card)
    def addtoHand(self,new_card):
        self.hand.append(new_card)
    def getCount(self):
        card_value = 0
        self.card_value = card_value
        for card in self.hand:
            if card[-2] == 'K' or card[-2] == 'Q' or card[-2] == 'J' or card[-2] == '0':
                self.card_value+=10
            elif card[-2] == '9' or card[-2] == '8' or card[-2] == '7' or card[-2] == '6' or card[-2] == '5' or card[-2] == '4' or card[-2] == '3' or card[-2] == '2':
                self.card_value += int(card[-2])
            else:
                if card [-2] == 'A' and self.card_value <= 10:
                    self.card_value +=11
                elif card [-2] == 'A' and self.card_value > 10:
                    self.card_value +=1
    def split(self, deck):
        l_card = deck.pop(random.randint(0,len(deck)))
        r_card = deck.pop(random.randint(0,len(deck)))

        self.hand[0], self.hand[1] = [self.hand[0], l_card], [self.hand[1], r_card]
    def anotherSplit(self,deck, i):
        l_card = deck.pop(random.randint(0,len(deck)))
        r_card = deck.pop(random.randint(0,len(deck)))
        self.hand.insert(i, [self.hand[i][0], l_card])
        self.hand.insert(i+1, [self.hand[i][1], r_card])
        self.hand.pop(i+2)
    def turnInCards(self):
        self.hand = []
    def betMoney(self, bet):
        if bet % 2 == 0:
            self.bet = bet
        else:
            print("You can only bet even Values")
            self.betMoney(int(input("how much? ")))
