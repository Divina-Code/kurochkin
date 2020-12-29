#!/usr/bin/env python3

inp = input("Enter some words: ").lower()
inp = inp.split()
for word in inp:
    if word[::-1] == word:
        print("Okay")
    else:
        print("No")
