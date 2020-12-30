#!/usr/bin/env python3
'''
 виселица
 загадывается слово и говорит сколько там букв,
 пользователь вводит букву и выводится слово и если пользователь правильно загадал букву,
 то она отображается, а если нет то закрыта звёздочкой
'''

from random import choice

# не успел

print("gallows!")
print("If you want exit print 'exit")

num = 0
words = ["hangout", "body", "rope", "neck", "gess"]
word = choice(words)
letters = []
for g in word:
    letters.append("_")

print(letters)

while True:
    if letters[num] == word[num]:
        num += 1
        if num >= len(word):
            print("You win!")
            break

    inp = input("Enter a letter: ")
    if inp == "exit":
        break
    for w in range(len(word)):
        if inp == word[w-1]:
            letters[w-1] = word[w-1]

    let = "".join(letters)
    print(let)