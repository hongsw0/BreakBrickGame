# from brick import Brick

# class Level:
#     def __init__(self):
#         self.current_level = 1
#         self.num_bricks = 0
#         self.bricks = []

#     def start_level(self):
#         self.bricks = self.setup_bricks(self.current_level)
#         self.num_bricks = len(self.bricks)

#     def next_level(self):
#         self.current_level += 1
#         self.start_level()

#     def setup_bricks(self, level):
#         num_bricks = 1 + (level - 1) * 3
#         bricks = []
#         for i in range(num_bricks):
#             brick = Brick(i * 70 + 35, 50)
#             bricks.append(brick)
#         return bricks

#     def bricks_left(self):
#         return self.num_bricks

#     def bricks_hit(self):
#         self.num_bricks -= 1

class Level:
    def __init__(self):
        self.level = 1

    def increase_level(self):
        self.level += 1

    def get_level(self):
        return self.level

    def ball_speed(self, ball):
        ball.speed_x *= 1.2
        ball.speed_y *= 1.2

    def paddle_length(self, paddle):
        paddle.rect.width *= 0.8