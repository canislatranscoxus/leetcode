'''
-------------------------------------------------------------------------------
fail in some cases.

3. Longest Substring Without Repeating Characters

Description:
    Given a string, find the length of the longest substring without repeating characters.

    Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Algorithm Intuition: create a dictionary 'counts' with char and (i1, i2, i3, ...) indexes.
                     create a dictionary 'repeated' of char
                     create a list       'candidates' of substrings
                        ( size, substring, start_index, end_index )
                     sort 'candidates' by size of substring

                     create a list 'Indexes', with the indexes of repeated chars.

                     sort Indexes by start_index

                     check which substrings in S does not contain another

author: AAT.
------------------------------------------------------------------------------- '''
from collections import defaultdict

class Solution(object):

    def get_counts(self, a ):
        '''
        read all the string, count the characters and store the indexes.
        :param a: string
        :return:
        '''
        n = len( a )
        d = defaultdict(list)
        for i in range( 0, n ):
            ch = a[ i ]
            d[ ch ].append( i )

        return d

    def get_candidates( self, counts, a ):
        '''
        create a list of candidates. Each candidate is a tuple
            ( size, substring, start_index, end_index )
        :param counts:
        :param a: string
        :return:
        '''
        candidates = list()

        # append all the string
        #t = (len(a), a, 0, len(a)-1 )
        #candidates.append( t )

        is_first = True

        for ch, indexes in counts.items():
            previous = indexes[ 0 ]
            if len( indexes ) == 1:

                continue

            for i in indexes:
                is_first = False
                if previous != i:
                    t = ( i - previous, a[ previous : i ], previous, i )
                    candidates.append( t )

                previous = i

        candidates = sorted( candidates, key = lambda t: -t[0] )
        return candidates

    def has_repeated_char( self, counts, a, ch, star_index, end_index ):
        '''
        check if char ch is repeated in a
        :param counts:
        :param a:
        :param ch:
        :param star_index:
        :param end_index:
        :return:
        '''
        result = False
        indexes = counts[ ch ]
        if len( indexes ) == 1:
            return False

        s = 0
        i = 0
        while i < len(indexes) and s < 2:
            ind = indexes[ i ]
            if ind >= star_index and ind < end_index:
                s = s + 1
            i = i + 1

        if s >= 2:
            result = True

        return  result

    def get_solutions( self, candidates, counts ):
        '''
        read the candidates and check if any of them is a solution.
        :param candidates:
        :return:
        '''

        solutions = []
        for c in candidates:
            size        = c[0]
            a           = c[1]
            start_index = c[2]
            end_index   = c[3]

            is_solution = True
            for ch, indexes in counts.items():
                if indexes[0] > end_index:
                    break
                if len( indexes ) == 1:
                    continue

                if self.has_repeated_char( counts, a, ch, start_index, end_index ) == True:
                    is_solution = False
                    break

            if is_solution == True:
                solutions.append( c )

        return solutions

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 1:
            return 1
        elif len(s) == 2:
            if s[0] == s[1]:
                return 1
            else:
                return 2

        result     = ''
        counts     = self.get_counts( s )
        candidates = self.get_candidates( counts, s )

        print('\ncandidates')
        candidates = self.get_candidates(counts, s)
        for c in candidates:
            print(c)

        solutions  = self.get_solutions( candidates, counts )

        if solutions != None and len(solutions) > 0:
            return solutions[0][0]

        return  0


#-------------------------------------------------------------------------------
# Unit Test
#-------------------------------------------------------------------------------


#a = 'abcabcbb'
a = 'aab'
print( 'input: {}'.format( a ) )

s = Solution()
output = s.lengthOfLongestSubstring( a )
print( 'output: {}'.format( output ) )


'''
ut_01
counts = s.get_counts( a )

print( 'counts' )
for ch, ind in counts.items():
    print( '{} \t {}'.format( ch, ind ) )

print( '\ncandidates' )
candidates = s.get_candidates( counts, a )
for c in candidates:
    print( c )

#a = 'abc'
ch = 'a'
repeated = s.has_repeated_char( counts, a, ch, 0, 7 )
print( '{} has repeated char {}: {}'.format( a, ch, repeated) )
'''

print( 'end.' )
