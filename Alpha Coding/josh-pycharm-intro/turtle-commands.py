import turtle
import random
bob = turtle.Pen()

def up():
    bob.setheading(90)
    bob.forward(100)

def down():
    bob.setheading(270)
    bob.forward(100)

def left():
    bob.setheading(180)
    bob.forward(100)

def right():
    bob.setheading(0)
    bob.forward(100)

colors = ["red", "blue", "green", "yellow", "black"]

def clickLeft(x, y):  # Make sure to have parameters x, y
    bob.color(random.choice(colors))

def clickRight(x, y):
    bob.stamp()

turtle.listen()

turtle.onscreenclick(clickLeft, 1)  # 1: Left Mouse Button, 2: Middle Mouse Button
turtle.onscreenclick(clickRight, 3)  # 3: Right Mouse Button

turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.mainloop()  # This will make sure the program continues to run
