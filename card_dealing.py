import numpy as np
import pandas as pd

class Mass_Card_Dealer:

    def __init__(self, dealings):
        """ This class simulates multiple card dealings and with its methods you can get statistics on these card dealings"""
        self.dealings = dealings
        self.decks = [] 
        colors = ['H', 'S', 'C', 'D']
        for i in range(self.dealings):
            for j in range(13):
                for k in range(4):
                    self.decks.append(str(j)+colors[k])
        
                
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
                sum = 0
                for c in person:
                    if int(c[0]) == card:
                        n+=1
                if n >= frequency:
                    n+=1
        return n


    def n_who_have_straight(self, start, end):
        n = 0
        for deck in self.decks:
            for person in deck:
                cards_met = []
                for card in person:
                    if card not in cards_met:
                        if (card >= start) and (card <= end):
                            cards_met.append(card)
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


class Card_Simulator:


    def __init__(self):

        colors = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        cards = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        deck = {'Cards':[],'Colors':[]} 
        for i in range(13):
            for j in range(4):
                deck['Cards'].append(cards[i])
                deck['Colors'].append(colors[j])
                
        index = [['Person '+str(i) for i in range(4) for j in range(13)],
                 [j for i in range(4) for j in range(13)]]

        self.df = pd.DataFrame(deck, index=index)
        for i in range(52):
            index = np.random.randint(52)
            card_hold = self.df.iloc[i].copy()
            self.df.iloc[i] = self.df.iloc[index]
            self.df.iloc[index] = card_hold

    def n_who_have(self, card, frequency):
        n=0
        for i in range(4):
            row_name = 'Person '+str(i)
            person = self.df.loc[row_name]
            nr_cards = (person.Cards == card).sum()
            if nr_cards >= frequency:
                n+=1
        return n;
x = Mass_Card_Dealer(2)
x.make_dataframe()
print(x.frame)
