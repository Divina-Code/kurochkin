#!/usr/bin/env python3

inp = input("Enter some words: ").lower()
inp = inp.split()
if inp[::-1] == inp:
    print("Okay")
else:
    print("No")
