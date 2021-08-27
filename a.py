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
       for i in range(len(self.cards)-1,0,-1) :
          r = random.randint(0,1)  
          self.cards[i] , self.cards[r] = self.cards[r] , self.cards[i]

   def drawCard(elf):
       return self.cards.pop()               

class player(object):
     def __init__(self , name):
         self.name = name
         self.hand = []

     def draw(self,deck):
         self.hand.append(Deck.drawCard()) 
         return self 

     def showHand(self):
         for card in self.hand:
             card.show()    
             

# card = Card("Club" , 6)
# card.show()

deck = Deck()
print(deck)
deck.show()

# player starts to play as bob!

bob = player("Bob")
bob.draw(deck).draw(deck)
bob.showHand()

card = deck.draw()
card.show()