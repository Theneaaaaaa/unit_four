def main():
    ticket_price = int(input("How old are you?"))
    if ticket_price <= 2:
        print("You can get in free!")
    elif ticket_price >= 3 and ticket_price <= 8:
        print("You need pay 8 dollars fro the ticket!")
    else:
        print("Ticket price for you is 10 dollars!")


main()