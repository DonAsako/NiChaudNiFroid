import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type):
        pygame.sprite.Sprite.__init__(self)
        self.type = enemy_type
        self.images = ["assets/image/fire.png", "assets/image/ice.png"]
        self.image = pygame.transform.scale(
            pygame.image.load(self.images[self.type]),
            (48, 48),
        ).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = 600 if self.type == 1 else 480
        self.rect.left = 1280

    def update(self, vel):
        self.rect.left -= vel
        if self.rect.right <= 0:
            self.kill()
