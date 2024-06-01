import pygame
import sys
from admin import get_top_scores
from game import Game

class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

    def show_menu(self):
        while True:
            self.screen.fill((255, 255, 255))
            self.draw_text("Main Menu", 400, 50)
            self.draw_button("Highest Scores", 400, 200)
            self.draw_button("Start Game", 400, 300)
            pygame.display.flip()
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.is_button_clicked(mouse_pos, 400, 200):
                        self.show_top_scores()
                    elif self.is_button_clicked(mouse_pos, 400, 300):
                        return "start_game"

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def draw_button(self, text, x, y):
        button_rect = pygame.Rect(x - 100, y - 20, 200, 40)
        pygame.draw.rect(self.screen, (0, 0, 0), button_rect, 2)
        self.draw_text(text, x, y)

    def is_button_clicked(self, mouse_pos, button_x, button_y):
        button_rect = pygame.Rect(button_x - 100, button_y - 20, 200, 40)
        return button_rect.collidepoint(mouse_pos)

    def show_top_scores(self):
        top_scores = get_top_scores()
        self.screen.fill((255, 255, 255))
        self.draw_text("Highest Scores", 400, 50)
        y = 150
        for i, (name, score) in enumerate(top_scores, 1):
            self.draw_text(f"{i}. {name}: {score}", 400, y)
            y += 50
        self.draw_button("Main Menu", 400, 500)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.is_button_clicked(mouse_pos, 400, 500):
                        return

if __name__ == "__main__":
    menu = MainMenu()
    choice = menu.show_menu()
    if choice == "start_game":
        game = Game()
        game.run() 