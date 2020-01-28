# Python-Card-Dealer
This little module allow for simulating large amounts of card dealings in an efficient manner, and analyzing those dealings.
## ----> How to use it?
Just download the card_dealing.py into your folder.
Import all the classes
##### from card_dealing import *
The you can create an instance like this
##### inst = Mass_Card_Dealer(1000) # where 1000 is the number of dealing you want to simulate
Then you can call methods on this instance like:
##### inst.n_who_have(2,2) # return the number of people who have two 2s
##### inst.n_who_have_straight(2, 8) # returns the number of people who have a straight starting from 2 and ending at 8
