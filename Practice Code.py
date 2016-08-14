'''
Scratch pad for practice code while reading the book
"Think Python 3 - Second Edition"
'''

import turtle


def is_power(a,b):
    if a/b == 1:
        return True
    if a%b != 0:
        return False
    return is_power(a/b,b)

print(is_power(27,3))