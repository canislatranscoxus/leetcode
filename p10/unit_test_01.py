import unittest
from unittest import TestCase
import p10

class unit_test_01( TestCase ):

    # TODO: fix this bug

    def test_case_00(self):
        sol = p10.Solution()
        s   = ''
        p   = 'bab'
        res = sol.isMatch( s, p )
        print( '{} -- {}, is Match: {}'.format( s, p, res ) )
        self.assertEqual( res, False, msg = 'this is NOT match' )

    '''
    def test_case_01(self):
        sol = p10.Solution()
        s   = 'aa'
        p   = 'a'
        res = sol.isMatch( s, p )
        print( '{} -- {}, is Match: {}'.format( s, p, res ) )
        self.assertEqual( res, False, msg = 'this is NOT match' )

    def test_case_02(self):
        sol = p10.Solution()
        s   = 'aa'
        p   = 'aa'
        res = sol.isMatch( s, p )
        print( '{} -- {}, is Match: {}'.format( s, p, res ) )
        self.assertEqual( res, True, msg = 'this is match' )

    def test_case_03(self):
        sol = p10.Solution()
        s   = 'aaa'
        p   = 'aa'
        res = sol.isMatch( s, p )
        print( '{} -- {}, is Match: {}'.format( s, p, res ) )
        self.assertEqual( res, False, msg = 'this is Not match' )

    def test_case_04(self):
        sol = p10.Solution()
        s   = 'aa'
        p   = 'a*'
        res = sol.isMatch( s, p )
        print( '{} -- {}, is Match: {}'.format( s, p, res ) )
        self.assertEqual( res, True, msg = 'this is match' )

    def test_case_05(self):
        sol = p10.Solution()
        s   = 'aa'
        p   = '.*'
        res = sol.isMatch( s, p )
        print( '{} -- {}, is Match: {}'.format( s, p, res ) )
        self.assertEqual( res, True, msg = 'this is match' )

    def test_case_06(self):
        sol = p10.Solution()
        s   = 'ab'
        p   = '.*'
        res = sol.isMatch( s, p )
        print( '{} -- {}, is Match: {}'.format( s, p, res ) )
        self.assertEqual( res, True, msg = 'this is match' )
    

    def test_case_07(self):
        sol = p10.Solution()
        s   = 'aab'
        p   = 'c*a*b*'
        res = sol.isMatch( s, p )
        print( '{} -- {}, is Match: {}'.format( s, p, res ) )
        self.assertEqual( res, True, msg = 'this is match' )
    '''

if __name__ == '__main__':
    unittest.main()
