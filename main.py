import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0
    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ###Allows us to quit with the exit button
                return
        pygame.Surface.fill(screen,(0,0,0)) #makes screen black
        dt = gameClock.tick(60) / 1000  #pauses the loops it's contained in until 1/60th of a second has passed, 
                                        #then returns the delta time and divides it by 1000 (converts milliseonds to seconds) 
                                        # and assigns this to the dt variable
        player.draw(screen)
        pygame.display.flip()










if __name__ == "__main__":
    main()