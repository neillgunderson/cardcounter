import random
import time
from cards import spade_dict, heart_dict, club_dict, diamond_dict

# Merge all the dictionaries into one
card_dict = {**spade_dict, **heart_dict, **club_dict, **diamond_dict}

# Create a card value dictionary
card_values = {f"{rank} of {suit}": value for suit in ['Spades', 'Hearts', 'Clubs', 'Diamonds'] 
                                         for rank, value in zip(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'], 
                                                                [1, 1, 1, 1, 1, 0, 0, 0, -1, -1, -1, -1, -1])}

cards = list(card_dict.keys())
random.shuffle(cards)

# Ask the user if they want to enter into simulation mode
simulation_mode = input("Do you want to enter into simulation mode? (y/n) ")

if simulation_mode.lower() == "y":
    num_cards = len(cards)
else:
    # Ask the user how many cards they want to see
    num_cards = int(input("How many cards do you want to see? "))
    if num_cards > len(cards):
        print(f"Maximum available cards is {len(cards)}. Using that.")
        num_cards = len(cards)

# Ask the user if they want a time limit
time_limit = input("Do you want a time limit? (y/n) ")
if time_limit.lower() == "y":
    delay = int(input("Enter the time limit in seconds: "))
else:
    delay = None

counter = 0
for i in range(num_cards):
    card = cards[i]
    print(card_dict[card])
    counter += card_values[card]
    # If more than one card is to be shown, wait for user to press enter or delay for the set time
    if i < num_cards - 1:  # Prevent asking for Enter when there's no card left
        if delay is not None:
            print(f"Next card in {delay} seconds...")
            time.sleep(delay)
        else:
            input("Press Enter to reveal the next card...")

print("Please enter the total count value:")
user_input = int(input())

if user_input == counter:
    print("Correct!")
else:
    print(f"Wrong! The correct count value is {counter}")
