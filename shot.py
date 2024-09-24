import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        return pygame.draw.circle(screen,(255,255,255),(self.position.x, self.position.y),SHOT_RADIUS,2)
    def update(self, dt):
         self.position.x += self.velocity.x * dt
         self.position.y += self.velocity.y *dt