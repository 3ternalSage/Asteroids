import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("#000000")
        for object in updatable:
            object.update(dt)
        
        for object in asteroids:
            if object.collision_with(player):
                print("Game over!")
                exit()
            for shot in shots:
                if object.collision_with(shot):
                    object.kill()
        
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()