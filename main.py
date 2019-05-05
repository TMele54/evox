# Created by Anthony Mele - 5/4/2019
# TMele54@github

from modules.create_pattern import generate

if __name__ == '__main__':

    # Free text information
    documents=["My ip address has four numbers, each one is connected by a period. The address is 71.127.215.54, it is unique to me, and so there are many like it but this one is mine.",""]
    user_string = "71.127.215.54"

    # population size
    initial_population_size = 1000  # number of individuals we begin with
    generations = 1000  # number of full cycle generatoins
    elite_size = 30  # number of top ranked individuals guaranteed to breed, others subject to randomly not breed
    mutation_rate = 0.15  # probability that offspring will be born with a mutation (adjustment in their regex pattern)

    generate(
        user_string = user_string,
        corpus=documents[0],
        initial_population_size=initial_population_size,
        elite_size=elite_size,
        mutation_rate=mutation_rate,
        generations=generations,

    )