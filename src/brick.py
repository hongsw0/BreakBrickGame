# 플레이어가 깨야 하는 벽돌

import pygame
import random
from screen import SCREEN_WIDTH, SCREEN_HEIGHT
from level import Level

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

class Brick:
    # 위치(x, y 좌표)
    def __init__(self, x, y, durability):
        self.rect = pygame.Rect(x, y, 60, 20)
        self.durability = durability
        self.font = pygame.font.Font(None, 18)
        self.update_text()

    # 내구도 (깨지기 전 후 상태)
    # 벽돌 파괴 관련 메서드
    def hit(self):
        self.durability -= 1
        if self.durability <= 0:
            return True
        else:
            self.update_text()
            return False
    
    def update_text(self):
        self.text_surface = self.font.render(str(self.durability), True, WHITE)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        if self.durability > 0:
            pygame.draw.rect(screen, BLUE, self.rect)
            screen.blit(self.text_surface, self.text_rect)

def setup_bricks(level):
    bricks = []
    brick_width = 60
    brick_height = 20
    gap = 10  # 벽돌 사이의 간격

    # 랜덤한 위치에 벽돌 생성
    for _ in range(level * level):
        # 벽돌의 x 좌표 계산
        x = random.randint(0, 740)  # 화면 너비 범위 내에서 랜덤한 x 좌표 선택 (0 ~ 740)
        # 벽돌의 y 좌표 계산
        y = random.randint(50, 200)  # 상단 50~200 픽셀 사이에서 랜덤한 y 좌표 선택
        # 벽돌 생성 및 리스트에 추가
        brick = Brick(x, y, level)
        bricks.append(brick)
    return bricks