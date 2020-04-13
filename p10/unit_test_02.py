'''
test p10_seq.py
'''

import unittest
from   unittest import TestCase
import p10_seq

class unit_test_02( TestCase ):

    # TODO: fix this bug

    '''
    def test_case_00(self):
        sol = p10_seq.Solution()
        s   = 'aaaabcxyzef'
        p   = 'a*bc.*ef'
        res = sol.isMatch( s, p )
        print( '{} -- {}, is Match: {}'.format( s, p, res ) )
        self.assertEqual( res, True, msg = 'this is match' )
    '''

    '''
    def test_case_01(self):
        # test simplify sequence.

        sol = p10_seq.Solution()
        s   = 'aaaabcxyzef'
        p   = 'a*bc.*ef'
        seq = sol.get_seq( p )
        ss  = sol.simplify_seq( seq )

        self.assertEqual( len( ss ), 4, msg = 'this is match' )
    

    def test_case_02(self):
        # test satisfy_pattern

        sol = p10_seq.Solution()
        s   = 'aaaa'
        p   = ( 'a', '*' )
        res = sol.s_satisfy_pattern( s, p )
        self.assertEqual( True, res, msg = 'a* is match' )



    def test_case_03(self):
        # test satisfy_pattern

        sol = p10_seq.Solution()
        s   = 'bc'
        p   = ( 'bc', 1 )
        res = sol.s_satisfy_pattern( s, p )
        self.assertEqual( True, res, msg = 'bc is match' )


    def test_case_04(self):
        # test satisfy_pattern

        sol = p10_seq.Solution()
        s   = 'xyz'
        p   = ( '.', '*' )
        res = sol.s_satisfy_pattern( s, p )
        self.assertEqual( True, res, msg = '.* is match' )

    def test_case_05(self):
        # test satisfy_pattern

        sol = p10_seq.Solution()
        s   = 'ef'
        p   = ( 'ef', 1 )
        res = sol.s_satisfy_pattern( s, p )
        self.assertEqual( True, res, msg = 'ef is match' )
        
    
    def test_case_06(self):
        # test satisfy_pattern

        sol      = p10_seq.Solution()
        s        = 'aaaabcxyzef'
        chunks   = [ 4, 2, 3, 2 ]

        p        = 'a*bc.*ef'
        seq      = sol.get_seq(p)
        ss       = sol.simplify_seq(seq)
        res      = sol.failed_matches( s, chunks, ss )

        self.assertEqual( 0.0, res, msg = 'No failed matches' )


    def test_case_07(self):
        # test satisfy_pattern

        sol      = p10_seq.Solution()
        s        = 'aaaabcxyzef'
        chunks   = [ 4, 0, 0, 0 ]

        p        = 'a*bc.*ef'
        seq      = sol.get_seq(p)
        ss       = sol.simplify_seq(seq)
        res      = sol.failed_matches( s, chunks, ss )

        print( 'tc07 - failed matches: {}'.format( res ) )
        self.assertEqual( 0.50, res, msg = 'No failed matches' )
    '''

    def test_case_08(self):
        # test satisfy_pattern

        sol      = p10_seq.Solution()
        s        = 'aaaabcxyzef'
        chunks   = [ 4, 2, 3, 1 ]

        p        = 'a*bc.*ef'
        seq      = sol.get_seq(p)
        ss       = sol.simplify_seq(seq)
        res      = sol.failed_matches( s, chunks, ss )
        print('tc08 - failed matches: {}'.format(res))
        self.assertEqual( 0.25, res, msg = 'No failed matches' )


if __name__ == '__main__':
    unittest.main( verbosity = 2 )
