import random

deck = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']*4

class Player:

    def __init__(self, name, balance=1000):
        self.name = name
        self.balance = balance

    def __repr__(self):
        print('{name} has {money}'.format(name=self.name, money = self.balance))

   
class Hand:

    def deal():
        deck = []
        for card in range(2):
            random.shuffle(deck)
            card = deck.pop()
            deck.append(card)
        return deck

    def value(hand):
        value = 0
        for card in hand:
            if 'JKQ' in card:
                value += 10
            elif 'A' in card:
                if value + 11 > 21:
                    value += 1
                else:
                    value += 11
            else:
                value += card
        return value
            

class Blackjack:

    def __init__(self, name='blackjack', won=0, lost=0):
        self.won = won
        self.lost = lost

    def __repr__(self):
        print('£{won} has been lost and £{lost} has been lost'.format(self.won, self.lost))




