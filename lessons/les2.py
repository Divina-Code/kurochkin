#!/usr/bin/env python3

print("Second lesson")

# random
import random as r

num = r.randint(1, 10)
print(num)

from time import sleep

sleep(1)

# // - int number % - float number

print(not True, "- not")
print(True and True, "- and")
print(False and True)
print(False and False)
print(True or False, "- or")
print(False or False)
print(True or True)
print(True is False, "- is")
print(False is False)

# strings

print("word" + "-another word")
print("word\n" * 9)

# slice

print("word"[::-1]) # [START:STOP:STEP]
print("wordi"[1])

w = "wOrd".upper()
print(w)

if w.lower() in "dmsvkWord".lower():
    print("yes")

print("madnes".title())

# function(object) and object.method()

# find

print("word".find("wo"))

print(ord("a"))
print(chr(ord("A")))

# lists

lis = ["Darenka", "Bonya", "Jenny"]

print(f"number of elements {len(lis)}")
print(sorted(lis))
lis.sort()
print(lis)
print(lis[1])
lis.append("Tom")
lis.pop(0)
print(lis)
print(lis)