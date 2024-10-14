import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS, COLOR_WHITE


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color=COLOR_WHITE,
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.velocity * dt
