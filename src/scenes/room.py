from src.scene import Scene
import pygame
from src.player import Player
from src.enemy import Enemy
import random


class RoomScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player()
        self.font = pygame.font.Font("assets/font/Silver.ttf", 48)

        # Background
        self.background_image = pygame.image.load("assets/image/background.png")
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
        self.score = 0
        self.score_sound = pygame.mixer.Sound("assets/sound/score.wav")
        self.text_score = self.font.render(
            f"Score : {int(self.score)}", False, (255, 255, 255)
        )
        self.text_temperature = self.font.render(
            f"Temperature: {int(self.player.temperature)}°C", False, (255, 255, 255)
        )

        # enemy Group
        self.enemies = pygame.sprite.Group()
        pygame.mixer.music.load("assets/sound/music.wav")
        pygame.mixer.music.play(-1)

    def update(self):
        vel = float(50 * (self.game.dt / 100)).__ceil__()

        self.player.update(self.game.dt, vel)

        # spawn Enemies
        if self.score / 2:
            self.enemies.add(Enemy(random.randint(0, 1)))
        self.enemies.update(vel)

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
            f"Score : {int(self.score)}", False, (255, 255, 255)
        )
        self.text_temperature = self.font.render(
            f"Temperature : {int(self.player.temperature)}°C", False, (255, 255, 255)
        )

        # append Score
        self.score += self.game.dt / 200

        # check If Player Collides Enemies
        self.check_collides()

        # check Player Temperature
        if self.player.temperature <= -5 or self.player.temperature >= 5:
            self.game_over()

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

    def handle_event(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.game.change_scene("menu")

    def game_over(self):
        self.game.change_scene("game_over")
