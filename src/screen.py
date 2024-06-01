# 게임화면 그리기 및 갱신
# 객체 그리기 관련 메서드
# 화면 갱신 관련 메서드


import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("벽돌깨기 게임")
        self.font = pygame.font.Font(None, 36)


    def fill(self, color):
        self.screen.fill(color)


    def draw_text(self, text, position):
        text_surface = self.font.render(text, True, WHITE)
        self.screen.blit(text_surface, position)


    def update(self):
        pygame.display.flip()


    def draw(self, *args):
        for drawable in args:
            drawable.draw(self.screen)