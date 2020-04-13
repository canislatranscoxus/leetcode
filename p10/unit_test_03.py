'''
test GA_p10_seq.py
'''

import unittest
from   unittest      import TestCase
from   GA_individual import GA_individual
from   GA_params     import GA_params
from   GA_p10        import GA_p10

class unit_test_03( TestCase ):

    '''
    def test_case_01(self):
        params         = GA_params()
        params.s       = 'aaaabcxyzef'
        params.s_size  = len( params.s )
        params.pattern = 'a*bc.*ef'

        ga =  GA_p10( params )
        ga.create_population()
        ga.print_population()

        population_size = len( ga.population )
        print( 'population size {}'.format( population_size ) )
        self.assertEqual( params.max_population_size, population_size, msg = 'population size' )


    def test_case_02(self):
        params         = GA_params()
        params.s       = 'aaaabcxyzef'
        params.s_size  = len( params.s )
        params.pattern = 'a*bc.*ef'

        individual = GA_individual()
        individual.chromosome = [ 4, 2, 3, 2 ]
        ga =  GA_p10( params )
        fitness = ga.calculate_fitness( individual )
        ga.run()

        print( 'fitness {}'.format( fitness ) )
        self.assertEqual( 0, 0, msg = 'check fitness' )
    '''

    def test_case_06(self):
        params         = GA_params()
        params.s       = 'aaaabcxyzef'
        params.s_size  = len( params.s )
        params.pattern = 'a*bc.*ef'

        ga =  GA_p10( params )
        ga.run()

        print( 'population size {}'.format( len( ga.population ) ) )
        self.assertEqual( params.max_generations, params.last_generation, msg = 'run generations' )





if __name__ == '__main__':
    unittest.main( verbosity = 2 )
