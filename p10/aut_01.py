'''
-------------------------------------------------------------------------------
description: load test cases from a CSV file.

usage:  $ python aut_01.py -v


references:
    https://eli.thegreenplace.net/2014/04/02/dynamically-generating-python-test-cases
    https://chrisalbon.com/python/data_wrangling/pandas_dataframe_importing_csv/
-------------------------------------------------------------------------------
'''

# import my code library
import p10

import pandas as pd
import numpy as np
import unittest

class DynamicClassBase(unittest.TestCase):
    longMessage = True


def make_test_function(description, expected_result, param_s, param_p ):
    def test(self):

        # convert data type for parameters as needed
        s      = str( param_s )
        p      = str( param_p )

        sol    = p10.Solution()
        result = sol.isMatch(s, p)
        self.assertEqual( bool(expected_result), result, description)
    return test


if __name__ == '__main__':
    df = pd.read_csv('tc_01.csv')
    #print( df )


    for index, row in df.iterrows():
        #print ( '{} {} {}'.format( row[ 'ID' ], row[ 'description' ], row[ 'expected_result' ] ) )
        test_func = make_test_function( row[ 'description' ], row[ 'expected_result' ],
                                        row[ 'param_s' ],
                                        row[ 'param_p' ],
                                        )

        klassname = 'Test_{0}'.format( row[ 'ID' ] )
        globals()[klassname] = type(klassname,
                                   (DynamicClassBase,),
                                   {'test_gen_{0}'.format( row[ 'ID' ] ): test_func})


    unittest.main( verbosity= 2)