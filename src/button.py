from typing import Collection
import pygame


class Button(pygame.sprite.Sprite):
    def __init__(
        self,
        size: Collection,
        position: Collection,
        text: str,
        font: pygame.font.Font,
        color: pygame.Color,
        hover_color: pygame.Color,
        text_color: pygame.Color,
        on_pressed: None,
    ):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.position = position
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.on_pressed = on_pressed
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.image.set_colorkey((0, 0, 0, 0))

        # Button Draw
        pygame.draw.rect(
            self.image,
            color=self.color,
            rect=[0, 0, self.size[0], self.size[1]],
            width=0,
            border_radius=5,
        )

        # Title
        self.title = self.font.render(self.text.upper(), True, self.text_color)
        self.image.blit(
            self.title,
            (
                self.rect.width / 2 - self.title.get_width() / 2,
                self.rect.height / 2 - self.title.get_height() / 2 + 7.5,
            ),
        )

    def update(self, events):
        self.handle_event(events)

    def handle_event(self, events):
        mouse_pos = pygame.mouse.get_pos()
        if (
            self.rect.top < mouse_pos[1] < self.rect.bottom
            and self.rect.left < mouse_pos[0] < self.rect.right
        ):
            self.on_hover()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(3)[0]:
                        self.on_pressed()
        else:
            pygame.draw.rect(
                self.image,
                color=self.color,
                rect=[0, 0, self.size[0], self.size[1]],
                width=0,
                border_radius=5,
            )
        self.image.blit(
            self.title,
            (
                self.rect.width / 2 - self.title.get_width() / 2,
                self.rect.height / 2 - self.title.get_height() / 2 + 7.5,
            ),
        )

    def on_hover(self):
        pygame.draw.rect(
            self.image,
            color=self.hover_color,
            rect=[0, 0, self.size[0], self.size[1]],
            width=0,
            border_radius=5,
        )
