import random
import turtle
from turtle import  *
walk=Turtle()
my_screen=Screen()
turtle.colormode(255)
direction=[0,90,180,270]
# my_screen.bgcolor("light grey")
walk.pensize(5)
walk.speed(0)

def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_colour=(r,g,b)
    return  random_colour
for i in range(200):
    my_screen.bgcolor(random_colour())
    walk.color(random_colour())
    walk.forward(30)
    walk.setheading(random.choice(direction))

my_screen.exitonclick()