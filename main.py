#!/usr/bin/env python3

print("It is my repository!")

# classic if
num = 10
if 2 < num < 6:
    print("3-5")
elif 6 < num < 120:
    print("7-119")
else:
    print("num < 0 or num > 120")

# how old are you
inp = int(input("Enter your age: "))
if inp < 19:
    print("You are young -", inp)
else:
    print("you are older than 19 or you 19 -", inp)

# year
year = int(input("Enter your year: "))
char = len(str(year))
print("bool -", len(str(year)) == 5)
print("char number -", char)
print("your year is ", year)

# user name
us_name = str(input("Enter your name: "))
print("your name is -", us_name)

print(bool(""), bool("snv"))
print(bool(0), bool(9))
print()

# second lesson

print("float -", float(345.97))
print("max -", max(13, 45, 99))
print("min -", min(8347, 283490, 4930))

# cycle
i = 1
while i < 10:
    print("It`s while")
    i += 1
g = True

while g:
    ans = str(input(("хокеистов слышен плач пропустил вратарь ...")))
    if ans == "шайбу":
        print("Yes, you are right!")
        g = False
    else:
        print("You lose, try again")
