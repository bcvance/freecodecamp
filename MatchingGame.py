
from ast import Num
from cmath import sqrt
import random
from tkinter.tix import DisplayStyle
from numpy import choose

# these characters will be the symbols for the front of the cards
characters = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F", "G", "G", "H", "H"]
# this list of lists will hold the "cards". each list holds the card number and the face value of the card
num_characters = len(characters)
# this dictionary will hold the displays for each player
displays = {}
# this dictionary will hold all of the cards for each player
cards = {}

# this function creates a display list 
# this list will hold the actual values being displayed on the screen, whether that be the front or back of the card
# starts out as all numbers, since all cards are unflipped
def create_display():
    return [i for i in range(1, len(characters)+1)]

# this function creates a list of lists. each list within the list will hold a number (back of card) and 
# letter (front of card) combination. the letters will be appended in the randomize_cards function
def create_cards():
    return [[i] for i in range(1, len(characters)+1)]

# function for formatting and displaying the board
def print_board(displayed, playerkey):
    print(f"\n{playerkey}'s turn")
    print(" -----" + "------"*3)
    print("|     "*4, end="")
    print("|")
    print(f"|{f'{displayed[0]:^5}'}|{f'{displayed[1]:^5}'}|{f'{displayed[2]:^5}'}|{f'{displayed[3]:^5}'}|")
    print("|     "*4, end="")
    print("|")
    print(" -----" + "------"*3)
    print("|     "*4, end="")
    print("|")
    print(f"|{f'{displayed[4]:^5}'}|{f'{displayed[5]:^5}'}|{f'{displayed[6]:^5}'}|{f'{displayed[7]:^5}'}|")
    print("|     "*4, end="")
    print("|")
    print(" -----" + "------"*3)
    print("|     "*4, end="")
    print("|")
    print(f"|{f'{displayed[8]:^5}'}|{f'{displayed[9]:^5}'}|{f'{displayed[10]:^5}'}|{f'{displayed[11]:^5}'}|")
    print("|     "*4, end="")
    print("|")
    print(" -----" + "------"*3)
    print("|     "*4, end="")
    print("|")
    print(f"|{f'{displayed[12]:^5}'}|{f'{displayed[13]:^5}'}|{f'{displayed[14]:^5}'}|{f'{displayed[15]:^5}'}|")
    print("|     "*4, end="")
    print("|")
    print(" -----" + "------"*3)

# this function randomly chooses values from the characters list and appends a value to each index of the cards
# list of lists. this creates the "key-value pairs" for each card. maybe should use dictionary instead for cards?
def randomize_cards(playerkey):
    # creating list to delete values from as they are appended to cards lists so that cards are only used the correct
    # number of times
    elim_chars = characters[:]
    for i in range(num_characters):
        chosen = random.choice(elim_chars)
        cards[playerkey][i].append(chosen)
        elim_chars.remove(chosen)
    return cards[playerkey]

# prompts user for card number choice
def choose_card():
    card_number = input(f"Pick a card number from 1 to {num_characters}")
    card_number = int(card_number) - 1
    return card_number

# this card will "flip" a card if the move is valid. flipping means changing the value at that card's index from
# a number (back of card) to a letter (front of card) or vice-versa
def flip_up(card_number, playerkey):
    if is_valid_move(card_number, playerkey):
        displays[playerkey][card_number] = cards[playerkey][card_number][1]
    return displays[playerkey]

def flip_down(card1, card2, playerkey):
    displays[playerkey][card1] = cards[playerkey][card1][0]
    displays[playerkey][card2] = cards[playerkey][card2][0]

        
# this function checks that the user's card choice is not already flipped and that it is within the range of
# card numbers available
def is_valid_move(card_index, playerkey):
    if not isinstance(displays[playerkey][card_index], int):
        print("Please choose a card that has not been flipped.")
        return False
    elif not card_index in range(num_characters):
        print(f"Please pick a card number between 1 and {num_characters}")
    else:
        return True

# this function determines is the two cards chosen by the player are the same, returning True if they are, and False if they are not
def is_match(card1, card2, playerkey):
    if displays[playerkey][card1] == displays[playerkey][card2]:
        return True
    return False

# this function checks if there are any cards unturned. If not, it is game over (returns True). 
def game_over(playerkey):
    for card in displays[playerkey]:
        if isinstance(card, int):
            return False
    return True


def main():
    num_players = int(input("How many players are there?"))
    # creating the dislay and card lists for each player
    for i in range(num_players):
        key = f"player{i+1}"
        displays[key] = create_display()
        cards[key] = create_cards()
        # randomizing the cards for each player
        cards[key] = randomize_cards(key)
    # matching game
    while True:
        for i in range(num_players):
            key = f"player{i+1}"
            print_board(displays[key], key)
            card1 = choose_card()
            flip_up(card1, key)
            print_board(displays[key], key)
            card2 = choose_card()
            flip_up(card2, key)
            print_board(displays[key], key)
            if not is_match(card1, card2, key):
                flip_down(card1, card2, key)
            if game_over(key):
                break
        
main()


