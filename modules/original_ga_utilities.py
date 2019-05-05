########################################################################################################################
##################################################### Modules ##########################################################
########################################################################################################################
from __future__ import division
import pandas as pd
import numpy as np
from random import randint
import random as rand

########################################################################################################################
##################################################### GA Functions #####################################################
########################################################################################################################

# creates first set of boxes

#check
def initialPopulation(popSize):
    population = []

    for i in range(0, popSize):
        H = randint(1, dY)
        W = randint(1, dX)
        X = randint(1, dX)
        Y = randint(1, dY)
        l = 3
        totalY = Y + H
        totalX = X + W

        while totalX > dX:
            X = X - 4  ## subtracting 1 left the outside of the rect to be displayed outside of the cord space
            totalX = X + W
        while totalY > dY:
            Y = Y - 4
            totalY = Y + H

        population.append(rectCreature(X, Y, H, W, l))

    # display initial population
    # plotRectangles(coorSpace=coorSpace, tBB=tBB, creatures=population)

    return population

# select those to continue in the next generation
def artificialSelection(genRanked, eliteSize):
    print "*" * 100
    selectionResults = []
    df = pd.DataFrame(np.array(genRanked), columns=["Index", "Area", "Distance", "Total"])
    df['cum_sum'] = df.Area.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Area.sum()
    df.head()

    # get all elite (need adjustment here...)
    for i in range(0, eliteSize):
        selectionResults.append(genRanked[i][0])

    # randomly get creatures
    for i in range(0, len(genRanked) - eliteSize):
        pick = 100 * rand.random()
        for i in range(0, len(genRanked)):

            if pick <= df.iat[i, 3]:
                selectionResults.append(genRanked[i][0])
                break

    return selectionResults

# group of those whose genes will be passed on
def matingPool(generation, selectResults):
    pool = []

    # get selected creatures by their index..
    for i in range(0, len(selectResults)):
        index = selectResults[i]
        pool.append(generation[index])

    return pool

# special editing space for child boxes (ie if a child's box would extend beyond the cord space)
def CRISPR(genes):
    dX, dY = genes[0], genes[1]
    X, Y, H, W, l = genes[2][0], genes[2][1], genes[2][2], genes[2][3], genes[2][4]

    totalY = Y + H
    totalX = X + W

    while totalX > dX:
        X = X - 4
        totalX = X + W

    while totalY > dY:
        Y = Y - 4
        totalY = Y + H

    editedGenes = X, Y, H, W, l

    return editedGenes

# breed, exchange of genes
def breed(parent1, parent2, dX, dY):
    # just being explicit
    geneA = parent1[0], parent1[1]
    geneB = parent2[4], parent2[3]

    genes = geneA[0], geneA[1], geneB[0], geneB[1], 5

    # keep boxes from going off the page..
    editedGenes = CRISPR((dX, dY, genes))

    eG = editedGenes
    child = rectCreature(eG[0], eG[1], eG[2], eG[3], eG[4])

    return child

# calls breed function
def breedPopulation(matingpool, eliteSize, dX, dY):
    children = []

    # the elite are passed onto the next generation
    length = len(matingpool) - eliteSize

    # randomize positions..
    pool = rand.sample(matingpool, len(matingpool))

    # keep the elite
    for i in range(0, eliteSize):
        children.append(matingpool[i])

    # do breeding
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool) - i - 1], dX, dY)
        children.append(child)

    return children

# gives a random mutation (new box dims, simple change)
def mutate(individual, mutationRate):

    if (rand.random() < mutationRate):
        # rectCreature(X=11, Y=48, H=1152, W=889, l=3)

        X = randint(1, dX)
        Y = randint(1, dY)
        H = randint(1, dY)
        W = randint(1, dX)
        l = individual[4]
        totalY = Y + H
        totalX = X + W

        while totalX > dX:
            X = X - 4
            totalX = X + W

        while totalY > dY:
            Y = Y - 4
            totalY = Y + H

        individual = rectCreature(X, Y, H, W, l)

    return individual

# performs mutations
def mutatePopulation(children, mutationRate):
    mutatedPop = []

    for individual in range(0, len(children)):
        mutatedIndividual = mutate(children[individual], mutationRate)
        mutatedPop.append(mutatedIndividual)

    return mutatedPop

# creates new generation
def newGeneration(pop, mutationRate, eliteSize, dX, dY):
    # rank intersected areas
    # genRanked = rankAreas(generation=pop, tBB=tBB)
    genRanked = rankDistances(generation=pop, tBB=tBB)
    print "Current Population Size:", len(genRanked)

    # execute artificial process of natural selection
    chosenOnes = artificialSelection(genRanked=genRanked, eliteSize=eliteSize)

    # print "Chosen Ones", len(chosenOnes)
    # Gather parents for breeding
    pool = matingPool(generation=pop, selectResults=chosenOnes)

    # print "Mating pool", len(pool)
    # breed the mating pool to obtain children.. children will take on X,Y and H,W genes from parents
    children = breedPopulation(matingpool=pool, eliteSize=eliteSize, dX=dX, dY=dY)

    # print "Children", len(children)
    # mutations
    nextGeneration = mutatePopulation(children=children, mutationRate=mutationRate)

    return nextGeneration

# runs Genetic algorithm
def geneticAlgorithm(popSize, eliteSize, mutationRate, generations, dX, dY):
    # get a first population or rectangles and their intersection areas
    pop = initialPopulation(popSize=popSize)

    creatures = list()
    print "Initial Population", len(pop)

    for i in range(0, generations):
        print "Computing Generation: {-", i, "-} of", generations, " generations.."
        pop = newGeneration(pop=pop, mutationRate=mutationRate, eliteSize=eliteSize, dX=dX, dY=dY)

        bestRectIndex = rankDistances(pop, tBB)[0][0]
        bestRect = pop[bestRectIndex]
        # print bestRectIndex
        creatures.append(bestRect)
        val = intersectionPercentage(bestRect, tBB)
        # with open("../xtr/example.txt", "a") as f:
        #    f.write(str(val)+ "," + str(i) + '\n')
        #    f.close()

    print "Total Top Creatures:", len(creatures)
    creatures = set(creatures)
    print "Unique Creatures:", len(set(creatures))

    # plotBestRectangles(coorSpace=coorSpace, tBB=tBB, creatures=bestRect)

    plotRectangles(coorSpace=coorSpace, tBB=tBB, creatures=creatures)

    return None