import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "grey"]


class Brick(Turtle):
    def __init__(self):
        super(Brick, self).__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color(random.choice(COLORS))
        self.is_active = True
