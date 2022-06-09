from card import Card
from deck import Deck


def game_info():
    print("HighLow is a simple card game.")
    print("During each turn of this game, a card is drawn from a shuffled deck of cards.")
    print("You have to predict whether the next card will be higher or lower.")
    print("Your score in the game is the number of correct predictions you make before you guess wrong.")
    print("Making a wrong prediction ends the game.\n")


def main():
    # print game information
    game_info()

    # create a deck of cards and shuffle it
    deck = Deck()
    deck.shuffle()
    nbr_guesses = 0


    current_card = deck.deal()
    print(f"The first card drawn from the deck is {current_card}")

    # REPLACE "pass" statement below with your implementation
    
    while True:
        choice = input('Will the next card be higher (H/h) or Lower (L/l) ?')
        next_card = deck.deal()
        print(f'The next card is {next_card}')

        if choice[0].lower() == 'h'  and next_card > current_card:
            print('Your prediction was correct')
            nbr_guesses +=1
        
        if choice[0].lower() == 'h'  and next_card < current_card:
            print('Your prediction was incorrect')
            break

        if choice[0].lower() == 'l'  and next_card < current_card:
            print('Your prediction was correct')
            nbr_guesses +=1

        if choice[0].lower() == 'l'  and next_card > current_card:
            print('Your prediction was incorrect')
            break
        

        current_card = next_card
        print(f'The current card is {current_card}')
    # DO NOT MODIFY
    print("The game is over.")
    print(f"You made {nbr_guesses} correct predictions.")


# call main() function if this module is executed as a top-level script
if __name__ == "__main__":
    main()
