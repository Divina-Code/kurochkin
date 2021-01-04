#!/usr/bin/env python3
'''
 помошник для изучения англиского можно добавить пару слов слово - перевод
 потом нужно угадать перевод слова

'''

from random import choice

word_list = {
    "word" : "w"
}

while True:
    inp = input("Enter command: ")
    if inp == "a":
        ans = input("Enter word and it`s translation: ").split()
        if len(ans) == 2:
            word = ans[0]
            tran = ans[1]

            if word_list.get(word) == None:
                word_list[word] = tran
                print("Word was add to your dictionary")
            else:
                print("This word and it`s translate is already exist")
    if inp == "wordl":
        print(*word_list.keys(), sep="\n")
    if inp == "del":
        word = input("Enter word that you want to delete: ")
        if word_list.get(word) == None:
            print("Try agan")
        else:
            word_list.pop(word)
            print(f"{word} was deleted fortunately")
            print(word_list)
    if inp == "play":
        lis = []
        for g in word_list:
            lis.append(g)
        word = choice(lis)
        while True:
            ans = input(f"Enter translation of {word}: ")
            if ans == word_list[word]:
                print("You win!")
                break
            else:
                print("Try agan")
    if inp == "exit":
        break