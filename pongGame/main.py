import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

paddle1 = Paddle()
paddle1.create_paddle(0)
paddle2 = Paddle()
paddle2.create_paddle(1)
ball = Ball()
ball2 = Ball()

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.listen()
screen.onkey(paddle1.move_paddle_up, "w")
screen.onkey(paddle1.move_paddle_down, "s")
screen.onkey(paddle2.move_paddle_up, "Up")
screen.onkey(paddle2.move_paddle_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.fast)
    screen.update()
    ball.check_top_bot()
    ball.check_right_left()
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.check_paddle()

    if ball.xcor() >= 390:
        ball2.first_score += 1
        ball.fast = .1
    elif ball.xcor() <= -390:
        ball2.second_score += 1
        ball.fast = .1
    ball2.score()

    if paddle2.position() == ball.position:
        ball.x *= -1
        ball.y *= -1
        ball.move_ball()
    else:
        ball.move_ball()

screen.exitonclick()
