import random
from cards import spade_dict, heart_dict, club_dict, diamond_dict

# Merge all the dictionaries into one
card_dict = {**spade_dict, **heart_dict, **club_dict, **diamond_dict}

# Create a card value dictionary
card_values = {f"{rank} of {suit}": value for suit in ['Spades', 'Hearts', 'Clubs', 'Diamonds'] 
                                         for rank, value in zip(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'], 
                                                                [1, 1, 1, 1, 1, 0, 0, 0, -1, -1, -1, -1, -1])}

cards = list(card_dict.keys())
random.shuffle(cards)

#The rules for card counting

print("\nHere are the rulles for card counting: \n\nValues 2-6 = +1 \nValues 7-9 = 0 \nValues 10, Jack, Queen, King and Ace = -1 \n\nKeep track of the total expected value and input it at the end. Good luck.")

# Ask the user how many cards they want to see
num_cards = int(input("\nHow many cards do you want to see? "))
if num_cards > len(cards):
    print(f"Maximum available cards is {len(cards)}. Using that.")
    num_cards = len(cards)

counter = 0
for i in range(num_cards):
    card = cards[i]
    print(card_dict[card])
    counter += card_values[card]
    # If more than one card is to be shown, wait for user to press enter
    if i < num_cards - 1:  # Prevent asking for Enter when there's no card left
        input("Press Enter to reveal the next card...")

print("Please enter the total count value:")
user_input = int(input())

if user_input == counter:
    print("Correct!")
else:
    print(f"Wrong! The correct count value is {counter}")
