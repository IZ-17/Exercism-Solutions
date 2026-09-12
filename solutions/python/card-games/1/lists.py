def get_rounds(number):
    return list(range(number, number + 3))

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    return (hand[0] + hand[-1]) / 2 == card_average(hand) or hand[len(hand) // 2] == card_average(hand)

def average_even_is_average_odd(hand):
    return sum(hand[::2]) / len(hand[::2]) == sum(hand[1::2]) / len(hand[1::2])
    
def maybe_double_last(hand):
    return hand if hand[-1] != 11 else hand[:-1] + [hand[-1] * 2]