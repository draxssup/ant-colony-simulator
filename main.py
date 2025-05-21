from colony.environment import Environment
from colony.ant import Ant


def main():
    env = Environment(width=20, height=20, num_ants=10)
    env.run_simulation(steps=1000)
    print("Max pheromone:", env.pheromones.max())


if __name__ == "__main__":
    main()
