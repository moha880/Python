from math import sin, pi
import turtle
import time
import os
t = turtle.Turtle()
wn = turtle.Screen()
t.shape("turtle")
wn.bgcolor("lavender blush")
t.speed(1)
os.system("start 1.mp3")

colors = ["red", "deep pink", "light pink", "midnight blue", "blue", "dodger blue", "deep sky blue"]

def color(iteration):
    t.pencolor(colors[iteration % len(colors)])
    
def at(x, y):
    t.penup()
    t.home()
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.pendown()

def heart(size, shape):
    t.pensize(5)
    radius = size * sin(shape * pi / 180) / (1 + sin((90 - shape) * pi / 180))
    t.right(shape)
    t.forward(size)
    t.circle(radius, 180 + shape)
    t.right(180)
    t.circle(radius, 180 + shape)
    t.forward(size)
    t.left(180 - shape)

def hearts():
    turtle.delay(0)
    for iteration in range(1, 14):
        color(iteration)
        at(0, iteration * -5)
        heart(iteration * 10, 45)
        time.sleep(0.5)

        
hearts()

t.penup()
t.goto(0,-100)
t.color("red")
time.sleep(1)
t.write("****love you****", None, "center", 14)
t.goto(1,-125)
time.sleep(1)
t.write("**** ya Ayosh ****", None, "center", 14)
t.goto(2,-150)
time.sleep(1)
t.write("**** يا روح قلبي يصغنن ****", None, "center", 14)
t.goto(3,-175)
time.sleep(1)
t.write("**** وعلي طول معاكي يا يبت ****", None, "center", 14)
t.color("white")
t.goto(0,-300)
time.sleep(1)
turtle.done()
