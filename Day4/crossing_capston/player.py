from turtle import Turtle

FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.goto(0, -280)
        self.setheading(90)

    def go_up(self):
        self.forward(20)

    def go_to_start(self):
        self.goto(0, -280)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else: 
            return False
    
