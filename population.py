from globals import *
from rocket import Rocket
from dna import DNA
import random

class Population:
    def __init__(self):
        self.population_size = 25
        self.mating_pool = []
        self.initialize_population()

    def initialize_population(self):
        self.rockets = []

        for i in range(self.population_size):
            self.rockets.append(Rocket())

    def run(self):
        for rocket in self.rockets:
            rocket.update()
            rocket.show()

    def evaluate(self):
        maxfitness = 0

        for rocket in self.rockets:
            rocket.calculate_fitness()
            if rocket.fitness > maxfitness:
                maxfitness = rocket.fitness

        for rocket in self.rockets:
            rocket.fitness /= maxfitness

        for rocket in self.rockets:
            n = rocket.fitness * 100

            for i in range(int(n)):
                self.mating_pool.append(rocket)

    def selection(self):
        new_rockets = []

        for i in range(len(self.rockets)):
            dna1 = random.choice(self.mating_pool).dna
            dna2 = random.choice(self.mating_pool).dna
            dna = dna1.crossover(dna2)
            new_rockets.append(Rocket(dna))

        self.rockets = new_rockets
