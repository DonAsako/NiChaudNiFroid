import pygame
from pygame import time


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_sheet = pygame.image.load("assets/image/player_run.png")
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (20, 600)
        self.index = 0
        self.temperature = 0
        # jump
        self.jump_sound = pygame.mixer.Sound("assets/sound/jump.wav")
        self.vel_y = 10
        self.air_time = 0

    def update(self, dt):
        self.handle_event()
        self.animation(dt)
        if self.is_jumping:
            self.jump(dt)

    def jump(self, dt):
        self.air_time += dt / 1000
        if self.air_time < 0.4:
            self.rect.top -= self.vel_y * (dt / 10)
        else:
            self.rect.top += self.vel_y * (dt / 10)

        if self.rect.bottom >= 600:
            self.air_time = 0
            self.rect.bottom = 600
            self.is_jumping = False

    def animation(self, dt):
        if self.index >= 4:
            self.index = 0

        self.image = self.get_image(int(self.index), 0)
        self.index += 1 * (dt / 100)

    def get_image(self, x: int, y: int):
        image = pygame.Surface((48, 48))
        image.blit(self.image_sheet, (0, 0), (x * 48, y * 48, 48, 48))
        image.set_colorkey((0, 0, 0))
        image = pygame.transform.scale(image, (48 * 2, 48 * 2))
        return image

    def handle_event(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.is_jumping = True
