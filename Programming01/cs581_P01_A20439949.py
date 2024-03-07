# Tania Soutonglang A20439949
# Programming Assignment 1
# CS 581-01 Spring 2024
import sys
import csv
import random
import math
import copy
import time

# get the state info (the state label and cartesian coordinates)
def read_file(filename):
    try:
        file = open(filename, "r")
        state_data = list(csv.reader(file, delimiter=","))        
        init_state = state_data[0]

        return init_state, state_data    
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

# define cost function
def cost(solution):
    total_cost = 0
    for i in range(len(solution) - 1):
        x1, y1 = float(solution[i][1]), float(solution[i][2])
        x2, y2 = float(solution[i+1][1]), float(solution[i+1][2])
        total_cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    return total_cost

# implement 2-edge swap on current state and return the new state
def two_edge_swap(solution):
    # randomly select two edges to swap
    index1, index2 = random.sample(range(len(solution)), 2)
    solution[index1], solution[index2] = solution[index2], solution[index1]

    return solution

# calculate the temp for the current iteration
def exponential_schedule(init_temp, alpha, iteration):
    current_temp = init_temp * math.exp(-alpha * iteration)
    return current_temp

def simulated_annealing(init_sol, init_temp, alpha):
    solution = init_sol
    current_cost = cost(init_sol)
    temp = init_temp
    iterations = 0
    start_time = time.perf_counter()

    while temp > 0:
        new_solution = two_edge_swap(solution)
        new_cost = cost(new_solution)

        # calculate the change in cost
        delta_cost = new_cost - current_cost

        # If the new state is better, always accept it
        if delta_cost < 0:
            solution = new_solution
            current_cost = new_cost

        # If the new state is worse, accept it with a certain probability
        else:
            probability = math.exp(-delta_cost / temp)
            if random.uniform(0, 1) < probability:
                solution = new_solution
                current_cost = new_cost

        temp = exponential_schedule(temp, alpha, iterations)
        iterations += 1
    
    end_time = time.perf_counter()

    return solution, current_cost, iterations, end_time

# define the fitness function based on the cost of the Hamiltonian cycle
def fitness_function(individual):
    pass

# perform Roulette Wheel selection and return selected individuals
def roulette_wheel_selection(population, fitness_values):
    pass

# perform 2-point crossover on two parents and return the resulting offspring
def two_point_crossover(parent1, parent2, crossover_points):
    pass

# perform mutation on an individual with a given probability
def mutation(individual, mutation_probability):
    pass

def genetic_algorithm(population_size, crossover_points, mutation_probability, termination_condition):
    pass
    
# parse command line arguments
if (len(sys.argv) != 5):
    print('ERROR: Not enough or too many input arguments.')
    exit()

filename = sys.argv[1]
init_state, state_data = read_file(filename)
init_sol = state_data.copy()

# 1 – Simulated Annealing,
# 2 – Genetic Algorithm
algo = sys.argv[2]

# Simulated Annealing: P1 is the initial temperature T value,
# Genetic Algorithm: P1 is the number of iterations K,
p1 = float(sys.argv[3])

# Simulated Annealing: P2 is the alpha parameter for the temperature cooling schedule
# Genetic Algorithm: P2 is the mutation probability Pm value
p2 = float(sys.argv[4])

if algo == '1':
    # simulated_annealing(state_data, init_state, init_temp, alpha)
    solution, cost, iterations, exe_time = simulated_annealing(init_sol, p1, p2)
    
    print(f"""Soutonglang, Tania, A20439949 solution:
          Initial state: {init_state}

          Simulated Annealing:
          Command Line Parameters: {algo}, {p1}, {p2}
          Initial solution: {state_data}
          Final solution: {solution}
          Number of iterations: {iterations}
          Execution time: {exe_time}
          Complete path cost: {cost}
          """)
elif algo == '2':
    result = genetic_algorithm()

    print(f"""Soutonglang, Tania, A20439949 solution:
          Initial state: {init_state}

          Genetic Algorithm:
          Command Line Parameters: {algo}, {p1}, {p2}
          Initial solution: LABEL1, LABEL2, LABEL3, …, LABELN-1, LABELN
          Final solution: LABEL1, LABEL2, LABEL3, …, LABELN-1, LABELN
          Number of iterations: {iterations}
          Execution time: 
          Complete path cost: 
          """)
else:
    print("ERROR: Invalid argument.")