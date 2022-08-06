import dataclasses
import pygame
import random

@dataclasses.dataclass
class Card:
    suit: str
    rank: int
    value: int = 0



class Deck:
    shuffled_deck = []
    cards = []
    def __init__(self):
        self.build()
        self.shuffle()
        

    def build(self):
        for suit in ["Spades", "Hearts", "Diamonds", "Clubs"]:
            for rank in ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']:
                    self.cards.append(Card(suit, rank))
                
        for cards in self.cards:
            if cards.rank == 'Ace':
                cards.value = 11
            elif cards.rank == 'Jack' or cards.rank == 'Queen' or cards.rank == 'King':
                cards.value = 10
            else:
                cards.value = cards.rank


    def shuffle(self):
        random.shuffle(self.cards)
        self.shuffled_deck = self.cards
        

    def print_deck(self):
        for card in self.cards:
            print(f'{card.rank} of {card.suit} Worth: {card.value}')
        
    def print_shuffled_deck(self):
        
        for card in self.shuffled_deck:
            print(f'{card.rank} of {card.suit} Worth: {card.value}')
        

    
        


class Player():
    def __init__(self, name):
        self.hand = []
        self.score = 0
        self.name = name
        print(f'{self.name} has been created')

    def print_hand(self):
        print(f'''{self.name}'s hand is: ''')
        for card in self.hand:
            print(f'    {card.rank} of {card.suit}')
        #print the score
        self.add_score()
        print(f'''{self.name}'s score is: {self.score}''')
    
    def add_score(self):
        self.score = 0
        for card in self.hand:
            self.score += card.value
        return self.score
    def deal(self, deck):
        self.hand.append(deck.shuffled_deck.pop())
        print(f'{self.name} has been dealt a card')
        self.add_score()
        



if __name__ == "__main__":
    deck = Deck()
    deck.print_deck()
    player1 = Player('Player 1')
    dealer = Player('Dealer')
    player1.deal(deck)
    dealer.deal(deck)
    dealer.print_hand()
    player1.deal(deck)
    dealer.deal(deck)
    player1.print_hand()
    dealer.deal(deck)
    dealer.print_hand()
    dealer.deal(deck)
    dealer.print_hand()