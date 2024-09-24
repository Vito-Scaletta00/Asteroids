import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots,updatable, drawable)
    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ###Allows us to quit with the exit button
                return
        pygame.Surface.fill(screen,(0,0,0)) #makes screen black
        dt = gameClock.tick(60) / 1000  #pauses the loops it's contained in until 1/60th of a second has passed, 
                                        #then returns the delta time and divides it by 1000 (converts milliseonds to seconds) 
                                        # and assigns this to the dt variable
        for item in drawable:
            item.draw(screen)
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.collision(player):
                print ("Game Over!")
                sys.exit()

        pygame.display.flip()










if __name__ == "__main__":
    main()