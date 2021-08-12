from src.scene import Scene
import pygame
from src.player import Player


class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font("assets/font/Silver.ttf", 192)
        self.title_image = self.font.render(
            "Ni Chaud, Ni Froid", False, (200, 200, 200)
        )
        self.title_rect = self.title_image.get_rect()
        self.title_rect.left = (
            self.screen.get_width() - self.title_image.get_width()
        ) / 2
        self.title_rect.top = 50
        self.index = 0

        # Button
        self.space_button = pygame.image.load("assets/image/button_space.png")
        self.button_image = self.get_image_animation_space_key()
        self.button_rect = self.button_image.get_rect()
        self.button_rect.center = (
            (self.screen.get_width() + 64) / 2,
            (self.screen.get_height() / 8) * 6,
        )

        # Player
        self.player_idle = pygame.image.load("assets/image/player_idle.png")
        self.player_image = self.get_image_animation_player()
        self.player_rect = self.player_image.get_rect()
        self.player_rect.center = (
            (self.screen.get_width() + 48) / 2,
            (self.screen.get_height() / 8) * 4,
        )

    def update(self):
        # Player Animation
        self.player_image = self.get_image_animation_player()
        self.index += 1 * (self.game.dt / 100)
        if self.index >= 9:
            self.index = 0

        # Button Animation
        self.button_image = self.get_image_animation_space_key()

    def draw(self):
        self.screen.fill((11, 11, 11))
        self.screen.blit(self.title_image, self.title_rect)
        self.screen.blit(self.player_image, self.player_rect)
        self.screen.blit(self.button_image, self.button_rect)

    def get_image_animation_player(self):
        image = pygame.Surface((48, 48))
        image.blit(self.player_idle, (0, 0), (int(self.index) * 48, 0, 48, 48))
        image.set_colorkey((0, 0, 0))
        return pygame.transform.scale(image, (48 * 4, 48 * 4))

    def get_image_animation_space_key(self):
        image = pygame.Surface((64, 32))
        image.blit(
            self.space_button, (0, 0), ((int(self.index / 2) % 2) * 64, 0, 64, 64)
        )
        image.set_colorkey((0, 0, 0))
        return pygame.transform.scale(image, (64 * 4, 32 * 4))

    def handle_event(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.game.change_scene("room")
