import pygame
from pygame import sprite
from src.settings import Settings
from src.scenes.room import RoomScene
from src.scenes.menu import MenuScene
from src.scenes.gameover import GameOverScene
from src.scenes.settings import SettingsScene
from src.scenes.scores import ScoresScene


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720), 8)
        pygame.display.set_caption("Ni Chaud Ni Froid")
        self.current_scene = None
        self.is_running = False
        self.clock = pygame.time.Clock()
        self.debug_font = pygame.font.Font("assets/font/Silver.ttf", 24)
        self.dt = None
        self.settings = Settings()
        self.score = 0
        self.score_filename = "scores.txt"
        self.events = []

    def run(self):
        self.is_running = True
        self.current_scene = MenuScene(self)
        while self.is_running:
            self.loop()

    def loop(self):
        self.dt = self.clock.tick(120)
        self.handle_event()

        # Current_scene
        self.current_scene.handle_event()
        self.current_scene.update()
        self.current_scene.draw()

        # Fps
        if self.settings.get_setting("debug", "show_framerate"):
            text_fps = self.debug_font.render(
                f"FPS : {self.clock.get_fps():2.0f}",
                False,
                (255, 0, 0),
            )

            text_rect = text_fps.get_rect()
            text_rect.topleft = (self.screen.get_width() - text_rect.width - 10, 10)
            self.screen.blit(text_fps, text_rect)

        pygame.display.flip()

    def handle_event(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.kill()

    def save_score(self):
        with open(self.score_filename, "a+") as file:
            if self.score > 0:
                file.write(f"{self.score:.0f};")
        self.score = 0

    def kill(self):
        self.save_score()
        self.is_running = False

    def change_scene(self, scene: str):
        pygame.mixer.music.stop()
        if scene == "menu":
            self.current_scene = MenuScene(self)
        elif scene == "room":
            self.current_scene = RoomScene(self)
        elif scene == "game_over":
            self.current_scene = GameOverScene(self)
        elif scene == "settings":
            self.current_scene = SettingsScene(self)
        elif scene == "scores":
            self.current_scene = ScoresScene(self)
