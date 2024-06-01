# 메인 모듈 지정
# 게임 루프 시작
# 이벤트 처리 (키 입력 및 종료)
# 게임 상태 업데이트
# 프레임 속도 조절

import pygame
from game import Game

def main():
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
    
if __name__ == "__main__":
    main()