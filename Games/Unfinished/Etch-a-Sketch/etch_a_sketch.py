from turtle import *

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(5)

def move_backward():
    turtle.backward(5)
    
def clear_board():
    turtle.clear()
    

def move_to_origin():
    turtle.penup()
    turtle.home()
    turtle.pendown()
    
def turn_left():
    turtle.left(5)

def turn_right():
    turtle.right(5)
    
screen.onkeypress(move_forward,"Up")
screen.onkeypress(turn_left,"Left")
screen.onkeypress(turn_right,"Right")
screen.onkeypress(move_backward,"Down")
screen.onkeypress(clear_board,"z")
screen.onkeypress(move_to_origin,"r")
screen.listen()
screen.exitonclick()



