import pygame
import random
from screen import SCREEN_WIDTH, SCREEN_HEIGHT

RED = (255, 0, 0)

class Ball:
    def __init__(self, speed_x=4, speed_y=4):
        #공의 초기 위치를 홤녀의 가운데로 설정, 크기는 10x10으로 설정
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 10, 10)
        #공의 초기 속도를 설정하며, x축과 y축은 랜덤하게 결정
        self.speed_x = speed_x * random.choice((1, -1))
        self.speed_y = speed_y * random.choice((1, -1))

    def move(self):
        #공의 속도에 따라 이동
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        #공이 왼,오른쪽 벽에 닿으면 x축 방향을 반전
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        #공이 위쪽 벽에 닿으면 y축 방향을 반전
        if self.rect.top <= 0:
            self.speed_y *= -1

    def draw(self, screen):
        #화면에 빨강 공을 그림
        pygame.draw.ellipse(screen, RED, self.rect)