# Senior
# Thenea Sun
# Oct. 3rd
# The program will model a simple hand of blackjack between one player and a dealer, in order to simulate a very
# simplified hand of blackjack.

import random


def draw_a_card():
    number = random.randint(1, 10)
    return number


def main():
    card1 = draw_a_card()
    card2 = draw_a_card()
    card3 = draw_a_card()
    card4 = draw_a_card()
    card5 = draw_a_card()
# We need to define the cards here first, otherwise it will not print out the number it got
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

    if users_total + card3 >= 21:
        print("Your total went over 21, you lose.")
    elif users_total + card3 > dealers_total:
        print("You win!")
    elif users_total + card3 <= dealers_total:
        print("You lose.")
# These statements make sure the program runs without misjudgement.


main()