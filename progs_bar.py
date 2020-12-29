#!/usr/bin/env python3
from sys import stderr
from time import sleep

inp = int(input("Enter number: "))

for g in range(inp):
    val = '█'
    emp_space = ' '
    val *= int(g / 10)
    emp_space *= int((inp - 1 - g) / 10)
    if g == inp - 1:
        stderr.write(f'\r|{val}{emp_space}| - {g + 1}/{inp}\n')
    else:
        stderr.write(f'\r|{val}{emp_space}| - {g + 1}/{inp}')
    sleep(0.01)