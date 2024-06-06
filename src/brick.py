import pygame
import random

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

class Brick:
    def __init__(self, x, y, level):
        self.rect = pygame.Rect(x, y, 60, 20)   #벽돌의 위치와 크기를 설정
        self.durability = level     #벽돌의 내구도를 설정
        self.font = pygame.font.Font(None, 18)  #글꼴과 크기를 설정
        self.text_surface = self.font.render(str(self.durability), True, WHITE) #render(text, antialias(텍스트 가장자리 부드럽게 할지 여부), color, background)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)    #텍스트의 위치를 벽돌의 중앙으로 설정

    def hit(self):
        self.durability -= 1
        if self.durability <= 0:
            return True #내구도가 0 이하면 true를 반환
        else:
            self.update_text()  #내구도를 업데이트하고 텍스트를 갱신
            return False    #내구도가 남아있으면 false를 반환
    
    def update_text(self):
        #현재 내구도 값을 렌더링하여 텍스트를 갱신
        self.text_surface = self.font.render(str(self.durability), True, WHITE)

    def draw(self, screen):
        if self.durability > 0: #내구도가 0보다 크면 벽돌을 그린다
            pygame.draw.rect(screen, BLUE, self.rect)   #벽돌을 그린다
            screen.blit(self.text_surface, self.text_rect)  ##벽돌에 내구도 텍스트를 그린다
            
    def initialize_bricks(level):
        brick_count = level     #레벨에 따라 벽돌의 개수를 설정
        #랜덤한 위치에 벽돌을 배치
        brick_positions = [(random.randint(0, 9) * (60 + 10) + 35, random.randint(0, 9) * (20 + 10) + 35) for _ in range(brick_count)]
        return [Brick(x, y, level) for x, y in brick_positions] #백돌 객체 리스트를 생성하여 반환