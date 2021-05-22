import time
from turtle import Screen
from paddle import Paddle
from brick_manager import BrickManager
from ball import Ball


screen = Screen()
screen.title("breakout")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

brick_manager = BrickManager()
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    ball.move()

    # detect collision between ball and paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -220:
        ball.bounce_y()

    # detect collision between ball and bricks
    if brick_manager.is_hit(ball.pos()):
        ball.bounce_y()

    # detect collision between ball and top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # detect collision between ball and left and right wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    screen.update()


















screen.exitonclick()
