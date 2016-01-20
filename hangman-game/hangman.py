import random

def wrong_guess(num_of_guesses):
    if num_of_guesses == 6:
        print("""
            _________
            |      |
            |      O
            |
            |
            |
            |
            |
        ---------
        """)

    elif num_of_guesses == 5:
        print("""
            _________
            |      |
            |      O
            |     |||
            |
            |
            |
            |
        ---------
        """)

    elif num_of_guesses == 4:
        print("""
            _________
            |      |
            |      O
            |     |||
            |      |
            |
            |
            |
        ---------
        """)

    elif num_of_guesses == 3:
        print("""
            _________
            |      |
            |      O
            |    /|||
            |      |
            |
            |
            |
        ---------
        """)

    elif num_of_guesses == 2:
        print("""
            _________
            |      |
            |      O
            |    /|||\\
            |      |
            |
            |
            |
        ---------
        """)

    elif num_of_guesses == 1:
        print("""
            _________
            |      |
            |      O
            |    /|||\\
            |      |
            |     /
            |
            |
        ---------
        """)

    elif num_of_guesses == 0:
        print("""
            _________
            |      |
            |      O
            |    /|||\\
            |      |
            |     / \\
            |
            |
        ---------

        You lose.
        """)

    print("You have {} guesses left.".format(num_of_guesses))

# word list
words = ["Google", "Anakin", "Starship", "Dalek", "Lannister", "titan",
        "compiler", "interpreter", "differentiation", "reddit", "time",
        "Dumbledore", "turing machine", "traveler", "blubber", "tweak"
        "Antarctica", "relativity", "quantum", "algorithm", "complexity",
        "discrete", "python", "machine", "atom", "electron"]

# choose a single word from the list and get its length
word = words[random.randint(0, len(words))]
wordLength = len(word)

# create a list of letters that are in word
letters = []
for char in word:
    letters.append(char)

guesses = 7

# start game
print("""

Let's play Hangman.

    _________
    |      |
    |
    |
    |
    |
    |
    |
---------
""" +
"_ " * wordLength
)

# main loop
while True:

    guess = input("Guess a single letter or the word: ")

    if guess == word:
        print("You win!")
        break
    else:
        for char in guess:
            if char in letters:
                continue
    else:
        guesses -= 1
        wrong_guess(guesses)

    if guesses == 0:
        break
