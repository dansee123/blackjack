import random

deck = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']*4

class Player:

    def __init__(self, name, balance=1000):
        self.name = name
        self.balance = balance
        self.hand = []
        self.value = 0
        self.playing = True

    def __repr__(self):
        return '{name} has the cards {cards} with a value of {value}'.format(name=self.name, cards=self.hand, value=self.value)

    def player_hand(self):
        for card in range(2):
            random.shuffle(deck)
            card = deck.pop()
            self.hand.append(card)
        return self.hand

    def player_value(self):
        self.value = 0
        for card in self.hand:
            if type(card) == int:
                self.value += card
            elif 'JKQ' in card:
                self.value += 10
            elif 'A' in card:
                if self.value + 11 > 21:
                    self.value += 1
                else:
                    self.value += 11       
        return self.value

    def keep_playing(self):
        looping = True
        while looping == True:
            playing = input('Would you like to keep playing? Enter Y or N: ')
            if playing.upper() == 'Y':
                self.playing = True
                looping = False
            elif playing.upper() == 'N':
                self.playing = False
                looping = False
            else:
                print('Invalid input. Please try again...')
        return self.playing

    def place_wager(self):
        looping = True
        while looping == True:
            wager = input('Please enter the amount that you would like to bet: ')
            if wager > self.balance:
                print('You cannot bet that much! Please try again...')
            elif type(wager) is not int:
                print('You must enter a integer value. Please try again...')
            else:
                looping = False
        return wager

    def hit_or_stand(self):
        looping = True
        while looping == True:
            hit_or_stand = input('Would you like to hit or stand? Enter H for hit or S for stand: ')
            if hit_or_stand.upper() == 'H':
                random.shuffle(deck)
                card_to_add = deck.pop()
                self.hand.append(card_to_add)
                looping = False
            elif hit_or_stand.upper == 'S':
                looping = False
            else:
                print('Invalid input. Please try again...')
        return self.hand
              
class Dealer:

    def __init__(self):
        self.hand = []
        self.value = 0

    def __repr__(self):
        return 'Dealer has the cards {cards} with a value of {value}'.format(cards=self.hand, value=self.value)

    def dealer_hand(self):
        for card in range(2):
            random.shuffle(deck)
            card = deck.pop()
            self.hand.append(card)
        return self.hand

    def dealer_value(self):
        self.value = 0
        for card in self.hand:
            if type(card) == int:
                self.value += card
            elif 'JKQ' in card:
                self.value += 10
            elif 'A' in card:
                if self.value + 11 > 21:
                    self.value += 1
                else:
                    self.value += 11       
        return self.value
    
    def hit(self):
        random.shuffle(deck)
        card_to_add = deck.pop()
        self.hand.append(card_to_add)
        return self.hand
            

class Blackjack:

    def __init__(self, name='blackjack', won=0, lost=0):
        self.won = won
        self.lost = lost

    def __repr__(self):
        print('£{won} has been lost and £{lost} has been lost'.format(self.won, self.lost))

    def play(self):
        
        play = True
        while play == True:
            player = Player(input('Please enter your name: '))
            dealer = Dealer()
            wager = Player.place_wager(player)
            player_hand = Player.player_hand(player)
            dealer_hand = Dealer.dealer_hand(dealer)
            player_value = Player.player_value(player)
            dealer_value = Dealer.dealer_value(dealer)

            print(repr(player))
            print(repr(dealer))








            play = Player.keep_playing(player)











