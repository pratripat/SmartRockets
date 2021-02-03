from globals import *
from population import Population

def main():
    population = Population()
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        population.run()
        pygame.draw.circle(screen, white, (int(target.x), int(target.y)), 10)

        pygame.display.update()

        if population.rockets[0].count == lifespan:
            population.evaluate()
            population.selection()

main()
