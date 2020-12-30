#!/usr/bin/env python3

# functions
'''
    факториал числа 8
    3 != 1 * 2 * 3

'''

def factor(num):
    ans = 1
    for g in range(1, num+1):
        ans *= g

    print(ans)

factor(3)