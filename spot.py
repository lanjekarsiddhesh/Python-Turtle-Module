import random
# import colorgram
import turtle
from turtle import  *
# rgb_color=[]
# hsl_color=[]
# colors=colorgram.extract('spot_drawing.png', 30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_color.append(new_color)
# print(rgb_color)
# for color in colors:
#     h = color.hsl.h
#     s = color.hsl.s
#     l = color.hsl.l
#     new_color = (h,s,l)
#     hsl_color.append(new_color)
# print(hsl_color)


colour_list = [(246, 242, 235), (247, 240, 244), (239, 242, 247), (237, 245, 240), (212, 149, 95), (215, 80, 62),
               (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29),
               (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96),
               (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63),
               (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]


# horizontal=int(input("How many row you want:- "))
# vertical=int(input("How many column you want:- "))
spot=Turtle()
my_screen=Screen()
turtle.colormode(255)
def draw(x,y):
    for j in range(y):
        my_screen.bgcolor("grey")
        for i in range(x):
            spot.dot(20,random.choice(colour_list))
            spot.penup()
            spot.forward(30)
            spot.pendown()

        spot.penup()
        spot.backward(30 * x)
        spot.left(90)
        spot.forward(30)
        spot.right(90)

draw(10,10)

# spot.speed(0)
# spot.hideturtle()
# spot.penup()
# spot.setheading(225)
# spot.forward(300)
# spot.setheading(0)
# num_of_dotas=100
# for dot_count in range(1,num_of_dotas+1):
#     spot.dot(20,random.choice(colour_list))
#     spot.forward(50)
#     if dot_count % 10==0:
#         spot.setheading(90)
#         spot.forward(50)
#         spot.setheading(180)
#         spot.forward(500)
#         spot.setheading(0)
my_screen.exitonclick()
