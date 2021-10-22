from src.scene import Scene
import pygame
from src.button import Button


class SettingsScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.row_height = self.screen.get_height() / 8
        self.column_width = self.screen.get_width() / 8

        # Title
        self.title_font = pygame.font.Font("assets/font/Silver.ttf", 96)
        self.title_image = self.title_font.render(
            "Settings", False, (255, 255, 255, 0.5)
        )
        self.title_rect = self.title_image.get_rect()
        self.title_rect.center = (
            self.screen.get_width() / 2,
            self.row_height * 1,
        )

        # Button
        self.button_font = pygame.font.Font("assets/font/Silver.ttf", 36)
        self.buttons = pygame.sprite.Group(
            Button(
                size=[122, 48],
                position=[10 + 66, 10 + 24],
                font=self.button_font,
                text="<- Back",
                color="#113e25",
                shadow_color=(255, 255, 255),
                hover_color="#5e915a",
                text_color=(255, 255, 255),
                on_pressed=lambda: self.game.change_scene("menu"),
            ),  # Back Button
        )

    def update(self):
        self.buttons.update()

    def draw(self):
        self.screen.fill("#7794b4")
        self.screen.blit(self.title_image, self.title_rect)
        self.buttons.draw(self.screen)

    def handle_event(self):
        pass
