import pygad
import numpy
import time

from joblib.numpy_pickle_utils import xrange

item_names = ['clock', 'painting nature', 'painting portrait', 'radio', 'laptop', 'silver cutlery', 'porcelain cups',
              'bronze statue', 'leather bag', 'vacuum cleaner']
item_values = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
item_weights = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]

# define all possible genes
gene_space = [0, 1]
limit = 25.0

# define the number of genes in a chromosome/solution
num_genes = len(item_weights)


# define the fitness function
# how to grade chromosomes?
def fitness_func(solution, solution_idx):
    SumValue = 0
    SumWeight = 0
    for index, i in enumerate(solution):
        if i == 0:
            continue
        else:
            SumValue += item_values[index]
            SumWeight += item_weights[index]
    if SumWeight > limit:
        return 0
    else:
        return SumValue


fitness_function = fitness_func

# size of the population
sol_per_pop = 10

# part of the population to become parents
num_parents_mating = 5

# how many parents will live with children
keep_parents = 2

# maximal number of generations
num_generations = 50

# type of selection
parent_selection_type = "sss"

# type of crossover
crossover_type = "single_point"

# how should mutation work?
# set the percentage to: round_up(100/num_genes)
mutation_type = "random"
mutation_percent_genes = 10

# initiate the algorithm, gice all the parameters from above


# run the algorithm, it will start the generation cycle
listOfTime = []

for i in range(10):
    start = time.time()
    ga_instance = pygad.GA(gene_space=gene_space,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes,
                           )
    ga_instance.run()
    end = time.time()
    totalTime = end - start
    listOfTime.append(totalTime)


print("Average time: ", numpy.average(listOfTime))

# summary: we return the solution
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

# we can additionaly give the best fitness
prediction = numpy.sum(item_weights * solution)
print("Predicted weight: {prediction}".format(prediction=prediction))
prediction1 = numpy.sum(item_values * solution)
print("Predicted value: {prediction}".format(prediction=prediction1))

# show a plot of the best solution fitness throughout the generations
ga_instance.plot_fitness()
