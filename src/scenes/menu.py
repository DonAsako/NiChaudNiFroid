import pygame
from src.scene import Scene
from src.player import Player
from src.button import Button


class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.row_height = self.screen.get_height() / 8

        # Title
        self.font = pygame.font.Font("assets/font/Silver.ttf", 192)
        self.title_image = self.font.render(
            "Ni Chaud, Ni Froid", False, (255, 255, 255, 0.5)
        )
        self.title_rect = self.title_image.get_rect()
        self.title_rect.center = (
            self.screen.get_width() / 2,
            self.row_height * 2,
        )
        self.background_image = pygame.image.load(
            "assets/image/background.png"
        ).convert()
        self.background_image = pygame.transform.scale(
            self.background_image,
            (
                self.background_image.get_width() * 2,
                self.background_image.get_height() * 2,
            ),
        )
        self.button_font = pygame.font.Font("assets/font/Silver.ttf", 36)
        self.play_button = Button(
            size=[256, 64],
            position=[
                self.screen.get_width() / 2,
                self.row_height * 4,
            ],
            font=self.button_font,
            text="Play",
            color="#5a5d91",
            hover_color="#725a91",
            text_color=(255, 255, 255),
            on_pressed=lambda: self.game.change_scene("room"),
        )
        self.scores_button = Button(
            size=[256, 64],
            position=[
                self.screen.get_width() / 2,
                self.row_height * 5,
            ],
            font=self.button_font,
            text="Scores",
            color="#5a5d91",
            hover_color="#725a91",
            text_color=(255, 255, 255),
            on_pressed=lambda: self.game.change_scene("scores"),
        )
        self.settings_button = Button(
            size=[256, 64],
            position=[
                self.screen.get_width() / 2,
                self.row_height * 6,
            ],
            font=self.button_font,
            text="Settings",
            color="#5a5d91",
            hover_color="#725a91",
            text_color=(255, 255, 255),
            on_pressed=lambda: self.game.change_scene("settings"),
        )

        self.buttons = pygame.sprite.Group(
            self.play_button, self.settings_button, self.scores_button
        )

    def update(self):
        self.buttons.update(self.game.events)

    def draw(self):
        self.screen.fill("#7794b4")
        self.screen.blit(
            self.background_image,
            (
                0,
                -self.background_image.get_height() / 2,
            ),
        )
        self.screen.blit(self.title_image, self.title_rect)
        self.buttons.draw(self.screen)

    def handle_event(self):
        pass
