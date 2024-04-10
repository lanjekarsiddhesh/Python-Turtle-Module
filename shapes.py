import random
import turtle
from turtle import  *
shape=Turtle()
my_screen=Screen()
my_screen.bgcolor("black")
color=["deep pink","cyan","yellow","purple","pink","blue","green","red"]
def draw_shape(num_sides):
    side=360/num_sides
    for _ in range(num_sides):
        shape.forward(100)
        shape.left(side)

for shape_side in range(3,11):
    shape.color(random.choice(color))
    draw_shape(shape_side)

my_screen.exitonclick()