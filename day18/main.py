import turtle as t
import random
t.Turtle()


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    random_color = (r,g, b)
    return random_color


t.colormode(255)
t.penup()
t.speed("fastest")
t.hideturtle()


def left_up():
    t.setheading(90)
    t.forward(50)
    t.setheading(0)


def right_up():
    t.setheading(90)
    t.forward(50)
    t.setheading(180)


for _ in range(5):
    for _ in range(10):
        t.dot(20, random_color())
        t.setheading(180)
        t.forward(50)
    left_up()
    for _ in range(10):
        t.forward(50)
        t.dot(20, random_color())
    right_up()


screen = t.Screen()
screen.exitonclick()
