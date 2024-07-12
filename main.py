# This is a termial game simulation of Blackjack
# Goal is to get a hand worth 21 points. Standard 52 card deck, 4 suits.
# 1-6 players. Play multiple games and keep track of pot.
# Face cards worth 10, ace worth 1 or 11, number cards == number value

"""To do list: 1. need if name == __main__ at top, or def main() and call it at bottom,
 2. add docstrings, 3. fill out functions, 4. upload to Github."""

import random

# player class attrib: self, name, hand, hand_value, bet, pot


class Player:
    def __init__(self, name):
        self.name = name
        self.hand_value = 0
        self.bet = 0
        self.pot = 0
        self.hand = []

    def get_hand(self):
        return self.hand

    def get_hand_value(self):
        return self.hand_value

    def get_bet(self):
        return self.bet

    def get_pot(self):
        return self.pot


# dealer class attrib: self, deck size, pot
class Dealer:
    def __init__(self):
        self.pot = 0
        self.deck = []
        self.deck_size = 52

    def get_pot(self):
        return self.pot

    def get_deck_size(self):
        return self.deck_size

# play game is main(), play round is per round

# play_round() asks for user input, calls hit(), stand(), double_down(), split(), surrender(), whilst score < 21
# if score > 21 after draw, you lose


def play_round(player):
    while self.hand_value <= 21:
        player_choice = input(
            "Would you like to: a) hit, b) stand, c) double down, d) split or e) surrender?")
        if player_choice == "a":
            hit()
        elif player_choice == "b":
            stand()
        elif player_choice == "c":
            double_down()
        elif player_choice == "d":
            split()
        elif player_choice == "e":
            surrender()

    # below is: deal(), hit(), stand(), double_down(), split(), surrender(), a deal function, or method of dealer class

    # deal() function deals cards to players and reduces decksize by 1

    # hit() function draws a card, add in ace if clause to each (11 or 1)

    # stand() function keeps score and end's players turns until other player is done

    # double_down, doubles bet and draws one card then ends player's turns

    # split() more complicated

    # surrender() player ends game for them and loses half their bet
