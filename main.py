import turtle
from _pyrepl.commands import clear_screen

drawing_board=turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("python turtle")

turtle_instance=turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angel_right():
    turtle_instance.right(45)

def rotate_angel_left():
    turtle_instance.left(45)

def clear_screen():
        turtle_instance.clear()

def turtle_return_home():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()


drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rotate_angel_right,key="Down")
drawing_board.onkey(fun=rotate_angel_left,key="Up")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=turtle_return_home,key="h")
drawing_board.onkey(fun=turtle_pen_up,key="w")
drawing_board.onkey(fun=turtle_pen_down,key="s")

turtle.mainloop()
