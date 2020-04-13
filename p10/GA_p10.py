import math
import random

from p10_seq       import Solution
from GA            import GA
from GA_individual import GA_individual
from GA_params     import GA_params



class GA_p10( GA ):
    # useful utilities
    p10                 = Solution()

    def create_rnd_individual(self):
        individual = GA_individual()
        individual.chromosome = []
        indexes    = random.sample( range(0, self.params.s_size ), self.params.chromosome_size )
        previous   = 0
        for i in indexes:
            if len( individual.chromosome ) == 0:
                individual.chromosome.append( i )
            else:
                individual.chromosome.append( int( math.fabs( i - previous ) ) )

            previous = i

        #print( 'individual.chromosome {}'.format( individual.chromosome ) )
        return individual

    def calculate_fitness(self, individual ):
        '''
        calculate the fitness of one chromosome. The smallest fitness (error) is better.
        :param chromosome:
        :return: a float from 0.0 to 1.0
        '''
        f1 = self.p10.failed_matches( self.params.s, individual.chromosome, self.params.subpatterns_seq )
        f2 =  math.fabs( self.params.chromosome_size - sum( individual.chromosome )  ) / 10000.0000
        fitness = f1 + f2
        individual.fitness = fitness

    def __init__(self, params ):
        self.params = params

        seq = self.p10.get_seq     ( self.params.pattern )
        seq = self.p10.simplify_seq( seq )
        self.params.subpatterns_seq = seq
