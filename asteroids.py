import pygame

from circleshape import CircleShape
from constants import COLOR_WHITE


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

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
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * 1 * dt
