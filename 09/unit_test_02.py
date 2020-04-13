import p09
import unittest
from unittest import TestCase


class unit_test_02( TestCase ):
    num = 10

    def test_case(self ):
        sol = p09.Solution()
        res = sol.isPalindrome( self.num )
        print( '{} is palindrome: {}'.format( self.num, res ) )
        self.assertEqual( res, True, msg = 'this is palindrome' )


def get_suite():
    suite = unittest.TestSuite()
    suite.addTest( 'case_001' )
    suite.addTest( 'case_002' )
    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    suite = get_suite()
    runner.run( suite )

    #unittest.main()