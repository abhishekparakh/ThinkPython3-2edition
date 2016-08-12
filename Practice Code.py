'''
Scratch pad for practice code while reading the book
"Think Python 3 - Second Edition"
'''


import turtle
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    circumfrence = 2*math.pi*r
    n = 15  #I fixed it
    length = circumfrence/n
    polygon(t, length, n)

def arc(t, r, angle):
    circumfrence = 2*math.pi*r
    n=15    #I fixed it
    length = circumfrence/n
    arcSize = angle/360
    for i in range(int(arcSize*n)):  #this aint very good
        t.fd(length)
        t.lt(360/n)

bob = turtle.Turtle()
radius = 50
arc(bob, radius, 270)

turtle.mainloop()
