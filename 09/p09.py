'''
9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        middle = len( s ) // 2

        for i in range(0, middle):
            if s[ i ] != s[ -i -1 ]:
                return False

        return True