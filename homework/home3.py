#!/usr/bin/env python3

def palindrom():
    inp = input("Enter some words: ").lower().split()
    for word in inp:
        if word[::-1] == word:
            print("Okay")
        else:
            print("No")

# компьютер перемешивает все буквы в слове
from random import choice, shuffle

lis = ["mainkun", "word", "human", "addres"]

count = 0
points = 0

while True:
    word = list(choice(lis).lower())

    print("word:", ''.join(word))

    inp = input("Enter what word was print: ")

    if count == 3:
        break
    else:
        if inp == word:
            print("Right!")
            points += 1
        else:
            print("Wrong!")
            points -= 1
        count -= 1