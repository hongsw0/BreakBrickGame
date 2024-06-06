import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    #화면 객체를 생성
        pygame.display.set_caption("벽돌깨기 게임") #창 제목을 설정
        self.font = pygame.font.Font(None, 36)  #폰트 객체를 생성


    def fill(self, color):
        self.screen.fill(color) #화면을 지정색으로 채움


    def draw_text(self, text, position):
        text_surface = self.font.render(text, True, WHITE)  #택스트를 랜더링
        self.screen.blit(text_surface, position)    #화면에 텍스트를 그림


    def update(self):
        pygame.display.flip()   #화면을 업데이트


    def draw(self, *args):
        for drawable in args:
            drawable.draw(self.screen)  #인자로 받은 객체들을 화면에 그림