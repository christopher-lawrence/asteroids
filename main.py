import sys
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, COLOR_BLACK
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(x, y, "one")
    AsteroidField()
    # Asteroid(x=SCREEN_WIDTH / 3, y=SCREEN_HEIGHT / 2, radius=40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(COLOR_BLACK)
        # limit the fps to 60
        dt = clock.tick(60) / 1000

        for update in updatable:
            update.update(dt)
        for draw in drawable:
            draw.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()


if __name__ == "__main__":
    main()
