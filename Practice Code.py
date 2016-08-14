'''
Scratch pad for practice code while reading the book
"Think Python 3 - Second Edition"
'''

import turtle


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(27,15))