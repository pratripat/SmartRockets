from globals import *
from dna import DNA
import math

class Rocket:
    def __init__(self, dna=None):
        self.position = pygame.math.Vector2(width/2, height/2)
        self.velocity = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()

        if dna == None:
            self.dna = DNA()
        else:
            self.dna = dna

        self.n = 3
        self.r = 10
        self.fitness = 0
        self.count = 0

        self.calculate_angle()
        self.re_calculate_points()

    def calculate_angle(self):
        #Calculating angle according to the velocity
        self.angle = math.radians(pygame.math.Vector2().angle_to(self.velocity))

    def create_points(self):
        #Creating the points of the vehicle
        a = self.angle
        points = []

        for i in range(self.n):
            v = pygame.math.Vector2(math.cos(a), math.sin(a))

            if i == 0: v *= self.r * 1.5
            else: v *= self.r

            v += self.position

            points.append(v)

            a += math.radians(360 / self.n)

        return points

    def re_calculate_points(self):
        #Just creating the points
        self.points = self.create_points()

    def apply_force(self, force):
        self.acceleration += force

    def show(self):
        pygame.draw.polygon(screen, white, self.points)

    def update(self):
        self.apply_force(self.dna.genes[self.count])

        self.position += self.velocity
        self.velocity += self.acceleration
        self.acceleration.update()

        self.calculate_angle()
        self.re_calculate_points()
        self.count += 1

        if self.position.distance_to(target) < self.r:
            self.position = pygame.math.Vector2(*target)
            self.fitness *= 10

    def calculate_fitness(self):
        d = self.position.distance_to(target)

        if d != 0: self.fitness = 1/d
        else: self.fitness = width
