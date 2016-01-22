#!/usr/bin/env python3

def coin_amount(total_mass, coin_mass):
    # calculates the total amount of one type of coin
    coinAmount = total_mass / coin_mass
    if coinAmount < (int(coinAmount) + 0.5):
        coinAmount = int(coinAmount)
    else:
        coinAmount = int(coinAmount) + 1

    return coinAmount


def total_value(penny_amount, nickel_amount, dime_amount, quarter_amount):
    # calculates total value of all coins
    pennyValue = 0.01
    nickelValue = 0.05
    dimeValue = 0.1
    quarterValue = 0.25

    totalValue = pennyValue * penny_amount
    totalValue += nickelValue * nickel_amount
    totalValue += dimeValue * dime_amount
    totalValue += quarterValue * quarter_amount

    if totalValue < (int(totalValue) + 0.5):
        totalValue = int(totalValue)
    else:
        totalValue = int(totalValue) + 1

    return totalValue


def wrappers(coin_amount, coins_in_wrapper):
    # calculates the total amount of wrappers for one type of coin
    wrapper_amount = coin_amount / coins_in_wrapper
    if wrapper_amount != coin_amount // coins_in_wrapper:
        wrapper_amount = coin_amount // coins_in_wrapper + 1
    return int(wrapper_amount)

# mass of each type of coin in grams
pennyMass = 2.5
nickelMass = 5.0
dimeMass = 2.268
quarterMass = 5.67

# amount of coins that fit in each type of wrapper
pennyWrapperCoinAmount = 50
nickelWrapperCoinAmount = 40
dimeWrapperCoinAmount = 50
quarterWrapperCoinAmount = 40

# welcome message and input request
print("\nWelcome to the Coin Estimator!")
print("Please enter the mass of your coins (in grams)")

userPennyMass = float(input("\tPennies: "))
userNickelMass = float(input("\tNickels: "))
userDimeMass = float(input("\tDimes: "))
userQuarterMass = float(input("\tQuarters: "))

# calculations
userPennyAmount = coin_amount(userPennyMass, pennyMass)
userNickelAmount = coin_amount(userNickelMass, nickelMass)
userDimeAmount = coin_amount(userDimeMass, dimeMass)
userQuarterAmount = coin_amount(userQuarterMass, quarterMass)

totalUserCoins = userPennyAmount + userNickelAmount + userDimeAmount + userQuarterAmount
totalUserValue = total_value(userPennyAmount, userNickelAmount, userDimeAmount, userQuarterAmount)

pennyWrapperAmount = wrappers(userPennyAmount, pennyWrapperCoinAmount)
nickelWrapperAmount = wrappers(userNickelAmount, nickelWrapperCoinAmount)
dimeWrapperAmount = wrappers(userDimeAmount, dimeWrapperCoinAmount)
quarterWrapperAmount = wrappers(userQuarterAmount, quarterWrapperCoinAmount)

# print results
print("\nYou have {0} coins".format(int(totalUserCoins)))
print("You have about ${0}".format(totalUserValue))

print("You will need:")
print("\t{0} penny wrappers".format(pennyWrapperAmount))
print("\t{0} nickel wrappers".format(nickelWrapperAmount))
print("\t{0} dime wrappers".format(dimeWrapperAmount))
print("\t{0} quarter wrappers\n".format(quarterWrapperAmount))
