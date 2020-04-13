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

    def get_seq( self, p ):
        '''
        Get the sequence represented in a pattern.
        :param p: (string) this is the pattern.
        :return: a list of tuples. ( character, number_of_times  )
        '''
        seq = []
        size = len( p )
        ch = ''
        n  = 0
        for i in range( 0, size ):
            ch = p[ i ]
            n  = 1

            if ch == '*' or ch == '+':
                continue

            if i+1 >= size :
                pass
            elif p[ i + 1 ] == '*' or p[ i + 1 ] == '+':
                n = p[ i + 1 ]

            t = ( ch, n )
            seq.append( t )

        '''print( 'get_seq...' )
        for i in seq:
            print( i )

        print( 'get_seq... end' )'''

        return seq

    def simplify_seq( self, seq ):
        '''
        simplify a sequence. Take as input a seq, a list of tuples. ( character, number_of_times  )
        :param seq:
        :return: a list of tuples ( string, number_of_times )
        '''
        s2 = []
        updated = True
        size = len( seq )

        t = seq[ 0 ]
        a = ( '', 0 )

        for i in range( 0, size ):
            t = seq[ i ]

            if t[1] == 1:
                # join this two subsequeces ( tuples )
                a = (a[0] + t[0], 1)

            else:
                if  a[1] == 1:
                    s2.append( a )
                    a = ('', 0)
                s2.append( t )

        if a[1] != 0:
            s2.append( a )

        '''print( 'simplify_seq...' )
        for i in s2:
            print( i )
        print('simplify_seq... end')'''

        return s2

    def find_all_rigid_subseq(self, s, seq):
        '''
        find all the ocurrences of each rigid subsequence in the string
        :param seq:
        :return:
        '''


        rigid_ss = []
        size = len( seq )

        for i in range( 0, size ):
            t = seq[ i ]

            if t[ 0 ] == '.' or t[ 1 ] == '*' or t[ 1 ] == '+':
                continue

            subseq = []

            p = t[ 0 ]
            start = 0
            while start != -1:
                start = s.find( p, start  )
                if start != -1:
                    end = start + len( p )
                    ind = ( start, end )
                    start = end
                    subseq.append( ind )

            rigid_ss.append( subseq )

        print( 'rigid_ss ...' )
        for t in rigid_ss:
            print( t )
        print( 'rigid_ss ... end' )

        return rigid_ss

    def s_satisfy_pattern(self, s, p ):
        '''
        check if a string s satisfy the pattern tuple_pattern
        :param s: a string
        :param p: a tuple that represent a pattern. for example
            ( 'a',  * )
            ( 'bc', 1 )
        :return: boolean
        '''
        s_size = len( s )

        if p[ 0 ] == None or  p[ 0 ] == '':
            return True

        if p[0] == '.':
            if  ( p[ 1 ] == 1   and len( s ) == 1 ) or  \
                ( p[ 1 ] == '*'  )                  or  \
                ( p[ 1 ] == '+' and len( s ) >= 1 ):
                return True

            return False

        elif p[ 1 ] == 1:
            if s == p[ 0 ]:
                return True

        elif p[ 1 ] == '*':
            if s_size == 0:
                return True

            p_size = len( p[ 0 ] )
            repeated = s.count( p[ 0 ] )
            if repeated * p_size  == s_size:
                return True

        elif p[ 1 ] == '+':
            if s_size == 0:
                return False

            p_size = len( p[ 0 ] )
            repeated = s.count( p[ 0 ] )
            if repeated * p_size  == s_size:
                return True

        return False

    def failed_matches(self, s, chunks, seq ):
        '''
        Take a string s, split it as chunks sizes says, and
        verify if each substring match a pattern in sequence seq.
        :param s      : a string
        :param chunks : a list of integers, each integer represent the number of characters for a substring
        :param seq    : a sequence of patterns. List of tuples ( string, number_of_times )
        :return       : number of substrings that NOT match its pattern. Float from 0.0 to 1.0
        '''
        start   = 0
        fails   = 0

        if len( seq ) == 0:
            return 0

        for i in range( 0, len( seq ) ):
            try:
                end = start + chunks[ i ]
                c = s  [ start : end  ]
                p = seq[ i ]
                if self.s_satisfy_pattern( c, p ):
                    pass
                else:
                    fails += 1
            except:
                fails += 1
            finally:
                start += chunks[ i ]

        fails = 1.0 * fails / len( seq )

        return fails




    def isMatch(self, s, p):
        result       = True
        seq          = self.get_seq( p )
        simp_seq     = self.simplify_seq( seq )
        #rigid_subseq = self.find_all_rigid_subseq( s, simp_seq )

        return result
