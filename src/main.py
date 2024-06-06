import pygame
import sys
from admin import get_top_scores
import admin
from game import Game

class MainMenu:
    def __init__(self):
        pygame.init()   #pygame 초기화
        self.screen = pygame.display.set_mode((800, 600))   #화면의 크기를 설정
        self.clock = pygame.time.Clock()    #게임의 시간 관리를 위한 clock 객체를 생성
        self.font = pygame.font.Font(None, 36)  #텍스트를 그리기 위한 폰트를 설정
        admin.create_table()    #데이터베이스 테이블을 생성

    def show_menu(self):
        while True:
            self.screen.fill((255, 255, 255))   #화면을 흰색으로 채우기 
            self.draw_text("Main Menu", 400, 50)    
            self.draw_button("Highest Scores", 400, 200)
            self.draw_button("Start Game", 400, 300)
            pygame.display.flip()   #화면을 업데이트
            self.clock.tick(30) #초당 30프레임으로 고정

            for event in pygame.event.get():    #pygame 이벤트를 처리
                if event.type == pygame.QUIT:   #종료 이벤트가 발생하면
                    pygame.quit()       #게임을 종료
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:  #마우스를 누르는 이벤트 처리
                    mouse_pos = pygame.mouse.get_pos()  #마우스 위츠를 가져옴
                    if self.is_button_clicked(mouse_pos, 400, 200): #최고 점수 버튼이 클릭되면
                        self.show_top_scores()  #최고 점수 화면을 표시
                    elif self.is_button_clicked(mouse_pos, 400, 300):   #게임 시작 버튼이 클릭되면
                        return "start_game" #'start game'을 반환

    def draw_text(self, text, x, y, color=(0, 0, 0)):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))    #텍스트의 위치를 설정
        self.screen.blit(text_surface, text_rect)   #화면에 텍스트를 그림

    def draw_button(self, text, x, y):
        button_rect = pygame.Rect(x - 100, y - 20, 200, 40) #버튼의 사각형을 생성
        pygame.draw.rect(self.screen, (0, 0, 0), button_rect, 2)    #버튼의 테두리를 그림
        self.draw_text(text, x, y)  #버튼 텍스트를 그림

    def is_button_clicked(self, mouse_pos, button_x, button_y):
        button_rect = pygame.Rect(button_x - 100, button_y - 20, 200, 40)   #버튼의 사각형을 생성
        return button_rect.collidepoint(mouse_pos)  #마우스 클릭이 영역 내에 있는지 확인하고 결과를 반환

    def show_top_scores(self):
        top_scores = get_top_scores()   #최고 점수를 가져옴
        self.screen.fill((255, 255, 255))
        self.draw_text("Highest Scores", 400, 50)   #최고 점수 텍스트를 화면에 그림
        if not top_scores:  #최고 점수가 없으면
            self.draw_text("Player data does not exist", 400, 150, color=(255, 0, 0))   #플레이어 데이터가 없음을 알리는 텍스트를 그림
        else:   #최고 점수가 있으면
            y = 150
            for i, (name, score) in enumerate(top_scores, 1):   #최고 점수를 반복하면서
                self.draw_text(f"{i}. {name}: {score}", 400, y) #순위와 점수를 화면에 그림
                y += 50
        self.draw_button("Main Menu", 400, 500) #메인 메뉴로 돌아가는 버튼을 그림
        pygame.display.flip()   #화면을 업데이트
        while True: #무한 루프
            for event in pygame.event.get():    #pygame 이벤트 처리
                if event.type == pygame.QUIT:   #종료 이벤트가 발생하면 게임을 종료
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #ESC키를 누르면
                    return  #함수를 종료
                elif event.type == pygame.MOUSEBUTTONDOWN:  #마우스 누르는 이벤트를 처리
                    mouse_pos = pygame.mouse.get_pos()  #마우스 위치 가져옴
                    if self.is_button_clicked(mouse_pos, 400, 500): #메인 멩뉴로 돌아가는 버튼이 클릭되면
                        return  #함수를 종료

if __name__ == "__main__":
    menu = MainMenu()   #MainMenu클래스의 인스턴스를 생성
    choice = menu.show_menu()   #메인메뉴를 표시하고 사용자의 선택을 받음
    if choice == "start_game":  #'start game'을 선택하면
        game = Game()   #게임 객체를 생성
        game.run()  #게임을 실행