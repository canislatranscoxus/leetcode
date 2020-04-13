'''
Problem 11. Given n non-negative integers a1, a2, ..., an ,
            where each represents a point at coordinate (i, ai).
            n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
            Find two lines, which together with x-axis forms a container,
            such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
        Input: [1,8,6,2,5,4,8,3,7]
        Output: 49

Solution: 

        save max_area, maximum height of left line. This can help us to skip smaller containers.

        we calculate the area of water containers.
        we create water container like this

            for left_line looping from left to right
                if height of left line > max_left_line:
                    max_left_line = height of left line
                else:
                    skip this and continue with next left line
            
                for right_line looping from right to left
                    calculate area
                    and update variables

                    if height of right line > height of left line:
                        #we have found the biggest container using left line.
                        break this loop


'''
class Solution:

    def maxArea(self, height: 'List[int]') -> 'int':
        size   = len( height )

        # indexes
        left   = 0
        right  = size - 1

        area   = min( height[left], height[right] )
        max_left_line = 0

        for i in range( 0, size -2 ):

            if height[ i ] > max_left_line:
                max_left_line = height[ i ]
            else:
                continue


            for j in range(right, i, -1):
                #print( '{} - {}'.format( i, j) )

                #a = base    * height
                a  = (j - i) * min( height[i], height[j] )

                if a > area:
                    area  = a
                    left  = i
                    right = j

                if height[ j ] >= height[i]:
                    #we have reach the biggest container using lef_line.
                    break

        print( 'area   : {}     '.format( area ))
        print( 'heights[ {} ] = {}'.format( left,  height[ left  ] ))
        print( 'heights[ {} ] = {}'.format( right, height[ right ] ))

        return area

    def __init__( self ):
        print( 'Contructor' )

# --------------------------------------


s = Solution()
#height = [1,8,6,2,5,4,8,3,7]

height = [1,1]

area = s.maxArea( height )

print( height )
print( 'area: {}'.format( area ) )

