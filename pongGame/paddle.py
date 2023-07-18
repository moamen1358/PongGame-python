from turtle import Turtle

POSITION = [(350, 0), (-350, 0)]


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.create_paddle(i=0)

    def create_paddle(self, i):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(POSITION[i])
        self.xcor()
        self.ycor()

    def move_paddle_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def move_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
