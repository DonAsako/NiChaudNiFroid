import pygame
from pygame import time


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player_run = pygame.image.load("assets/image/player_run.png")
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (20, 600)
        self.index = 0
        self.jump_sound = pygame.mixer.Sound("assets/sound/jump.wav")

    def update(self, dt):
        self.handle_event()
        if self.index >= 4:
            self.index = 0

        self.image = self.get_image(int(self.index), 0)
        self.index += 1 * (dt / 100)

    def get_image(self, x: int, y: int):
        image = pygame.Surface((48, 48))
        image.blit(self.player_run, (0, 0), (x * 48, y * 48, 48, 48))
        image.set_colorkey((0, 0, 0))
        image = pygame.transform.scale(image, (48 * 2, 48 * 2))
        return image

    def say(self, message: str):
        pass

    def handle_event(self):
        pass
