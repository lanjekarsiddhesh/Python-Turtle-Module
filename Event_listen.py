from turtle import Turtle,Screen

pet=Turtle()
my_screen=Screen()
my_screen.title("Etch-A-Sketch")
def move_forword():
    pet.forward(5)

def move_backword():
    pet.backward(5)

def move_anticlock():
    pet.left(5)
    # new_heading=pet.heading()+10
    # pet.setheading(new_heading)

def move_clock():
    pet.right(5)

def pen_up():
    pet.penup()

def pen_down():
    pet.pendown()
def clear():
    # pet.clear()
    pet.reset()


my_screen.listen()
my_screen.onkeypress(key="w",fun=move_forword)
my_screen.onkeypress(key="s",fun=move_backword)
my_screen.onkeypress(key="a",fun=move_anticlock)
my_screen.onkeypress(key="d",fun=move_clock)
my_screen.onkeypress(key="u",fun=pen_up)
my_screen.onkeypress(key="space",fun=pen_down)
my_screen.onkeypress(key="c",fun=clear)
my_screen.exitonclick()