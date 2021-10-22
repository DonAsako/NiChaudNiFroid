import pygame
from src.scene import Scene


class GameOverScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        # Game Over Title
        self.font = pygame.font.Font("assets/font/Silver.ttf", 192)
        self.title_image = self.font.render("GAME OVER.", False, (0, 0, 0))
        self.index = 0
        self.text = ""

    def update(self):
        self.index += self.game.dt / 500
        self.text += (int(self.index) - len(self.text)) * "."
        if len(self.text) > 3:
            self.text = ""
            self.index = 0

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.title_image = self.font.render("GAME OVER" + self.text, False, (0, 0, 0))
        self.screen.blit(
            self.title_image,
            (
                (self.screen.get_width() - self.title_image.get_width()) / 2,
                (self.screen.get_height() - self.title_image.get_height()) / 2,
            ),
        )

    def handle_event(self):
        pass
