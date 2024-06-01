# 플레이어가 깨야 하는 벽돌

import pygame
import random

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

class Brick:
    # 위치(x, y 좌표)
    def __init__(self, x, y, level):
        self.rect = pygame.Rect(x, y, 60, 20)
        self.durability = level
        self.font = pygame.font.Font(None, 18)
        self.text_surface = self.font.render(str(self.durability), True, WHITE)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

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

    def draw(self, screen):
        if self.durability > 0:
            pygame.draw.rect(screen, BLUE, self.rect)
            screen.blit(self.text_surface, self.text_rect)