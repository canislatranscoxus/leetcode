import unittest
from unittest import TestCase
import p09

class unit_test_01( TestCase ):

    def test_case_01(self):
        sol = p09.Solution()
        a1  = 'abccba'
        res = sol.isPalindrome( a1 )
        print( '{} is palindrome: {}'.format( a1, res ) )
        self.assertEqual( res, True, msg = 'this is palindrome' )


    def test_case_02(self):
        sol = p09.Solution()
        a1  = 'xyz_O_zyx'
        res = sol.isPalindrome( a1 )
        print( '{} is palindrome: {}'.format( a1, res ) )
        self.assertEqual( res, True, msg = 'this is palindrome' )


if __name__ == '__main__':
    unittest.main()
