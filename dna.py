from globals import *
import random

class DNA:
    def __init__(self, genes=[]):
        self.initialize_genes(genes)

    def initialize_genes(self, genes):
        if len(genes) == 0:
            self.genes = []

            for i in range(lifespan):
                self.genes.append(self.random_velocity())
        else:
            self.genes = genes

    @staticmethod
    def random_velocity():
        magnitude = 0.1
        return pygame.math.Vector2(random.uniform(-magnitude, magnitude), random.uniform(-magnitude, magnitude))

    def crossover(self, other):
        new_genes = []
        mid = random.randrange(0, len(self.genes))

        for i in range(len(self.genes)):
            if i > mid: new_genes.append(self.genes[i])
            else: new_genes.append(other.genes[i])

        return DNA(new_genes)
