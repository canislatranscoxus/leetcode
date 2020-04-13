import math
import random

import sys


from GA_individual import GA_individual
from GA_params     import GA_params

class GA:
    population          = []
    params              = GA_params()

    def create_rnd_individual(self):
        individual = GA_individual()
        return individual

    def calculate_fitness(self, individual ):
        return 0

    def create_population(self):
        for i in range( 0, self.params.max_population_size ):
            individual            = self.create_rnd_individual()
            individual.generation = 0
            individual.active     = True
            #self.mutate_chromosome( individual )
            self.calculate_fitness( individual )
            self.population.append( individual )

    def sort_population(self):
        self.population = sorted( self.population, key = lambda i: i.fitness )

    def select_parents(self):
        '''
        return the 4 most fittest individuals from population.
        :return:
        '''
        parents = self.population[ 0 : self.params.parents_pool ]
        return parents

    def crossover(self, mama, papa ):
        '''
        Crossover: Create new offspring program(s) for the new population
                   by recombining randomly chosen parts from two selected programs.
        :param mama:
        :param papa:
        :return:
        '''
        try:
            pivot      = random.randrange( 0, self.params.chromosome_size )
            chromosome = mama.chromosome[ 0: pivot ] + papa.chromosome[ pivot : ]
            offspring  = GA_individual()
            offspring.chromosome = chromosome
            return offspring
        except:
            error_msg = sys.exc_info()[0]
            print( 'GA.crossover(), error: {}'.format( error_msg ) )
            raise



    def mate_parents(self, parents, generation= 0 ):
        '''mama      = parents[ 0 ]
        papa      = parents[ 1 ]
        offspring = self.crossover(mama, papa)
        return offspring'''

        try:
            for mama, papa in zip( parents[ 0::2 ], parents[ 1::2 ] ):
                offspring            = self.crossover( mama, papa )
                offspring.generation = generation
                self.calculate_fitness( offspring )
                self.population.append( offspring )

        except:
            error_msg = sys.exc_info()[0]
            print( 'GA.mate_parents(), error: {}'.format( error_msg ) )
            raise


    def mutate_chromosome(self, individual ):

        for i in range( 0, 2 ):
            index = int( random.randrange( 0, self.params.chromosome_size, 1 ) )

            c     = individual.chromosome[ index ]
            m     = int( random.randrange( -1, 2, 1 ) )

            value = c + m
            value = math.fabs( value )
            if  value > self.params.chromosome_size:
                value = self.params.chromosome_size

            individual.chromosome[ index ] = value


    def reproduce(self):
            '''
            Reproduction: Copy the selected individual program to the new population.
            ( delete the less fittest individuals ).
            :return:
            '''
            self.sort_population()
            start = len( self.population ) - 1
            stop  = self.params.max_population_size - 1
            for i in range( start, stop, -1 ):
                del self.population[ i ]


    def print_population(self):
        print( 'fitness     i.generation    i.chromosome' )
        print( '-------     ------------    ------------' )

        for i in self.population:
            print( '{}  {}  {}'.format( i.fitness, i.generation, i.chromosome  ) )


    def run( self ):
        self.create_population()

        g = 0
        for g in range( 0, self.params.max_generations + 1 ):
            #print( 'GA.run(), generation: {}'.format( g ) )
            self.sort_population()
            parents              = self.select_parents()
            self.mate_parents( parents, generation = g )
            self.reproduce()

        self.params.last_generation = g
        self.print_population()


    def __init__(self, params ):
        self.params = params