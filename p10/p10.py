'''
-------------------------------------------------------------------------------
10. Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.


'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
1. isMatch("aa","a") → false
2. isMatch("aa","aa") → true
3. isMatch("aaa","aa") → false
4. isMatch("aa", "a*") → true
5. isMatch("aa", ".*") → true
6. isMatch("ab", ".*") → true
7. isMatch("aab", "c*a*b") → true
-------------------------------------------------------------------------------
'''

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str string
        :type p: str pattern
        :rtype: bool
        """
        result = True

        # pattern characters
        c       = ''
        p_previous = ''

        # string s index
        s_i     = 0
        s_len   = len( s )
        i       = 0

        for c in p:
            # if quantifier
            if c == '*':
                if p_previous == '.':
                    return True

                # advance in s until we find a different char
                for i in range( s_i, s_len ):
                    if p_previous != s[ i ]:
                        break
                s_i = i

            else:
                if p_previous == '':
                    #p_previous = c
                    pass

                elif s_i < s_len and p_previous == s[ s_i ]:
                    #p_previous = c
                    s_i += 1
                elif s_i >= s_len:
                    return False

                p_previous = c

        # checking the last char
        if s_i >= s_len and c != '*':
            return False

        if c != '*' and p_previous != s[ s_i ]:
            result = False

        elif s_i < s_len - 1:
            result = False

        return result