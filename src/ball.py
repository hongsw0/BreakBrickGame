# 벽돌을 깨는 공


import pygame
import random
from screen import SCREEN_WIDTH, SCREEN_HEIGHT

RED = (255, 0, 0)

class Ball:
    def __init__(self):
        #공을 화면 중앙에 생성
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 10, 10) #screen의 중앙에서 공이 생성
        self.speed_x = 4 * random.choice((1, -1))
        self.speed_y = 4 * random.choice((1, -1))

    def move(self):
        #공을 이동시키기
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        #화면의 좌우 경계에서 반사
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        #화면의 상단 경계에서 반사
        if self.rect.top <= 0:
            self.speed_y *= -1

    def draw(self, screen):
        #공을 화면에 그리기
        pygame.draw.ellipse(screen, RED, self.rect)

    def reset_speed(self):
        self.speed_x = 4 * random.choice((1, -1))
        self.speed_y = 4 * random.choice((1, -1))