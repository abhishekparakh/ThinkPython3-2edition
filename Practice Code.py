'''
Scratch pad for practice code while reading the book
"Think Python 3 - Second Edition"
'''


import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

bob = turtle.Turtle()
length = 10
polygon(bob, length, 15)

turtle.mainloop()
