# 게임상태 (진행중, 일시정지, 종료)
# 플레이어 정보 (점수, 목숨)


# 게임 시작, 일시정지, 재시작, 종료 관련 메서드
# 점수 업데이트, 플레이어 목숨 감소 등 상태변화 관련 메서드

import pygame
import time
from ball import Ball
from paddle import Paddle
from screen import Screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from collision import detect_collision
from admin import GameAdmin
from level import Level
from brick import setup_bricks

class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.clock = pygame.time.Clock()
        self.ball = Ball() #인스턴스 속성
        self.paddle = Paddle()
        self.level = Level()
        self.bricks = setup_bricks(self.level.get_level())
        self.running = True
        self.paused = False
        self.score = 0
        self.lives = 3
        self.admin = GameAdmin()

    def run(self):
        self.countdown()
        while self.running:
            self.handle_events() #입력처리
            self.update() #게임 상태 업데이트(패들, 충돌검사)
            self.draw() #업데이트된 상태 그리기
            self.clock.tick(60) #프레임 속도
        self.admin.save_score(self.score)  # 게임 오버 시 점수 저장
        self.show_game_over_screen()

    def countdown(self):
        for i in range(3, 0, -1):
            self.screen.fill(BLACK)
            self.screen.draw_text(f"Game starts in {i}...", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.update()
            time.sleep(1) #1초 대기

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused

    def update(self):
        if not self.paused:
            keys = pygame.key.get_pressed()
            self.paddle.move(keys)
            self.ball.move()
            if detect_collision(self.ball, self.paddle, self.bricks):
                self.score += 10

            if self.ball.rect.bottom >= SCREEN_HEIGHT:
                self.lives -= 1
                if self.lives > 0:
                    self.reset_ball_and_paddle()
                else:
                    self.running = False

            if all(brick.durability <= 0 for brick in self.bricks):
                self.next_level()

    def next_level(self):
        self.level.increase_level()
        self.level.ball_speed(self.ball)  # 공의 속도 증가
        self.level.paddle_length(self.paddle)  # 패들 길이 감소 
        self.bricks = setup_bricks(self.level.get_level())
        self.paused = True  # 다음 레벨 시작 시 잠시 멈춤
        self.draw()  # 화면 갱신
        self.screen.draw_text(f"Level {self.level}", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # 레벨 표시
        pygame.display.flip()
        # self.screen.draw_text(f"Level : {self.level}", (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50))
        pygame.time.delay(2000)  # 2초간 대기
        self.paused = False  # 멈춤 해제  

    def draw(self):
        self.screen.fill(BLACK)
        self.screen.draw(self.paddle, self.ball, *self.bricks)
        self.screen.draw_text(f"Score: {self.score}", (10, 10))
        self.screen.draw_text(f"level: {self.level.get_level()}", (SCREEN_WIDTH // 2, 10))
        self.screen.draw_text(f"Lives: {self.lives}", (SCREEN_WIDTH - 100, 10))
        if self.paused and not self.level.increase_level():
            self.screen.draw_text("Paused", (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
        self.screen.update()

    def show_game_over_screen(self):
        self.screen.fill(BLACK)
        game_over_font = pygame.font.Font(None, 50)
        score_font = pygame.font.Font(None, 36)
        game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
        score_text = score_font.render(f"Score: {self.score}", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.screen.blit(game_over_text, game_over_rect)
        self.screen.screen.blit(score_text, score_rect)
        self.screen.draw_text("Press R to play again or Q to quit", (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart_game()
                        self.run()
                        waiting = False
                    elif event.key == pygame.K_q:
                        waiting = False
                        self.running = False

    def restart_game(self):
        self.ball = Ball()
        self.paddle = Paddle()
        self.level = Level()
        self.bricks = setup_bricks(self.level.get_level())
        self.score = 0
        self.lives = 3
        self.running = True

    def reset_ball_and_paddle(self):
        self.ball = Ball()
        self.paddle = Paddle()