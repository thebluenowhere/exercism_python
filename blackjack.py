"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    # cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
    # Assign value 10 to face cards
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    # Assign value 1 to aces
    elif card == 'A':
        return 1
    # Return integer of numbered cards
    else: 
        return int(card)
        
def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    C1 = value_of_card(card_one)
    C2 = value_of_card(card_two)
    if C1 > C2:
        return card_one
    elif C1 < C2:
        return card_two
    else:
        return (card_one), (card_two)



def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.
    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.
        :return: int - value of the upcoming ace card (either 1 or 11).
    """
    ace_value = 0
    C1 = value_of_card(card_one)
    C2 = value_of_card(card_two)    
    if (C1 + C2 >= 11) or (card_one == 'A' or card_two == 'A'):
        ace_value = 1    
    else:
        ace_value = 11
    return ace_value
