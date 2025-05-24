# Ant Colony Simulator

This project implements a decentralized ant colony simulation where individual agents forage for food, return it to the nest, and lay pheromone trails to optimize pathfinding over time. The behavior emerges from simple rules, without any centralized coordination or learning model.

## Objective

To explore swarm intelligence using biologically-inspired algorithms and demonstrate how local agent rules can lead to efficient global behavior in dynamic environments.

## Features

- Grid-based 2D environment with nest, food sources, and obstacles
- Ants move using probabilistic decisions based on pheromone levels and environmental cues
- Pheromones evaporate and diffuse over time, creating dynamic, adaptive paths
- Short-term memory to prevent ants from looping or revisiting recent locations
- Modular architecture with separate environment, ant agent, and simulation controller

## Project Structure

- `main.py` – Simulation loop and visualization
- `environment.py` – Grid setup, pheromone handling, and object placement
- `ant.py` – Ant behavior, movement logic, and pheromone interaction

## Visualization

Simulation output is visualized using Matplotlib with real-time updates. Food collection efficiency and trail formation can be observed as ants converge on optimal routes over time.

## Future Extensions

- Multi-nest or competing colony scenarios
- Integration with reinforcement learning for hybrid behavior
- Performance benchmarking across map sizes and obstacle layouts
- Exporting simulation data for analysis or machine learning training
