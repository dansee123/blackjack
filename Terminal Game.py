import random

deck = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']*4

class Player:

    def __init__(self, name, balance=1000):
        self.name = name
        self.balance = balance
        self.hand = []
        self.value = 0
        self.playing = True
        self.hitting = True

    def __repr__(self):
        return '{name} has the cards {cards} with a value of {value}'.format(name=self.name, cards=self.hand, value=self.value)

    def balance_check(self):
        return 'You have a balance of {}'.format(self.balance)

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
            elif 'J' in card:
                self.value += 10
            elif 'K' in card:
                self.value += 10
            elif 'Q' in card:
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
            if int(wager) > self.balance:
                print('You cannot bet that much! Please try again...')
            else:
                looping = False
        return wager

    def hit_or_stand(self):
        looping = True
        while looping == True:
            hit_or_stand = input('Would you like to hit or stand? Enter H for hit or S for stand: ')
            if hit_or_stand.upper() == 'H':
                self.hitting = True
                looping = False
            elif hit_or_stand.upper() == 'S':
                looping = False
                self.hitting = False
            else:
                print('Invalid input. Please try again...')
        return self.hitting

    def card_to_add(self):
        if self.hitting == True:
            random.shuffle(deck)
            card_to_add = deck.pop()
            self.hand.append(card_to_add)


    def win(self, wager):
        if self.value == 21:
            win = int(wager) * 2
            print('You got a blackjack! You won £{}'.format(win))
        else:
            win = int(wager) * 1.5
            print('Congratulations, you won £{}'.format(win))

        self.balance += win - int(wager)
        return self.balance

    def lose(self, wager):
        print('The house wins')
        print('Unlucky, you lost {}'.format(wager))
        self.balance -= int(wager)
        return self.balance
              
class Dealer:

    def __init__(self):
        self.hand = []
        self.value = 0
        self.hitting = True

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
            elif 'J' in card:
                self.value += 10
            elif 'K' in card:
                self.value += 10
            elif 'Q' in card:
                self.value += 10
            elif 'A' in card:
                if self.value + 11 > 21:
                    self.value += 1
                else:
                    self.value += 11     
        return self.value
    
    def hit_or_stand(self):
        if self.value <= 17:
            self.hitting = True
        else:
            self.hitting = False
            print('The dealer stands')
        return self.hitting

    def card_to_add(self):
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
        player = Player(input('Please enter your name: '))
        while play == True:
            dealer = Dealer()
            wager = Player.place_wager(player)
            player_hand = Player.player_hand(player)
            dealer_hand = Dealer.dealer_hand(dealer)
            player_value = Player.player_value(player)
            dealer_value = Dealer.dealer_value(dealer)

            print(repr(player))
            print(repr(dealer))

            player_hitting = True
            while player_hitting == True:
                    player_hitting = Player.hit_or_stand(player)
                    player.card_to_add()
                    player.player_value()
                    print(repr(player))
                    if player_value >= 21:
                        player_hitting = False
                        dealer_hitting = False

            dealer_hitting = True
            while dealer_hitting == True:
                dealer_hitting = Dealer.hit_or_stand(dealer)
                dealer.card_to_add()
                dealer.dealer_value()
                print(repr(dealer))
                if dealer_value >= 21:
                    dealer_hitting = False
                

            if player_value <= 21 and dealer_value > 21:
                Player.win(player,wager)
                another_round = False
            elif player_value > 21 and dealer_value <= 21:
                Player.lose(player,wager)
                another_round = False
            elif player_value > dealer_value and player_value <= 21:
                Player.win(player,wager)
                another_round = False
            elif player_value < 21 and player_value < dealer_value:
                Player.lose(player,wager)
                another_round = False
            elif player_value == dealer_value:
                print ('Push')

            print(Player.balance_check(player))
            play = Player.keep_playing(player)

black_jack = Blackjack()
black_jack.play()











