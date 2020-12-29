#!/usr/bin/env python3
def ot():
    # 1
    year = int(input("Enter your year of birth: "))
    name = str(input("Enter your name: "))

    age = 2020 - year

    print("Your age is ", age)

    if age >= 18:
        print("I think that you need to watch thriller")
    else:
        print("I think you need to watch comedy")

    # 2

    g = True
    while g:
        ans = int(input("6 + 7 ** 2 = ... "))
        if ans == 55:
            print("You are win!")
            g = False
        elif ans == 20:
            print("I catch you, wrong answer")
        else:
            print("Wrong answer")

# 3  нужно угадать число загадоное компютером с random, писать число большо загадоного, равно, больше

import random as r

def th():
    l = list()
    for i in range(10):
        l.append(i)

    num = r.choice(l)

    g = True
    while g:
        ans = int(input("Enter number: "))
        if ans == num:
            print("You are win! number is right!")
            g = False
        else:
            if ans > num:
                print("That number more than right number")
            else:
                print("That number less then right number")

# 4 если у когото при вытаскивании карт будет в сумме больше 21, то он проиграл, а если ровно 21, то выиграл, всвего 3 игрока

print("Game 21 start!")

# cards
l = list()
for i in range(0, 13):
    l.append(i)

# players
pl1 = r.choice(l)
l.remove(pl1)
player1 = 1
steel1 = 1
print(f"{player1} get card - {pl1}")

pl2 = r.choice(l)
l.remove(pl2)
player2 = 2
steel2 = 1
print(f"{player2} get card - {pl2}")

# main game
g = True
while g:
    # check
    if steel2 == 0:
        print(f"Player {player2} lose, and {player1} win!")
        break
    elif steel1 == 0:
        print(f"Player {player1} lose, and {player2} win!")
        break
    else:
        print("Everything okay")


    card = r.choice(l)
    l.remove(card)

    print("Player -", player1, "get card with number -", card)
    pl1 += card
    print("Player have now", pl1)
    if pl1 > 21:
        print(player1, "- lose")
        break
    elif pl1 == 21:
        print(player1, "- Win!")
        break
    else:
        print("Everything okey")

        inp = str(input("Do you want continue?(y, n): "))
        if inp == "n":
            steel1 = 0
            print(f"Player {player1} exit")
        else:
            steel1 = 1
        # 2

        if steel2 == 0:
            print(f"Player {player2} lose, and {player1} win!")
            break
        elif steel1 == 0:
            print(f"Player {player1} lose, and {player2} win!")
            break
        else:
            print("Okay")

        card = r.choice(l)
        l.remove(card)

        print("Player -", player2, "get card with number -", card)
        pl2 += card
        print("Player have now", pl2)
        if pl2 > 21:
            print(player2, "- lose")
            break
        elif pl2 == 21:
            print(player2, "- Win!")
            break
        else:
            print("Everything okey")

        inp = str(input("Do you want continue?(y, n): "))
        if inp == "n":
            teel2 = False
            print(f"Player {player2} exit")
        else:
            steel2 = True

# 5

word = input("Enter a word: ").lower()
if word[::-1] == word:
    print("Okay")
else:
    print("No")