from turtle import Turtle, write


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.speed(1)
        self.x = 10
        self.y = 10
        self.first_score = 0
        self.second_score = 0
        self.fast = .1

    def move_ball(self):

        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def check_top_bot(self):
        if self.ycor() >= 300 or self.ycor() <= -300:
            self.y *= -1

    def check_paddle(self):
        self.x *= -1
        self.fast *= .9

    def check_right_left(self):
        if self.xcor() >= 400 or self.xcor() <= -400:
            self.goto(0, 0)
            self.x *= -1

    def score(self):
        self.hideturtle()
        self.penup()
        self.clear()
        self.goto(0, 280)
        self.write((f"{self.first_score} : {self.second_score}"))
