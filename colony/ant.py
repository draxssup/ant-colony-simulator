import random


class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.carrying_food = False

    def move(self, environment):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Up, down, right, left
        random.shuffle(directions)  # Introduce randomness

        best_dir = None
        best_pheromone = -1

        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < environment.width and 0 <= ny < environment.height:
                pheromone_level = environment.pheromones[ny, nx]
                if pheromone_level > best_pheromone:
                    best_pheromone = pheromone_level
                    best_dir = (dx, dy)

        # 80% chance follow best pheromone, 20% explore randomly
        if best_dir and random.random() < 0.8:
            dx, dy = best_dir
        else:
            dx, dy = random.choice(directions)

        # Update position safely
        new_x = max(0, min(environment.width - 1, self.x + dx))
        new_y = max(0, min(environment.height - 1, self.y + dy))

        self.x = new_x
        self.y = new_y

        # Pickup/drop food
        if not self.carrying_food and (self.y, self.x) == environment.food:
            self.carrying_food = True
        elif self.carrying_food and (self.y, self.x) == environment.nest:
            self.carrying_food = False

        # Drop pheromone while returning with food
        if self.carrying_food:
            environment.pheromones[self.y, self.x] += 1.0
