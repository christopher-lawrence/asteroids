import random

import pygame

from circleshape import CircleShape
from constants import COLOR_WHITE, ASTEROID_MIN_RADIUS


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
        # forward = pygame.Vector2(0, 1)
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        self.spawn(random_angle)
        self.spawn(-random_angle)

    def spawn(self, angle):
        vector = self.velocity.rotate(angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(
            self.position.x, self.position.y, radius
        )
        asteroid.velocity = vector * 1.2
