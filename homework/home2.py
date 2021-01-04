#!/usr/bin/env python3

# 6 список покупок, можно добавить продукт в список, удалить или просмотреть весь список
# ховчет ли пользователь добавить какой-нибудь продукт
print("This is product check list")

lis = []

print('''
    1 - add product
    2 - remove product
    3 - see check list
    4 - exit
    ''')

while True:
    ans = input("Enter number of action that you want to do: ")

    if ans == "1":
        pr = input("Enter name of product: ")
        nump = int(input("Enter number of product in check list: ")) - 1
        lis.insert(nump, pr)
        print(lis)
        print("Done!")
    elif ans == "2":
        nump = input("Enter number of product, if you don`t know it enter 'list': ")
        if nump == "list":
            char = len(lis)
            for i in range(0, char):
                print(f"{i+1} - {lis[i]}")

            num = int(input("Enter number of product: ")) - 1
            lis.pop(num)
            print(lis)
            print("Done!")
        else:
            lis.pop(int(nump)-1)
            print(lis)
            print("Done!")
    elif ans == "4":
        break
    else:
        char = len(lis)
        for i in range(0, char):
            print(f"{i+1} - {lis[i]}")