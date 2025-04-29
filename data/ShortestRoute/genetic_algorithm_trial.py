import numpy as np
import pandas as pd
from mpi4py import MPI

# Load the distance matrix
distance_matrix = pd.read_csv('city_distances.csv').to_numpy()

# Parameters
num_nodes = distance_matrix.shape[0]
population_size = 10000
num_tournaments = 4  # Number of tournaments to run
mutation_rate = 0.1
num_generations = 200
infeasible_penalty = 1e6  # Penalty for infeasible routes
stagnation_limit = 5  # Number of generations without improvement before regeneration

# Create MPI communicator
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Generate initial population: each individual is a route starting at node 0
np.random.seed(42)  # For reproducibility
population = generate_unique_population(population_size, num_nodes)

# Initialize variables for tracking stagnation
best_calculate_fitness = int(1e6)
stagnation_counter = 0

# Main GA loop
for generation in range(num_generations):
    # Distribute the population to all processes
    chunk_size = len(population) // size
    start_idx = rank * chunk_size
    end_idx = (rank + 1) * chunk_size if rank != size - 1 else len(population)
    local_population = population[start_idx:end_idx]

    # Evaluate fitness for the local portion of the population
    local_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in local_population])

    # Gather the fitness values from all processes
    all_fitness_values = comm.gather(local_fitness_values, root=0)

    if rank == 0:
        # Flatten the list of fitness values
        all_fitness_values = np.concatenate(all_fitness_values)

        # Print fitness values for debugging
        print(f"Generation {generation}: Fitness Values: {all_fitness_values}")

        # Check for stagnation
        current_best_calculate_fitness = np.min(all_fitness_values)
        if current_best_calculate_fitness < best_calculate_fitness:
            best_calculate_fitness = current_best_calculate_fitness
            stagnation_counter = 0
        else:
            stagnation_counter += 1

        # Regenerate population if stagnation limit is reached, keeping the best individual
        if stagnation_counter >= stagnation_limit:
            print(f"Regenerating population at generation {generation} due to stagnation")
            best_individual = population[np.argmin(all_fitness_values)]
            population = generate_unique_population(population_size - 1, num_nodes)
            population.append(best_individual)
            stagnation_counter = 0
            continue  # Skip the rest of the loop for this generation

        # Selection, crossover, and mutation
        selected = select_in_tournament(population, all_fitness_values)
        offspring = []
        for i in range(0, len(selected), 2):
            parent1, parent2 = selected[i], selected[i + 1]
            route1 = order_crossover(parent1[1:], parent2[1:])
            offspring.append([0] + route1)
        mutated_offspring = [mutate(route, mutation_rate) for route in offspring]

        # Replace the individuals that lost in the tournaments with the new offspring
        for i, idx in enumerate(np.argsort(all_fitness_values)[::-1][:len(mutated_offspring)]):
            population[idx] = mutated_offspring[i]

        # Ensure population uniqueness
        unique_population = set(tuple(ind) for ind in population)
        while len(unique_population) < population_size:
            individual = [0] + list(np.random.permutation(np.arange(1, num_nodes)))
            unique_population.add(tuple(individual))
        population = [list(individual) for individual in unique_population]

        # Print best fitness
        print(f"Generation {generation}: Best calculate_fitness = {current_best_calculate_fitness}")

# Update calculate_fitness_values for the final population
all_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in population])

# Output the best solution
best_idx = np.argmin(all_fitness_values)
best_solution = population[best_idx]
print("Best Solution:", best_solution)
print("Total Distance:", calculate_fitness(best_solution, distance_matrix))
