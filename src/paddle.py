import pygame
from screen import SCREEN_WIDTH, SCREEN_HEIGHT

WHITE = (255, 255, 255)

class Paddle:
    def __init__(self, width=100):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - width // 2, SCREEN_HEIGHT - 30, width, 10)  #패들의 사각형을 생성
        self.speed = 6

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:  #왼쪽 화살표 키를 누르고 패들이 화면 좌측에 닿지 않았으면
            self.rect.x -= self.speed   #패들을 왼쪽으로 이동
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH: #오른쪽 화살표 키를 누르고 패들이 화면 우측에 닿지 않았으면
            self.rect.x += self.speed   #패들을 오른쪽으로 이동

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)  #패들을 회면에 그림