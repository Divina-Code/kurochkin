#!/usr/bin/env python3
from sys import stderr
from time import sleep

for g in range(250):
    val = '█'
    emp_space = ' '
    it = 250
    val *= int(g / 10)
    emp_space *= int((it - 1 - g) / 10)
    if g == it - 1:
        stderr.write(f'\r|{val}{emp_space}| - {g + 1}/{it}\n')
    else:
        stderr.write(f'\r|{val}{emp_space}| - {g + 1}/{it}')
    sleep(0.01)