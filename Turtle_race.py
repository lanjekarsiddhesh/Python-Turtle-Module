import random
from turtle import Turtle,Screen
from tkinter import messagebox
is_on_race=False
my_screen=Screen()
my_screen.setup(800,400)
messagebox.showinfo("Turtle's Colours", "red\ngreen\nblue\nyellow\norange\npurple\ndark slate blue\nmedium violet red")
user_bet=my_screen.textinput("Make Your Bet","Which turtle will win the race? Enter colour:-")
color=["red","green","blue","yellow","orange","purple","dark slate blue","medium violet red"]
y_coordinate=[130,100,70,40,10,-20,-50,-80,-110,-140]
line=Turtle()
line.hideturtle()
x=[-345,350]
line.right(90)
for i in range(0,2):
    line.speed(6)
    line.penup()
    line.goto(x[i],195)
    line.pendown()
    line.forward(375)
    line.penup()

line.left(90)

for _ in range(0,9):
    line.goto(-400,y_coordinate[_]+15)
    line.pendown()
    line.forward(800)
    line.penup()


all_turtle=[]
for index in range(0,8):
    turtle=Turtle("turtle")
    turtle.penup()
    turtle.color(color[index])
    turtle.goto(-370,y_coordinate[index])
    all_turtle.append(turtle)


if user_bet:
    is_on_race=True

while is_on_race:
    for turtle_race in all_turtle:
        if turtle_race.xcor() > 350:
            is_on_race=False
            winning_color=turtle_race.pencolor()
            if winning_color == user_bet:
                messagebox.showinfo("Turtle Race Result",f"Winner is {winning_color} Turtle\nYou've won the bet!!! ")
            else:
                messagebox.showinfo("Turtle Race Result",f"Winner is {winning_color} Turtle\nYou've loss the bet!!! ")


        num=random.randint(0,10)
        turtle_race.forward(num)

my_screen.exitonclick()