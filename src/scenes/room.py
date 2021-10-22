from pygame import surface
from src.scene import Scene
import pygame
from src.player import Player
from src.enemy import Enemy
from src.button import Button
import random
import math


class RoomScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player()
        self.font = pygame.font.Font("assets/font/Silver.ttf", 48)
        self.is_pause = False

        # Background
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
        self.background_rect = self.background_image.get_rect()
        self.background_rect.bottom = self.game.screen.get_height()
        self.background_rect_1 = self.background_rect.copy()
        self.background_rect_1.left = self.background_image.get_width()

        # Score
        self.score_sound = pygame.mixer.Sound("assets/sound/score.wav")
        self.text_score = self.font.render(
            f"Score : {int(self.game.score)}", False, (255, 255, 255)
        )
        self.text_temperature = self.font.render(
            f"Temperature: {int(self.player.temperature)}°C", False, (255, 255, 255)
        )

        # enemy Group
        self.enemies = pygame.sprite.Group()
        pygame.mixer.music.load("assets/sound/music.wav")
        pygame.mixer.music.play(-1)

    def update(self):
        if self.is_pause is not True:
            vel = math.ceil((50 + (self.game.score / 110)) * (self.game.dt / 100))
            self.player.update(self.game.dt)

            # spawn Enemies
            if len(self.enemies) == 0 or random.randint(0, 50) == 10:
                self.enemies.add(Enemy(random.randint(0, 1)))
            self.enemies.update(vel, self.game.dt)

            # update Background
            self.background_rect.left -= vel
            self.background_rect_1.left -= vel
            if self.background_rect.left <= -self.background_image.get_width():
                self.background_rect.left = (
                    self.background_image.get_width() + self.background_rect_1.left
                )
            if self.background_rect_1.left <= -self.background_image.get_width():
                self.background_rect_1.left = (
                    self.background_image.get_width() + self.background_rect.left
                )

            # update HUD
            self.text_score = self.font.render(
                f"Score : {int(self.game.score)}", False, (255, 255, 255)
            )
            self.text_temperature = self.font.render(
                f"Temperature : {int(self.player.temperature)}°C",
                False,
                (255, 255, 255),
            )

            # append Score
            self.game.score += self.game.dt / 200

            # check If Player Collides Enemies
            self.check_collides()

            # check Player Temperature
            if abs(self.player.temperature) >= 5:
                self.game_over()

            # Pause
            self.pause_surface = pygame.Surface(self.screen.get_size())
            self.pause_surface.set_alpha(200)
            self.pause_button = pygame.sprite.GroupSingle(
                Button(
                    size=[256, 64],
                    position=[
                        self.screen.get_width() / 2,
                        self.screen.get_height() / 2,
                    ],
                    font=self.font,
                    text="RESUME",
                    color="#ffffff",
                    shadow_color=(255, 255, 255),
                    hover_color="#f4f4f4",
                    text_color="#113e25",
                    on_pressed=self.unpause,
                )
            )
        else:
            self.pause_button.update()

    def check_collides(self):
        collides = pygame.sprite.spritecollide(
            self.player, self.enemies, True, pygame.sprite.collide_mask
        )

        for collide in collides:
            if collide.type == 0:
                self.player.temperature += 1
            else:
                self.player.temperature -= 1

    def draw(self):

        # draw Background
        self.screen.blit(
            self.background_image,
            self.background_rect,
        )
        self.screen.blit(
            self.background_image,
            self.background_rect_1,
        )

        # draw Player
        self.screen.blit(self.player.image, self.player.rect)

        # draw Enemies
        self.enemies.draw(self.screen)

        # draw Hud
        self.screen.blit(self.text_score, (10, 5))
        self.screen.blit(
            self.text_temperature, (10, self.text_temperature.get_height())
        )
        if self.is_pause:

            self.screen.blit(self.pause_surface, (0, 0))
            self.pause_button.draw(self.screen)

    def handle_event(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.pause()

    def game_over(self):
        self.game.change_scene("game_over")

    def pause(self):
        self.is_pause = True
        pygame.mixer.music.pause()

    def unpause(self):
        self.is_pause = False
        pygame.mixer.music.unpause()
