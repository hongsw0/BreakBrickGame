# 관리자 역할
# 게임이 끝날 때 플레이어의 점수를 데이터베이스에 저장
# 최고 점수 목록을 관리 및 조회

import sqlite3
import pygame
from screen import Screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK

class GameAdmin:
    def __init__(self):
        self.db_name = 'game_scores.db'
        self.conn = None
        self.cursor = None
        self.player_name = ''
        self.screen = Screen()
        self.init_db()
        self.get_player_name()

    def init_db(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def get_player_name(self):
        running = True
        self.screen.fill(BLACK)
        self.screen.draw_text("Enter your name:", (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
        pygame.display.flip()
        
        name = ""
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.player_name = name
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode

            self.screen.fill(BLACK)
            self.screen.draw_text("Enter your name:", (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
            self.screen.draw_text(name, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            pygame.display.flip()

    def save_score(self, score):
        # 높은 점수부터 저장되는지 확인
        self.cursor.execute('SELECT MAX(score) FROM scores')
        max_score = self.cursor.fetchone()[0]

        # 최고 점수가 현재 점수보다 낮다면
        if max_score is None or score > max_score:
            # 현재 점수를 저장
            self.cursor.execute('INSERT INTO scores (name, score) VALUES (?, ?)', (self.player_name, score))
            self.conn.commit()
        else:
            # 최고 점수부터 정렬하여 가져오기
            self.cursor.execute('SELECT name, score FROM scores ORDER BY score DESC')
            high_scores = self.cursor.fetchall()
            # 최고 점수부터 순회하며 현재 점수가 들어갈 위치 찾기
            for idx, (_, old_score) in enumerate(high_scores, start=1):
                if score > old_score:
                    self.cursor.execute('INSERT INTO scores (name, score) VALUES (?, ?)', (self.player_name, score))
                    self.conn.commit()
                    break
                
    def close_db(self):
        self.conn.close()