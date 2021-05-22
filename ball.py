from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 4
        self.y_move = 8
        self.move_speed = 0.1
        self.goto(0,100)

    def move(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1