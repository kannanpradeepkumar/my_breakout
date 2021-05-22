from turtle import Turtle

PADDLE_MOVE_SPEED = 50
PADDLE_STARTING_POSITION = (0, -240)


class Paddle(Turtle):
    def __init__(self):
        super(Paddle, self).__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.goto(PADDLE_STARTING_POSITION)

    def move_left(self):
        new_x = self.xcor() - PADDLE_MOVE_SPEED
        if new_x > -355:
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + PADDLE_MOVE_SPEED
        if new_x < 355:
            self.goto(new_x, self.ycor())
