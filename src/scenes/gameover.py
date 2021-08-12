import pygame
from src.scene import Scene


class GameOverScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        # Game Over Title
        self.font = pygame.font.Font("assets/font/Silver.ttf", 192)
        self.title_image = self.font.render("T'as perdu, t'es nul.", False, (0, 0, 0))

        # Gif lose
        self.image_sheet = pygame.image.load("assets/image/gameover.png")
        self.index = 0
        self.image = self.get_image(0)
        # Music
        pygame.mixer.music.load("assets/sound/gameover.ogg")
        pygame.mixer.music.play(-1)

    def update(self):
        self.title_image = self.font.render("T'as perdu, t'es nul.", False, (0, 0, 0))
        self.index += 1 * (self.game.dt / 100)
        if self.index >= 20:
            self.index = 0
        self.image = self.get_image(int(self.index))
        print(self.index)

    def draw(self):
        self.screen.blit(self.image, self.image.get_rect())
        self.screen.blit(
            self.title_image,
            (
                (self.screen.get_width() - self.title_image.get_width()) / 2,
                (self.screen.get_height() - self.title_image.get_height()) / 2,
            ),
        )

    def get_image(self, x: int):
        image = pygame.Surface((320, 240))
        image.blit(self.image_sheet, (0, 0), (x * 320, 0, 320, 240))
        image.set_colorkey((0, 0, 0))
        image = pygame.transform.scale(
            image, (self.screen.get_width(), self.screen.get_height())
        )
        return image

    def handle_event(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.game.change_scene("menu")
