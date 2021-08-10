import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type):
        pygame.sprite.Sprite.__init__(self)
        self.type = enemy_type
        self.font = pygame.font.Font("assets/font/Silver.ttf", 36)
        self.image = self.font.render(
            f"T moche",
            False,
            (255, 0, 0),
        )
        self.rect = self.image.get_rect()
        self.rect.bottom = 600
        self.rect.left = 1280

    def update(self, vel):
        self.rect.left -= vel
        if self.rect.right <= 0:
            self.kill()
