import pygame
from pygame import time


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player_run = pygame.image.load("assets/image/player_run.png")
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.rect.bottom = 600
        self.index = 0
        self.is_jumping = False
        self.vel_y = 0
        self.time_air = 0
        self.jump_sound = pygame.mixer.Sound("assets/sound/jump.wav")

    def update(self, dt):
        self.handle_event()
        if self.index >= 4:
            self.index = 0

        self.image = self.get_image(int(self.index), 0)
        self.index += 1 * (dt / 100)
        self.vel_y = 5 * (dt / 10)
        if self.is_jumping:
            if self.time_air > 0.5:
                self.rect.bottom += self.vel_y
            else:
                self.rect.bottom -= self.vel_y
                self.time_air += dt / 1000
            if self.rect.bottom >= 600:
                self.is_jumping = 0
                self.rect.bottom = 600
                self.time_air = 0

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.time_air = 0
            self.jump_sound.play()

    def get_image(self, x: int, y: int):
        image = pygame.Surface((48, 48))
        image.blit(self.player_run, (0, 0), (x * 48, y * 48, 48, 48))
        image.set_colorkey((0, 0, 0))
        image = pygame.transform.scale(image, (48 * 2, 48 * 2))
        return image

    def say(self, message: str):
        pass

    def handle_event(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.jump()
