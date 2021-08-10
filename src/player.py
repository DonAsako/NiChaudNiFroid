import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.player_jump = pygame.image.load("assets/image/player_jump.png")
        self.player_run = pygame.image.load("assets/image/player_run.png")
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.rect.bottom = 600
        self.index = 0

    def update(self, dt):
        if self.index >= 4:
            self.index = 0

        self.image = self.get_image(int(self.index), 0)
        self.index += 1 * (dt / 100)
        print(int(self.index))

    def get_image(self, x: int, y: int):
        image = pygame.Surface((48, 48))
        image.blit(self.player_run, (0, 0), (x * 48, y * 48, 48, 48))
        image.set_colorkey((0, 0, 0))
        image = pygame.transform.scale(image, (48 * 2, 48 * 2))
        return image

    def say(self, message: str):
        pass
