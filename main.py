import pygame

from constants import *
from player import *

def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    time_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    the_player = Player(x, y)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill((1,1,1))

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        delta_time = time_clock.tick(60)

        dt = delta_time

if __name__ == "__main__":
    main()