import pygame
import time
from ball import Ball
from paddle import Paddle
from brick import Brick
from screen import Screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from collision import detect_collision
from level import Level
import admin

class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.ball = Ball()
        self.paddle = Paddle()
        self.running = False
        self.paused = False
        self.score = 0
        self.lives = 3
        self.player_name = None

    def get_player_name(self):
        name = ""   #플레이어 이름을 저장할 변수를 초기화
        while True:
            for event in pygame.event.get():    #pygame 이벤트를 처리
                if event.type == pygame.QUIT:   #종료 이벤트가 발생하면 pygame을 종료하고 프로그램을 종료
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:    #키보드 입력 이벤트를 처리
                    if event.key == pygame.K_RETURN:    #Enter 키를 누르면 이름 입력을 완료
                        return name
                    elif event.key == pygame.K_BACKSPACE:   #Backspace 키를 누르면 이름에서 마지막 글자를 삭제
                        name = name[:-1]
                    else:   #다른 키를 누르면 이름에 해당 문자를 추가
                        name += event.unicode
            self.screen.fill(BLACK)
            self.screen.draw_text("Enter your name:", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            self.screen.draw_text(name, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()   #화면을 업데이트
            self.clock.tick(30) #초당 30프레임으로 고정

    def initialize_ball_and_paddle(self):
        self.ball = Ball()  #Ball 객체를 다시 생성하여 초기화
        self.paddle = Paddle()  #Paddle 객체를 다시 생성하여 초기화
        
    def reset_ball_and_paddle(self):
        ball_speed_x = self.ball.speed_x    #현재 Ball 객체의 x축 속도를 저장
        ball_speed_y = self.ball.speed_y    #현재 Ball 객체의 y축 속도를 저장
        paddle_width = self.paddle.rect.width   #현재 Paddle 객체의 너비를 저장
        self.ball = Ball(ball_speed_x, ball_speed_y)    #저장된 속도로 Ball 객체를 다시 생성
        self.paddle = Paddle(paddle_width)  #저장된 너비로 Paddle 객체를 다시 생성

    def run(self):
        self.player_name = self.get_player_name()   #플레이어 이름을 입력받음
        self.running = True #게임을 실행 상태로 설정
        self.countdown()    #게임 시작 카운트다운을 실행
        while self.running: 
            self.handle_events()    #이벤트를 처리
            self.update()   #게임 상태를 업데이트
            self.draw() #화면에 그림
            self.clock.tick(60) #초당 60 프레임으로 고정
        self.show_game_over_screen()    #게임 오버 화면을 표시

    def countdown(self):
        for i in range(3, 0, -1):   #3초 카운트 다운 실행
            self.screen.fill(BLACK)
            self.screen.draw_text(f"Game starts in {i}...", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.update()    #화면 업데이트
            time.sleep(1)   #1초 동안 대기

    def handle_events(self):
        for event in pygame.event.get():    #pygame이벤트 처리
            if event.type == pygame.QUIT:   #종료 이벤트가 발생하면 게임을 종료
                self.running = False
            if event.type == pygame.KEYDOWN:    #키보드 입력 이벤트 처리
                if event.key == pygame.K_SPACE: #스페이스바를 누르면 일시정지 또는 재개
                    self.paused = not self.paused

    def update(self):
        if not self.paused: #게임이 일시정지 되지 않았을때
            keys = pygame.key.get_pressed() #현재 눌린 키 상태를 가져옴
            self.paddle.move(keys)  #패들을 이동
            self.ball.move()    #공을 이동
            if detect_collision(self.ball, self.paddle, self.level.bricks): #충돌을 감지
                self.score += 10    #충돌이 발생하면 점수를 증가

            if self.ball.rect.bottom >= SCREEN_HEIGHT:  #공이 화면 하단에 닿으면
                self.lives -= 1     #목숨이 하나 까임
                if self.lives > 0:
                    self.reset_ball_and_paddle()    #목숨이 남아있으면 공과 패들을 초기화
                else:
                    self.running = False    #목숨이 모두 사라지면 게임을 종료

            if not self.level.bricks:   #모든 벽돌이 사라졌을때
                self.level.level_up(self.ball, self.paddle) #레벨을 올리고
                self.reset_ball_and_paddle()    #공과 패들을 초기화
                self.wait_for_level_up()    #레벨 업 화면을 표시
                
    def wait_for_level_up(self):
        self.screen.fill(BLACK)
        self.screen.draw_text("Level Up!", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.update()    #화면을 업데이트
        pygame.time.wait(1000)  #1초동안 대기

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.draw(self.paddle, self.ball, *self.level.bricks)
        self.screen.draw_text(f"Score: {self.score}", (150, 10))
        self.screen.draw_text(f"Level: {self.level.level}", (10, 10))
        self.screen.draw_text(f"Lives: {self.lives}", (SCREEN_WIDTH - 150, 10))
        if self.running:
            self.screen.draw_text(f"Player: {self.player_name}", (10, SCREEN_HEIGHT - 30))
        if self.paused:
            self.screen.draw_text("Paused", (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
        self.screen.update()

    def show_game_over_screen(self):
        self.screen.fill(BLACK)
        game_over_font = pygame.font.Font(None, 50) #게임 오버 텍스트의 글꼴과 크기를 설정
        score_font = pygame.font.Font(None, 36) #점수 텍스트의 글꼴과 크기를 설정
        game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
        score_text = score_font.render(f"Score: {self.score}", True, (255, 255, 255))
        player_text = score_font.render(f"Player: {self.player_name}", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        player_rect = player_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.screen.blit(game_over_text, game_over_rect) #게임 오버 텍스트를 화면에 그림
        self.screen.screen.blit(score_text, score_rect) #점수 텍스트를 화면에 그림
        self.screen.screen.blit(player_text, player_rect)   #플레이어 이름 텍스트를 화면에 그림
        self.screen.draw_text("Press R to play again or Q to quit", (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()   #화면을 업데이트
        admin.save_user_data(self.player_name, self.score, self.level.level)    #플레이어 데이터를 저장
        self.wait_for_key() #키 입력을 대기

    def wait_for_key(self):
        waiting = True  #키 입력 대기 상태를 나타내는 플래그
        while waiting:
            for event in pygame.event.get():    #pygame 이벤트를 처리
                if event.type == pygame.QUIT:   #종료 이벤트가 발생하면
                    waiting = False         #대기 상태를 종료하고
                    self.running = False    #게임을 종료
                if event.type == pygame.KEYDOWN:    #키보드 입력 이벤트 처리
                    if event.key == pygame.K_r: #R키를 누르면
                        self.restart_game()     #게임을 재시작
                        self.run()          #??????????????????????
                        waiting = False
                    elif event.key == pygame.K_q:   #Q키를 누르면
                        waiting = False         #대기 상태를 종료하고
                        self.running = False    #게임을 종료

    def restart_game(self):
        self.level = Level()    #레벨을 초기화
        self.score = 0
        self.lives = 3
        self.running = True #게임을 실행 상태로 설정
        self.level.bricks = Brick.initialize_bricks(self.level.level)   #벽돌 초기화
        self.initialize_ball_and_paddle()   #공과 패들 초기화