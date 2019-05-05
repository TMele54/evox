from __future__ import division
import pickle
import unicodedata
import random
import re
import random as rand


class eVoX:

    # Initialization
    def __init__(self, s1, document, initial_population_size, elite_size, mutation_rate, generations):
        self.s1 = s1
        self.doc = document
        self.ip_size = initial_population_size
        self.elite_size = elite_size
        self.mutation_rate = mutation_rate
        self.generations = generations


        with open('data/basic_elements.pym', 'rb') as handle:
            data = pickle.load(handle)
        self.beol = data['simple']

    # Measure distance between user example and current individual's chromosome
    def edit_distance(self, result):
        if len(self.s1) > len(result):
            self.s1, individual = result, self.s1

        distances = range(len(self.s1) + 1)
        for i2, c2 in enumerate(result):
            distances_ = [i2 + 1]
            for i1, c1 in enumerate(self.s1):
                if c1 == c2:
                    distances_.append(distances[i1])
                else:
                    distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            distances = distances_
        return distances[-1]

    # Perform Regex to test the output
    def search_document(self, individual):
        rx = re.compile(individual)
        result = "".join(rx.findall(self.doc))
        return result

    # Evaluate the fitness of current individual's search pattern
    def evaluate_individual_fitness(self, individual):
        result = self.search_document(individual)
        distance = self.edit_distance(result)
        bigger = max(len(self.s1), len(individual))
        pct = (bigger - distance) / bigger
        return pct*100

    # Creates individual for different populations
    def spawn_individual(self):
        individual_obj = {"pattern":"", "options":""}

        #escapes = random.choice(self.beol["Escapes"])
        classes = random.choice(self.beol["Classes"])
        #anchors = random.choice(self.beol["Anchors"])
        quants = random.choice(self.beol["Quantifiers"])
        options = random.choice(self.beol["Options"])

        #individual_obj["pattern"] += '/'
        individual_obj["pattern"] += classes
        individual_obj["pattern"] += quants
        #individual_obj["pattern"] += '/'
        individual_obj["options"] = options
        individual = individual_obj["pattern"]+individual_obj["options"]

        return individual

    # Creates first generation of individuals
    def initial_population(self):
        population = []

        for i in range(0, self.ip_size):
            population.append({"index": i, "pattern": self.spawn_individual()})

        return population

    # Evaluate fitness of an entire generation
    def evaluate_generation(self, generation):
        individuals_fitness = []

        for individual in generation:
            individuals_fitness.append({"index": individual["index"], "fitness":self.evaluate_individual_fitness(individual["pattern"])})

        return individuals_fitness

    # Sort and Rank the top performers in a generation and begin breeding
    def rank_individuals(self, performances):
        return ""


