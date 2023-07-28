import random

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def generate_population(num_chromosomes, chromosome_length):
    population = []
    for _ in range(num_chromosomes):
        chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        population.append(chromosome)
    return population


def fitness(chromosome, items, knapsack_capacity):
    total_value = 0
    total_weight = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_value += items[i].value
            total_weight += items[i].weight
    if total_weight > knapsack_capacity:
        return 0
    else:
        return total_value

def selection(population, items, knapsack_capacity):
    parents = []
    for _ in range(2):
        tournament = random.sample(population, 5)
        best_chromosome = max(tournament, key=lambda c: fitness(c, items, knapsack_capacity))
        parents.append(best_chromosome)
    return parents

def crossover(parents):
    crossover_point = random.randint(1, len(parents[0])-1)
    child1 = parents[0][:crossover_point] + parents[1][crossover_point:]
    child2 = parents[1][:crossover_point] + parents[0][crossover_point:]
    return child1, child2

def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # Flip the bit
    return chromosome

def genetic_algorithm(items, knapsack_capacity, num_generations, population_size, mutation_rate):
    chromosome_length = len(items)
    population = generate_population(population_size, chromosome_length)

    for _ in range(num_generations):
        new_population = []
        for _ in range(population_size // 2):
            parents = selection(population, items, knapsack_capacity)
            print(_,parents)
            offspring1, offspring2 = crossover(parents)
            offspring1 = mutate(offspring1, mutation_rate)
            offspring2 = mutate(offspring2, mutation_rate)
            new_population.extend([offspring1, offspring2])
        population = new_population

    best_chromosome = max(population, key=lambda c: fitness(c, items, knapsack_capacity))
    best_value = fitness(best_chromosome, items, knapsack_capacity)
    return best_chromosome, best_value

# Example usage: weight , value
items_dataset1 = [Item(5, 10), Item(2, 4), Item(8, 15), Item(1, 3), Item(4, 8)]
items_dataset2 = [Item(3, 7), Item(2, 5), Item(4, 10), Item(5, 12), Item(6, 14)]

knapsack_capacity = 10
num_generations = 100
population_size = 50
mutation_rate = 0.01

best_chromosome, best_value = genetic_algorithm(items_dataset1, knapsack_capacity, num_generations, population_size, mutation_rate)
print("Dataset 1 - Best Chromosome:", best_chromosome)
print("Dataset 1 - Best Value:", best_value)

best_chromosome, best_value = genetic_algorithm(items_dataset2, knapsack_capacity, num_generations, population_size, mutation_rate)
print("Dataset 2 - Best Chromosome:", best_chromosome)
print("Dataset 2 - Best Value:", best_value)
