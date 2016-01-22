#!/usr/bin/env python3

print("Please enter: ")

name = input("A name: ")
pronoun = input("A third-person pronoun: (he/she) ")
pronoun2 = "his"

animal = input("An animal: ")
place = input("A place: ")
time = input("A period of time: (seconds, years, etc.)")
noun4 = input("A fourth noun: ")

ad1 = input("An adjective: ")
ad2 = input("A second adjective: ")
ad3 = input("A third adjective: ")
ad4 = input("A fourth adjective: ")
ad5 = input("A fifth adjective: ")

if pronoun == "she":
    pronoun2 = "her"

l1 = "Today {0} decided that {1} was going to take {2} {3} to the {4}. ".format(name, pronoun, pronoun2, animal, place)

l2 = "{0} thought that {1} was finally ready to let the {2} {3} be {4}. ".format(name, pronoun, ad1, animal, ad2)

l3 = "You see, it had caused {0} much {1} over the last few {2}. ".format(pronoun2, ad3, time)

l4 = "When {0} arrived at the {1}, {2} decided that {2} {3} another {4} for his {5} instead. ".format(name, place, pronoun, ad4, noun4, animal)

l5 = "So {0} went back home, and to {1} {2}, the {3} was still with {4}.".format(name, pronoun2, ad5, animal, pronoun)

story = l1 + l2 + l3 + l4 + l5
print("\n" + story)
