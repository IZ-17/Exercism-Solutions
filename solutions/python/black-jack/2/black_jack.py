ace_card = ["A"]
face_cards = ["K","Q","J"]
def value_of_card(card):
    if card in face_cards:
        return 10
    elif card in ace_card:
        return 1
    return int(card)

def higher_card(card_one, card_two):
    value_1 = value_of_card(card_one)
    value_2 = value_of_card(card_two)
    if value_1 == value_2:
        return card_one, card_two
    elif value_1 > value_2:
        return card_one
    return card_two
    
def value_of_ace(card_one, card_two):
    value_1 = 11 if card_one in ace_card else value_of_card(card_one)
    value_2 = 11 if card_two in ace_card else value_of_card(card_two)
    if value_1 + value_2 > 10:
        return 1
    return 11

def is_blackjack(card_one, card_two):
    value_1 = 11 if card_one in ace_card else value_of_card(card_one)
    value_2 = 11 if card_two in ace_card else value_of_card(card_two)
    if value_1 + value_2 == 21:
        return True
    return False

def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    value_1 = value_of_card(card_one)
    value_2 = value_of_card(card_two)
    if 9 <= value_1 + value_2 <=11:
        return True
    return False