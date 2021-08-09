import pygame
from src.scenes.room import RoomScene


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((720, 720))
        self.current_scene = RoomScene(self)
        self.is_running = False
        self.clock = pygame.time.Clock()

    def run(self):
        self.is_running = True
        while self.is_running:
            self.loop()

    def loop(self):
        self.dt = self.clock.tick(60)
        self.handle_event()
        self.screen.fill((0, 0, 0))
        self.current_scene.update()
        self.current_scene.draw()
        pygame.display.flip()

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.kill()

    def kill(self):
        self.is_running = False
