import random
import turtle
from turtle import  *
my_screen=Screen()


sid=Turtle()
sid.color("black","white")
sid.begin_fill()
for i in range(4):
    sid.forward(100)
    sid.right(90)
my_screen=turtle.Screen()
sid.end_fill()



#---------------------------------------------------------------------------
draw=Turtle()
# draw_on_screen=turtle.Screen()
my_screen.title("Graphics Screen")
my_screen.bgcolor("Purple")
draw.shape("turtle")
draw.color("white","black")
# draw.hideturtle()
draw.speed(1) #fastest=0, fast=10, normal=6, slow=3, slwest=1
draw.begin_fill()
for _ in range(2):
    draw.forward(100)
    draw.left(90)
    draw.forward(200)
    draw.left(90)
draw.end_fill()
# draw_on_screen.exitonclick()



#--------------------------------------------------------------------------------
dot=Turtle()
dot.shape("arrow")
dot.speed(1)
for i in range(10):
    dot.forward(10)
    dot.penup()
    dot.forward(10)
    dot.pendown()


my_screen.exitonclick()


