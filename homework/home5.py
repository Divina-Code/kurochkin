#!/usr/bin/env python3

# генератор паролей 8 символов со спкциальными символами

# не успел

st = list("ZYXWVUTSRQPONMLKJIHGFEDCBA").lower()
stp = list("ZYXWVUTSRQPONMLKJIHGFEDCBA")
speclet = list("!@#$%^&*()?><:~")

from random import choice

word1 = choice(st)
word2 = choice(stp)
word3 = choice(speclet)
