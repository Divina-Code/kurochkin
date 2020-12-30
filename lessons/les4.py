#!/usr/bin/env ptyhon3

# dictionarys
# jam
# https://jamboard.google.com/d/1WfeNiD_0JKMglhGKQz_qvCeuGTF5L2s1JpkUR331ax4/edit?usp=sharing

data = {
    # key : value
    "root" : "liar", # we can`t change key in future
    "st_user" : "qwerty176" # everything can be key
}

print(data["root"])

# дописать

print("print n to create new user\n"
      "print a to enter to your account\n")

while True:
    ans = input("You new user or you already registered?[n, a]")
    if ans == "n":
        inp = input("Enter new login and password: ").split()
        if len(inp) == 2:
            log = inp[0]
            pas = inp[1]

            if data.get(log) == None: # None it symbol of nothing
                data[log] = pas
            else:
                print("This login already exist")
        else: # more than 2 or less value/s
            print("Try agan")
    if ans == "a":
        inp = input("Enter your login and password: ").split()
        if len(inp) == 2:
            log = inp[0]
            pas = inp[1]

            if data.get(log) == None:
                print("Try another password or register")
            else:
                if pas == data[log]:
                    print(f"Welkome, {log}")
                else:
                    print("That password is incorrect")
    if ans == "del":
        log = input("Enter login that you want to delete: ")
        if data.get(log) == None:
            print("Try another password or register")
        else:
            data.pop(log)
            print(f"{log} was deleted fortunately")
            print(data)
    if ans == "inf":
        print(*data.keys(), sep="\n")