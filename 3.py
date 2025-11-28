suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

sample_space_cards = [(rank, suit) for rank in ranks for suit in suits]

def calculate_probability(event, sample_space):
    return len(event) / len(sample_space)

event_heart = [card for card in sample_space_cards if card[1] == "Hearts"]
prob_heart = calculate_probability(event_heart, sample_space_cards)
print(f"Probability of drawing a Heart: {prob_heart:.2f}")

event_ace = [card for card in sample_space_cards if card[0] == "A"]
prob_ace = calculate_probability(event_ace, sample_space_cards)
print(f"Probability of drawing an Ace: {prob_ace:.2f}")

event_red = [card for card in sample_space_cards if card[1] in ["Hearts", "Diamonds"]]
prob_red = calculate_probability(event_red, sample_space_cards)
print(f"Probability of drawing a Red card: {prob_red:.2f}")
