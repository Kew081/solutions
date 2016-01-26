#!/usr/bin/env python3

from time import sleep
from random import randint

# list of responses
responses = ["Yes", "No", "Probably", "Maybe", "I don't think so", "Perhaps",
             "It's possible", "Yes, I think so", "That seems likely", "Sure",
             "That's not possible", "I would hope so", "Sounds like it could be true",
             "You shoudn't do that", "But why?", "Dreadfully tinny word, that is",
             "The cake is a lie!", "A man chooses. A slave obeys.", "Did you set it to Wumbo?", "42"]

def magic():
    question = input("Ask me a question: ")

    print("\nThinking ...")
    sleep(1)
    print(responses[randint(0, 20)], "\n")

    loop()

def loop():
    play = input("\nWould you like to play again? (y/n) ").lower()

    if play == "y":
        magic()

    elif play == "n":
        print("Goodbye!")

    else:
        print("I didn't quite catch that.")
        loop()

if __name__ == '__main__':
    print("\nWelcome to the Magic 8 ball!")
    magic()
