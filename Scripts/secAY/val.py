# Step 1 import and Set turtle's shape, color
from math import sin, pi

import turtle
import time
turtle.shape("turtle")
turtle.color("red")

# Step 2 set turtle starting position
colors = ["red", "deep pink", "light pink", "midnight blue", "blue", "dodger blue", "deep sky blue"]


def color(iteration):
    turtle.pencolor(colors[iteration % len(colors)])
 

def at(x, y):
    turtle.penup()
    turtle.home()
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.pendown()

def heart(size, shape):
    turtle.pensize(5)
    radius = size * sin(shape * pi / 180) / (1 + sin((90 - shape) * pi / 180))
    turtle.right(shape)
    turtle.forward(size)
    turtle.circle(radius, 180 + shape)
    turtle.right(180)
    turtle.circle(radius, 180 + shape)
    turtle.forward(size)
    turtle.left(180 - shape)

def hearts():
    turtle.delay(0)
    for iteration in range(1, 14):
        color(iteration)
        at(0, iteration * -5)
        heart(iteration * 10, 45)
        time.sleep(0.5)

        
hearts()


# Step 4 Write I love you below heart shape
turtle.penup()
turtle.goto(-120, -180)
turtle.pendown()
turtle.write("I love you!", font=("Arial", 36, "normal"))

# Step 5 set turtle Background fancy colors
t = turtle.Turtle()
colors = ["purple","pink", "maroon", "magenta", "light slate blue",  "violet", "black"]

for color in colors:
    t.screen.bgcolor(color)
    time.sleep(1)

# step 6 Keep the window open until the user closes it
turtle.done()