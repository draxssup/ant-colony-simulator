class Environment:
    def __init__(self, width, height, num_ants):
        self.width = width
        self.height = height
        self.ants = []  # Will add Ants later
        print(f"Environment initialized: {width}x{height} with {num_ants} ants")

    def run_simulation(self, steps):
        for step in range(steps):
            print(f"Step {step + 1}/{steps}")
