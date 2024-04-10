import random
import turtle
from turtle import  *
my_screen=Screen()
my_screen.bgcolor("black")
round=Turtle()
turtle.colormode(255)

def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_colour=(r,g,b)
    return  random_colour


round.speed(0)
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        round.color(random_colour())
        round.circle(100)
        round.setheading(round.heading()+size_of_gap)

draw_spirograph(10)
my_screen.exitonclick()