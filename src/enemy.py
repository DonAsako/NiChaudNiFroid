import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type):
        pygame.sprite.Sprite.__init__(self)
        self.type = enemy_type
        self.size = (84, 9) if enemy_type else (68, 9)
        self.image_sheets = [
            "assets/image/fireball.png",
            "assets/image/iceball.png",
        ]
        self.image_sheet = pygame.image.load(
            self.image_sheets[self.type]
        ).convert_alpha()
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.rect.bottom = 550 if self.type == 1 else 480
        self.rect.left = 1280
        self.index = 0

    def update(self, vel, dt):
        self.rect.left -= vel
        if self.rect.right <= 0:
            self.kill()
        self.index += dt / 100
        if self.index >= 10:
            self.index = 0
        self.image = self.get_image(int(self.index), 0)

    def get_image(self, x: int, y: int):
        image = pygame.Surface(self.size)
        print(self.size)
        width, height = self.size
        image.blit(
            self.image_sheet,
            (0, 0),
            (x * width, y * height, width, height),
        )
        image.set_colorkey((0, 0, 0))
        image = pygame.transform.scale(image, (84 * 1.5, 9 * 1.5))
        return image
