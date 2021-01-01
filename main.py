import random
import turtle

cursor = turtle.Turtle()


def move_forwards():
    cursor.forward(10)


def move_backwards():
    cursor.backward(10)


def tilt_left():
    angle = cursor.heading() + 10
    cursor.setheading(angle)


def tilt_right():
    angle = cursor.heading() - 10
    cursor.setheading(angle)


def clear():
    cursor.clear()
    cursor.penup()
    cursor.home()
    cursor.pendown()


screen = turtle.Screen()
screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=tilt_left)
screen.onkey(key='d', fun=tilt_right)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
