from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
           super().__init__(x,y,radius)

    def draw(self,screen):
        return pygame.draw.circle(screen,(255,255,255),(self.position.x, self.position.y),self.radius,2)
    
    def update(self, dt):
         self.position.x += self.velocity.x * dt
         self.position.y += self.velocity.y *dt

    def split(self):
         self.kill()
         if self.radius <= ASTEROID_MIN_RADIUS:
              return
         else:
              rand_angle = random.uniform(20, 50)
              new_vector1 = (self.velocity.rotate(rand_angle)) * 1.2
              new_vector2 = (self.velocity.rotate(-rand_angle)) * 1.2
              new_radius = (self.radius - ASTEROID_MIN_RADIUS)
              asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
              asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
              asteroid1.velocity = new_vector1
              asteroid2.velocity = new_vector2

