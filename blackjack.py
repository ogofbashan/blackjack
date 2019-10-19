import random
from cardplayers import PlayingCards
from cardplayers import CardPlayers

shoe = PlayingCards()
dealer = CardPlayers("dealer", 1, hand = [])
#player_1 = CardPlayers(input('name? '), 0, hand = [], pot = int(input("How much money you want? ")))
player_1 = CardPlayers('player', 0, hand = [], pot = 10)



class BlackJack():
    def __init__(self, playing):
        self.playing = playing

    def play(self):
        self.showRules()
        return self.question()
    def showRules(self):
        return print('''Rule Number 4: There is no rule number 4''')
    def question (self):
        option = input("Would you like to play? [y/n] ").strip().lower()
        if option == 'n' or option == 'no' or option == 'exit' or option == 'x':
            return self.playing == False
        elif option == 'y':
            self.deal()
        else:
            print("Error #1")

    def deal(self):
        print(f'How much money you have: {player_1.pot}')
        player_1.betMoney(int(input("how much? ")))

        shoe.startDeckBuilder()
        player_1.getCard(shoe.deck)
        dealer.getCard(shoe.deck)
        player_1.getCard(shoe.deck)
        dealer.getCard(shoe.deck)
        dealer.getCount()
        player_1.getCount()
        self.showHand(player_1.hand)
        self.blackjackCheck(player_1.card_value, dealer.card_value)
        self.nextMove()

    def blackjackCheck(self, player_num, dealer_num):
        if player_num == 21:
            print("BlackJack")
            player_1.pot += (player_1.bet*1.5)
            self.endgame()
        else:
            if dealer_num == 21:
                print("BlackJack")
                player_1.pot -= player_1.bet
                self.endgame()
            else:
                pass
    def bustCheck(self, num):
        if num > 21:
            print("Loser")
            player_1.pot -= player_1.bet
            self.endgame()
        else:
            pass

    def nextMove(self):
        option = input("Hit or Stay? ")
        card = PlayingCards()

        if option == 'stay':
            return self.dealerMoves(dealer)
        if option == 'hit':
            player_1.getCard(shoe.deck)
            player_1.getCount()
            self.bustCheck(player_1.card_value)
            self.showHand(player_1.hand)
            return self.nextMove()
        if option == 'split':
            print("TODO")
        if option == 'double down':
            player_1.bet = (player_1.bet*2)
            player_1.getCard(shoe.deck)
            player_1.getCount()
            self.showHand(player_1.hand)
            self.bustCheck(player_1.card_value)
            return self.dealerMoves(dealer)
        else:
            print('Error. Try Again')
            return self.nextMove()


    def dealerMoves(self,dealer):
        dealer.getCount()
        print(f'Dealer\'s Hand: {dealer.hand}  value: {dealer.card_value}')


        if dealer.card_value < 17:
            dealer.getCard(shoe.deck)
            dealer.getCount()
            print(f'Dealer\'s Hand: {dealer.hand}  value: {dealer.card_value}')
            self.dealerMoves(dealer)
        elif dealer.card_value > 21:
            print("The Dealer has Busted")
            player_1.pot += player_1.bet
            self.endgame()
        else:
            self.finalcheck(player_1.card_value, dealer.card_value)
    def finalcheck(self, num1, num2):
        if num1>num2:
            print("Player Wins!")
            player_1.pot += player_1.bet
            self.endgame()
        elif num2>num1:
            print("Dealer Wins!")
            player_1.pot -= player_1.bet
            self.endgame()
        elif num1==num2:
            print("Push")
            self.endgame()
    def endgame(self):
        player_1.turnInCards()
        dealer.turnInCards()
        self.play()

    def showHand(self, hand):
        print(f'\n\nDealer\'s Hand: {dealer.hand[1]} seen value: {dealer.hand[1][:-1]}\n\n')

        for i in range(len(hand)):
            print(f'''+-----+
|{hand[i]}   |
|     |
|   {hand[i]}|
+-----+''')

        print(f'Player\'s Hand: {player_1.hand} current value: {player_1.card_value}\n')




blackjack = BlackJack(playing = True)

if blackjack.playing == True:
    blackjack.play()
