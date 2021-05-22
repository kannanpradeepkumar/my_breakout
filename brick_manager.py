from brick import Brick

BRICK_STARTING_POSITION = (0, 0)
STARTING_Y_POS = 105
WALL_HEIGHT = 4


class BrickManager:
    brick_list = []

    def __init__(self):
        self.y_pos = STARTING_Y_POS
        for _ in range(0, WALL_HEIGHT):
            self.y_pos += 20
            for x_pos in range(-350, 450, 100):
                new_brick = Brick()
                new_brick.goto(x=x_pos, y=self.y_pos)
                self.brick_list.append(new_brick)

    def is_hit(self, ball_position):
        for b in self.brick_list:
            if b.is_active and b.distance(ball_position) < 70 and b.ycor() - ball_position[1] < 20:
                b.is_active = False
                b.color("black")
                return True
        return False
