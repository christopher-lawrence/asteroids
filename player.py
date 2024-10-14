import pygame

from circleshape import CircleShape
from constants import COLOR_WHITE, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, name):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.name = name

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.surface.Surface):
        triangle = self.triangle()
        pygame.draw.polygon(surface=screen, color=COLOR_WHITE, points=triangle, width=2)

    def rotate(self, dt: int):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        print('shot')
        Shot(self.position.x, self.position.y)