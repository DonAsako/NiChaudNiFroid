from src.scene import Scene
import pygame
from src.button import Button
import os


class ScoresScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.row_height = self.screen.get_height() / 8
        self.column_width = self.screen.get_width() / 8
        self.scores = []

        # Title
        self.title_font = pygame.font.Font("assets/font/Silver.ttf", 96)
        self.title_image = self.title_font.render(
            "Best Scores", False, (255, 255, 255, 0.5)
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
                color="#5a5d91",
                hover_color="#725a91",
                text_color=(255, 255, 255),
                on_pressed=lambda: self.game.change_scene("menu"),
            ),  # Back Button
        )

        # Scores
        if not os.path.exists(self.game.score_filename):
            open(self.game.score_filename, "w").close()
        with open(self.game.score_filename, "r") as file:
            scores = file.read().split(";")
            scores.pop()
            self.scores = [int(score) for score in scores]
        self.scores.sort(reverse=True)

        self.score_font = pygame.font.Font("assets/font/Silver.ttf", 48)
        self.scores_text = []

        # load scores
        for i in range(10):
            if i >= len(self.scores):
                break
            score = self.scores[i]
            score_image = self.score_font.render(
                f"n°{i+1:02d} - {score:02d}", False, (255, 255, 255, 0.5)
            )
            score_rect = score_image.get_rect()
            score_rect.center = (
                self.screen.get_width() / 2,
                self.row_height * (2 + i / 2),
            )
            self.scores_text.append([score_image, score_rect])
            i += 1

    def update(self):
        self.buttons.update(self.game.events)

    def draw(self):
        self.screen.fill("#7794b4")
        self.screen.blit(self.title_image, self.title_rect)
        for score in self.scores_text:
            self.screen.blit(score[0], score[1])
        self.buttons.draw(self.screen)

    def handle_event(self):
        pass
