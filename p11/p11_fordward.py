'''
Description:  this is pure brute force
'''

class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':

        h1 = 0
        h2 = 1
        area = min( height[0], height[1] )

        size = len( height)
        for i in range( 0, size -1):

            if i > 0 and height[i] <= height[ h1 ]:
                i = h2

            for j in range( i+1, size ):

                n = min( height[i], height[j] )
                a = n * ( j - i)
                if a > area:
                    area = a
                    h1 = i
                    h2 = j

        print( 'area: {}, heights: {} and {}, indexes: {} and {}'.format( area, height[h1], height[h2], h1, h2 ) )
        return  area

    def __init__( self ):
        print( 'Contructor' )

# --------------------------------------

'''
s = Solution()
height = [1,8,6,2,5,4,8,3,7]
area = s.maxArea( height )

print( height )
print( 'area: {}'.format( area ) )
'''