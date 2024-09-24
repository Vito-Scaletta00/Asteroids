import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen): #handles drawing the player character
        pygame.draw.polygon(screen, (255,255,255),self.triangle(),2)

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision(self,CircleShape): 
        distance = self.position.distance_to(CircleShape.position)
        if distance <= self.radius + CircleShape.radius:            #Detects collision and returns true/false, everything should use this for colliding
            return True
        else:
            return False



