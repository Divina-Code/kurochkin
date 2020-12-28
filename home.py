#!/usr/bin/env python3
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