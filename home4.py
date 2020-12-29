#!/usr/bin/env python3

# дописать

from random import randint as rid

code = str(rid(100, 999))

while True:
    print(f"Right number: {code}")
    rnum = 0
    rplace = 0
    inp = input("Enter secret code:\t")

    if len(inp) != 3 :
        print("This nmber isn`t three letter")
    elif not inp.isdigit():
        print("This isn`t number")

    elif inp == code:
        print("You right gess number!")
    else:
        for g in inp:
            if g in code:
                rnum += 1
        for er in range(3):
            if inp[er] == code[er]:
                rplace += 1
        print(f"You right gess {rnum} numbers and {rplace} places of numbers!")