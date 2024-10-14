import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.surface.Surface):
        pass

    def update(self, dt: int):
        pass

    def collision(self, circle) -> bool:
        distance = self.position.distance_to(circle.position)

        return distance <= self.radius + circle.radius
