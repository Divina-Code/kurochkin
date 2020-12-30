#!/usr/bin/env python3
# нужно дополнять
# hit - hot - dot - gog - coy

# дописать

from random import randint as rid

it = 0
gess_code = True

while True:
    if it == 4:
        print("You finish the game!")
        break
    else:
        if gess_code == True:
            code = str(rid(100, 999))
            print(f"Right number: {code}")

        rnum = 0
        rplace = 0
        inp = input("Enter secret code:\t")

        if len(inp) != 3 :
            print("This nmber isn`t three letter")
            gess_code = False
        elif not inp.isdigit():
            print("This isn`t number")
            gess_code = False

        elif inp == code:
            print("You right gess number!")
            gess_code = True
            it += 1
        else:
            for g in inp:
                if g in code:
                    rnum += 1
            for er in range(3):
                if inp[er] == code[er]:
                    rplace += 1
            print(f"You right gess {rnum} numbers and {rplace} places of numbers!")
            gess_code = False