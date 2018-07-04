#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 22:54:12 2018

@author: letcosta
"""
"""
For this assignment we are going to (also) create a poker game. The game needs to do the following:

Needs to be written on a file named poker_game.py
The game can be played by running python poker_game.py NUMBER_OF_PLAYERS
The script accepts an argument number_of_players which is a number indicating the number of players.
For each player the script will ask the name (using input() function).
The script will deal 5 cards to each player (you can use random.choice to select at random from a list). The different cards, sorted from lowest to highest are 2,3,4,5,6,7,8,9,10,J,Q,K,A. There are four suits, clubs, spades, hearts, diamonds.
The script will print out each one of the players' hand, find out which one of the players have a winning hand and will print out the name of the winner
For the winning rules, there are two possible implementations:
Easy version, where we just compare the hands and the hand with the highest cards wins. For example, if Player 1 has the hand 2,3,K,Q,7 and Player 2 has the hand 8,10, ACE,J,2 Player 2 would win because 1 ACE beats a K. If Player 1 has the hand 2,3,K,Q,7, and Player 2 has the hand J,J,K,7,3 then Player 1 would win (since K,Q beats K,J).
Hard version, where we implement the different poker hands taking the suits into account (flush, poker, straight, etc).
hint: You can use the __gt__ , __lt__ or __eq__ methods on a class to implement comparisons (greater than, less than).

Finally, we will create a repository on github called poker_game, upload the poker_game.py file and a README.md file explaining what the game does. Then we will link the repository on the blog post.
""" 
"""
The two basic requirements of this game are a deck of cards and a dealer. 
In this first section, I've created two lists in which the ranks of the cards are stablished. 
The list ranks lays out the cards being used from the deck and ranges from 2 to 11, the last card representing 'As' This will be better explained on the article further on as the transformation takes place later on on the code. 

"""
ranks=[i for i in range(2,11)]+['JACK', 'QUEEN', 'KING', 'ACE']
suits=['SPADE', 'HEART', 'DIAMOND', 'CLUB']

def get_deck(): 
    return[[rank, suit] for rank in ranks for suit in suits]

"""
Here I've used a list comprehension, which a concise way of creating a list.
This will return a result list.
Now we will create a function which will get a deck of cards and randomly shuffle them.

""" 
deck = get_deck()
random.shuffle(deck)

"""
Now that we have constructed the deck of cards as a list comprehendsion, we msut also create the code for shuffling the cards. 
This is done through the random library module. We use the function shuffle and insert the deck of cards in it.
Now we must create a dummy or boolean variable in which the player 'i' is in the game. The rest of the code will keep the game going (it's the code for dealing with the hand).
""" 
player i in = True

player i hand = [deck.pop(), deck.pop()]
dealer i hand = [deck.pop(), deck.pop()]

ranks = [i for i in range(2,11)]+['JACK', 'QUEEN', 'KING', 'ACE']
suits=['SPADE', 'HEART', 'DIAMOND', 'CLUB']
def get_deck() 
shuffle(deck)
player i hand = [deck.pop(), deck.pop()]

"""
In the following code, I'll take the prrevious list in which I lay out the values of the cards and I will modify them through a helper function.
What this helper function essentially does is it makes a particular functionality happen in multiple places.
For example, oin this case, I want the number 11 to represent the card 'As''
This function will also make the code more readable.
""" 

def card_value(card):
    rank=card[0]
    if rank in ranks [0:-4]:
        return int(rank)
    elif ranks is 'ACE':
        return 11
    else:
        return 10

def hand_value(hand):
    
tmp_value=sum(card i value(i)for i in hand)
num_aces=len([i for i in hand if i[0] is 'ACE'])

"""
By adding up the cards, we can check that it adds up to a maximum of 21. 
This shows that aces can count for 1 or 11.

""" 
while num_aces>0:
    if tmp_value>21 and 'ACE in ranks:
        tmp_value -= 10
        num_aces -= 1
    else:
        break
    if tmp_value<21:
        return[str(tmp_value), tmp_value]
    elif tmp_value ==21:
        return['Blackjack!', 21]:
            else: 
                return['Bust!, 100]
                

"""
This next part of the code will display if the player stays or hits and if the hand is a bust or not. 
If the hand is not a bust, the player may keep going, in which case the player must change to the dealer so that the game will keep going.

"""
while player_in: 
    current_score_str="'\nYou are currently at %s\nwith the hand%s\n"''
print current_score_str%(hand_value(player_hand)[0],player_hand)
if hand_value(player_hand)[1] == 100:
    break

"""
Through this code, we can display the player's current hand and its value.
In this case, the code will determine if the hand is a bust and will end the game for the player as it will not give it a choice of how to proceed about the game.
"""
if player_in:
    response=int(raw_input('Hit or stay? (Hit=1, Stay=0)'))
    if response:
    player_in=True
    new_player_card=deck.pop()
    player_hand.append(new_player_card)
    print 'You draw %s' % new_player_card 
else:
    player_in=False
    

"""
Now we will create a code which will calculate the score of the dealer and the player.
"""
player_score_label, player_score = hand_value(player_hand)
dealer_score_label, dealer_score = hand_value(dealer_hand) 

if player_score<= 21:
    dealer_hand_string = ”’\nDealer is at %s\nwith the hand %s\n”’
    print dealer_hand_string % (dealer_score_label, dealer_hand)
else:
    print "Dealer wins.""

while hand_value(dealer_hand[1])<17:
dealer_hand.append(new_dealer_card)
print ‘Dealer draws %s’ % new_dealer_card
    

"""
The last thing to be done in this game is to check the final score of the player and the dealer.
"""
dealer_score_label, dealer_score = hand_value(dealer_hand)

if player_score < 100 and dealer_score == 100:
print ‘You beat the dealer!’
elif player_score > dealer_score:
print ‘You beat the dealer!’
elif player_score == dealer_score:
print ‘You tied the dealer, nobody wins.’
elif player_score < dealer_score:
print “Dealer wins!”


"""
Done!
"""

