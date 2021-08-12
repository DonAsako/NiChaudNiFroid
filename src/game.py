import pygame
from src.scenes.room import RoomScene
from src.scenes.menu import MenuScene
from src.scenes.gameover import GameOverScene


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Ni Chaud Ni Froid")
        self.current_scene = None
        self.is_running = False
        self.clock = pygame.time.Clock()

    def run(self):
        self.is_running = True
        self.current_scene = MenuScene(self)
        while self.is_running:
            self.loop()

    def loop(self):
        self.dt = self.clock.tick(60)
        self.handle_event()
        self.screen.fill((0, 0, 0))
        self.current_scene.handle_event()
        self.current_scene.update()
        self.current_scene.draw()
        pygame.display.flip()

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.kill()

    def kill(self):
        self.is_running = False

    def change_scene(self, scene: str):
        pygame.mixer.music.stop()
        if scene == "menu":
            self.current_scene = MenuScene(self)
        elif scene == "room":
            self.current_scene = RoomScene(self)
        elif scene == "game_over":
            self.current_scene = GameOverScene(self)
