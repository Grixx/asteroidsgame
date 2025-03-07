import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        random_angle = random.uniform(20, 50)
        speed = random._inst
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            new2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            new1.velocity = self.velocity.rotate(-random_angle) * 1.2
            new2.velocity = self.velocity.rotate(random_angle) * 1.2