def user_input():
    # get input from user
    while True:
        try:
            price = float(input("Price of item: $"))
            money = float(input("Money given to you: $"))
        except ValueError:
            print("Invalid input: numbers only\n")
        else:
            # check if customer is paying less than item's price
            if price > money:
                print("\nMoney given is less than item's price.")
                while True:
                    try:
                        money = float(input("Please pay a valid amount of money: $"))
                    except ValueError:
                        print("Invalid input: numbers only\n")
                    else:
                        break
            break

    return money - price


def change():
    # dollar values per type of coin
    pennyValue = 0.01
    nickelValue = 0.05
    dimeValue = 0.1
    quarterValue = 0.25
    target = user_input()

    print("Change needed is $" + str(target))
    # Calculate the amount of coins needed to reach the target value.
    quarters = target // quarterValue
    target -= quarters * quarterValue

    dimes = target // dimeValue
    target -= dimes * dimeValue

    nickels = target // nickelValue
    target -= nickels * nickelValue

    pennies = target // pennyValue
    target -= pennies * pennyValue

    print("\t{0} quarters".format(quarters))
    print("\t{0} dimes".format(dimes))
    print("\t{0} nickels".format(nickels))
    print("\t{0} pennies\n".format(pennies))

    go_again()


def go_again():
    # ask user to go again
    choice = input("Would you like to go again? (y/n) ".lower())
    if choice == "Y" or choice == "y":
        change()
    elif choice == "N" or choice == "n":
        print("\nGoodbye!\n")
    else:
        go_again()


print("Welcome to the change calculator!\n")
change()
