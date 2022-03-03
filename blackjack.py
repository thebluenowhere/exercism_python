"""Functions to help play and score a game of blackjack."""
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
        
def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.
    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    is_blackjack = True
    if card_one + card_two != 21:
        is_blackjack = False
    if (card_one == 'A' or card_two == 'A') and not (card_one == 'A' and card_two == 'A'):
        is_blackjack = True
    return is_blackjack

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    C1 = value_of_card(card_one)
    C2 = value_of_card(card_two)    
    can_split = True
    if C1 != C2:
        can_split = False
    return can_split

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.
    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    C1 = value_of_card(card_one)
    C2 = value_of_card(card_two)
    if ((C1 + C2) <= 11) and not (card_one == 'A' and card_two == 'A'):
        return True
    else:
        return False
