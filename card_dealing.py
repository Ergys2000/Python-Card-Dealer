import numpy as np
import pandas as pd
import re

class Mass_Card_Dealer:

    def __init__(self, dealings):
        """ This class simulates multiple card dealings and with its methods you can get statistics on these card dealings"""
        self.dealings = dealings
        self.decks = [] 
        colors = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        for i in range(self.dealings):
            for j in range(13):
                for k in range(4):
                    self.decks.append(str(j+1)+' of '+colors[k])
        
                
        self.decks = np.array(self.decks).reshape((dealings, 52))

        for deck in self.decks:
            for i in range(52):
                index = np.random.randint(52)
                deck[i], deck[index] = deck[index], deck[i]
        self.decks = self.decks.reshape((dealings, 4, 13))
    

    def n_who_have(self, card, frequency):
        n = 0
        for deck in self.decks:
            for person in deck:
                sum=0
                for c in person:
                    card_nr = re.findall('\d+', c)
                    nr = int(card_nr[0])
                    if nr == card:
                        sum +=1
                if sum >= frequency:
                    n+=1
        return n


    def n_who_have_straight(self, start, end):
        n = 0
        for deck in self.decks:
            for person in deck:
                cards_met = []
                for card in person:
                    card_nr = re.findall('\d+', card)
                    nr = int(card_nr[0])
                    if nr not in cards_met:
                        if (nr >= start) and (nr <= end):
                            cards_met.append(nr)
                if len(cards_met) == (end-start+1):
                    n += 1
        return n

    def make_dataframe(self):
        cards_table =  self.decks.reshape(4*self.dealings, 13) # this is the card table that contains the cards of 4 * dealings people

        index = ["Card " + str(i+1) for i in range(13)]

        # the next line creates the outer column names in the hierarchical columns
        outer = ["Dealing : "+str(i+1) for i in range(self.dealings) for j in range(4)]
        # this creates the inner column names
        inner = ["Person : "+str(j+1) for i in range(self.dealings) for j in range(4)] 

        columns = [outer, inner]
        self.frame = pd.DataFrame(cards_table.T, index=index, columns=columns) # we passed the transpose because we want to 
                                                                               # have the cards as the indexes

