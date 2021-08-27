from math import radians
import random


class Card(object):
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val
    
    def show(self):
        print "{} of {}".format(self.value , self.suit)     


class Deck(object):
   def __init__(self):
       self.cards = []
       self.build()

   def build(self):
       for s in ["Spades","Clubs","Diamonds","Hearts"]:
           for v in range(1,14):
               self.cards.append(Card(s,v))
               print "{} of {}".format(v,s)


   def show(self):
       for c in self.cards:
           c.show()   

   def shuffle(self):
       for i in range(len(self.cards)-1,0,-1) 
      rand = random.randint(0,1)          

# class player(object):
#     def __init__(self):
       


# card = Card("Club" , 6)
# card.show()

deck = Deck()
print(deck)
deck.show()