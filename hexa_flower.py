from turtle import *
from colorsys import *

bgcolor("black")
speed(0)
pensize(2)
h = 0
n = 36

for i in range(n):
    col = hsv_to_rgb(h, 1, 1)
    color(col)
    h += 1 / n

    for j in range(6):
        circle(100)
        left(60)

    left(360 / n)

hideturtle()
done()
