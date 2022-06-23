import random
import itertools

deck = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']*4

class Player:

    def __init__(self, name, balance=1000):
        self.name = name
        self.balance = balance

    def __repr__(self):
        print('{name} has {money}'.format(name=self.name, money = self.balance))


class Dealer:
    def __init__(self, name='House'):
        self.name = name

    
class Hand:
    def __innit__(self, ):
        pass

    def deal():
        deck = []
        for card in range(2):
            random.shuffle(deck)
            card = deck.pop()
            deck.append(card)
        return deck


class Blackjack:

    def __init__(self, name='blackjack', won=0, lost=0):
        self.won = won
        self.lost = lost

    def __repr__(self):
        print('£{won} has been lost and £{lost} has been lost'.format(self.won, self.lost))


