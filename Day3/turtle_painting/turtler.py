from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(number_sides):
    for i in range(number_sides):
        angle = 360 / number_sides
        timmy.forward(100)
        timmy.right(angle)

# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_side_n)

directions = [0, 90, 180, 270]
timmy.pensize(5)

# for i in range(200):
#     timmy.color(random.choice(colours))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

timmy.speed("fastest")

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.color(random.choice(colours))
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

# draw_spirograph(5)

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()





screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()