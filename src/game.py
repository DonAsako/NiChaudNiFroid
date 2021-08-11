import pygame
from src.scenes.room import RoomScene
from src.scenes.menu import MenuScene


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.score = 0
        self.scenes = {
            "menu": MenuScene(self),
            "room": RoomScene(self),
        }
        self.current_scene = self.scenes["menu"]
        self.is_running = False
        self.clock = pygame.time.Clock()

        # Music
        pygame.mixer.music.load("assets/sound/music.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.pause()

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

    def goto(self, to_scene: str):
        self.current_scene = self.scenes[to_scene]
        if to_scene == "menu":
            pygame.mixer.music.pause()
        elif to_scene == "room":
            pygame.mixer.music.unpause()
