from abc import ABC, abstractmethod


class Scene(ABC):
    @abstractmethod
    def __init__(self, game):
        self.game = game

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def draw(self):
        ...

    @abstractmethod
    def handle_event(self):
        ...
