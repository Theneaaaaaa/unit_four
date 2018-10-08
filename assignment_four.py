# Senior
# Thenea Sun
# Oct. 3rd
# The program will model a simple hand of blackjack between one player and a dealer, in order to simulate a very
# simplified hand of blackjack.

import random


def draw_a_card():
    number = random.randint(1, 10)
    return number


def game_mode():
    card1 = draw_a_card()
    card2 = draw_a_card()
    card3 = draw_a_card()
    card4 = draw_a_card()
    card5 = draw_a_card()
# We need to define the cards here first, otherwise it will not print out the number it got.
    users_total = card1 + card2
    dealers_total = card4 + card5
    print("You got a", card1, "and a", card2)
    print("Your total is", users_total)
    answer = input("Would you like another card? (Please type 'y' or 'n')")
    if answer == "y":
        print("Your new card is", card3, "and your total is now", users_total + card3)
        print("The dealer now have a", card4, "and a", card5)
        print("The dealer's total is", dealers_total)
    elif answer == "n":
        print("The dealer now have a", card4, "and a", card5)
        print("The dealer's total is", dealers_total)
    else:
        print("Please type in either 'y' or 'n', otherwise the program will not run correctly.")
    win_or_lose = users_total + card3
    if win_or_lose > 21:
        print("Your total went over 21, you lose.")
    elif win_or_lose == 21:
        print("Blackjack! You win!")
    elif win_or_lose > dealers_total:
        print("You win!")
    else:
        print("You lose.")
# These statements make sure the program runs without misjudgement.


def main():
    start_game = input("Welcome to the Blackjack game! I am your dealer. Please type 'start' to play.")
    if start_game == "start":
        game_mode()
    else:
        second_chance = input("Please type 'start' to start the game.")
        if second_chance == "start":
            game_mode()
        else:
            print("You lost. Because you did not even want to start the game.")


main()
