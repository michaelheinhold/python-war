import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# deck class with value and suit
class Deck:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

# logic for when printing to call face cards by their names
def check_for_face(card):
    match(card):
        case 11:
            return 'Jack'
        case 12:
            return 'Queen'
        case 13:
            return 'King'
        case _: return card


def main():
    # setup empty decks for each player
    player1_deck = []
    player2_deck = []
    # create and shuffle a deck of cards with 52 cards and suits with values 1-13
    deck = [Deck(value, suit) for value in range(1, 14) for suit in suits]
    random.shuffle(deck)
    # deal 26 cards to each player using pop to keep cards unique
    for i in range(26):
        player1_deck.append(deck.pop())
        player2_deck.append(deck.pop())

    # Start game
    print("Welcome to War, the card game")
    player1_name = input("Enter Player 1 name: ")
    player2_name = input("Enter Player 2 name: ")
    choice = ""

    # game loop
    while choice != 'q' or choice != 'Q':
        #check if either player is out of cards - end game
        if len(player1_deck) == 0 or len(player2_deck) == 0:
            if len(player1_deck) == 0:
                print(f"{ player1_name } has run out of cards, { player2_name } wins !")
            else:
                print(f"{ player2_name } has run out of cards, { player1_name } wins !")
            break

        # prompt user to play or quit
        choice = input("(P)lay, (C)heck statuses or (Q)uit: ")
        if choice == "Q" or choice == "q":
            break
        elif choice == "C" or choice == "c":
            print(f"{ player1_name } has { len(player1_deck) } cards. While { player2_name } has { len(player2_deck) } cards.")
            continue
        elif choice != "P" and choice != "p":
            print("Invalid choice, please choose P or Q.")
            continue

        # new round so empty played_cards list / initialize
        played_cards = []
        # setup new while loop so logic is re-run on Wars, keeping code DRY
        logic = True
        while logic == True:
            # determine and remove played cards by each player, store in new list
            player1_played = player1_deck.pop(0)
            player2_played = player2_deck.pop(0)
            played_cards.append(player1_played)
            played_cards.append(player2_played)

            # print cards played
            print(f"{ player1_name } played: { check_for_face(player1_played.value) } of { player1_played.suit }.\n{ player2_name } played: { check_for_face(player2_played.value) } of { player2_played.suit }.")


            # checking cards against each other
            if player1_played.value == player2_played.value:
                print("WAR!\nThree cards added face down")
                # 3 face down cards added to played pile
                for x in range(3):
                    # protection agains erros - calling pop on empty list
                    if len(player1_deck) <= 0 or len(player2_deck) <= 0:
                        break
                    else:
                        played_cards.append(player1_deck.pop(0))
                        played_cards.append(player2_deck.pop(0))
                # repeat inner while loop for new played cards
                continue
            elif player1_played.value > player2_played.value:
                print(f"{ player1_name } wins!")
                # add all played cards to winners hand
                for x in played_cards:
                    player1_deck.append(x)
                logic = False
            else:
                print(f"{ player2_name } wins!")
                for x in played_cards:
                    player2_deck.append(x)
                logic = False


    # Exit logic
    if len(player1_deck) > len(player2_deck):
        print(f"{ player1_name } won the game with { len(player1_deck) } cards! While { player2_name } had { len(player2_deck) }")
    elif len(player2_deck) > len(player1_deck):
        print(f"{ player2_name } won the game with { len(player2_deck) } cards! While { player1_name } had { len(player1_deck) }")
    else:
        print(f"It was a tie, you both had { len(player1_deck) } cards!")
    print("Thanks for playing!")

main()