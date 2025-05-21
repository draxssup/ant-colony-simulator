import numpy as np
import matplotlib.pyplot as plt
from colony.ant import Ant


class Environment:
    def __init__(self, width, height, num_ants):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.pheromones = np.zeros((height, width), dtype=float)
        self.ants = [Ant(x=width // 2, y=height // 2) for _ in range(num_ants)]
        self.food = (np.random.randint(0, height), np.random.randint(0, width))
        self.nest = (height // 2, width // 2)

        # Set up Matplotlib figure and axis once
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.im = None

    def run_simulation(self, steps):
        plt.ion()
        for step in range(steps):
            self.decay_pheromones()
            for ant in self.ants:
                ant.move(self)
            self.render()
        plt.ioff()
        plt.show()

    def decay_pheromones(self, decay_rate=0.005):
        self.pheromones *= 1 - decay_rate

    def render(self):
        pheromone_map = self.pheromones.copy()

        # Normalize pheromone map for consistent visualization
        max_pheromone = pheromone_map.max()
        if max_pheromone > 0:
            pheromone_map /= max_pheromone

        self.ax.clear()

        # Show pheromones with some transparency for better overlay visibility
        self.ax.imshow(
            pheromone_map,
            cmap="Blues",
            origin="lower",
            alpha=0.8,
            interpolation="nearest",
        )

        # Plot ants on top
        ant_x = [ant.x for ant in self.ants]
        ant_y = [ant.y for ant in self.ants]
        self.ax.scatter(
            ant_x,
            ant_y,
            c="red",
            s=15,
            label="Ants",
            edgecolors="black",
            linewidths=0.5,
        )

        # Plot food and nest with distinct markers
        self.ax.scatter(
            self.food[1],
            self.food[0],
            c="green",
            marker="*",
            s=120,
            label="Food",
            edgecolors="darkgreen",
        )
        self.ax.scatter(
            self.nest[1], self.nest[0], c="black", marker="^", s=80, label="Nest"
        )

        # Clean up axis ticks and labels for cleaner visualization
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.ax.set_title("Ant Colony Simulation - Pheromone Map")
        self.ax.legend(loc="upper right", fontsize="small")

        plt.pause(0.05)
