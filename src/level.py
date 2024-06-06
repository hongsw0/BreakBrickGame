from brick import Brick
from ball import Ball
from paddle import Paddle

class Level:
    def __init__(self, level=1):
        self.level = level
        self.bricks = Brick.initialize_bricks(self.level)   #현재 레벨에 맞는 벽돌을 초기화

    def level_up(self, ball, paddle):
        self.level += 1  
        self.increase_speed(ball)  
        self.shorten(paddle) 
        self.bricks = Brick.initialize_bricks(self.level)   #새로운 레벨에 맞는 벽돌을 초기화
        
    def increase_speed(self, ball): #공 x,y축 속도를 10% 증가 
        ball.speed_x *= 1.1
        ball.speed_y *= 1.1
        
    def shorten(self, paddle):  #패들의 너비를 10 줄이고 최소 너비를 30으로 설정
        paddle.rect.width = max(30, paddle.rect.width - 10)