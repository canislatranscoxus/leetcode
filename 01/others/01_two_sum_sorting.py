'''
-------------------------------------------------------------------------------
Description: For Positive Integers, using sorting.

    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

Author: AAT.
------------------------------------------------------------------------------- '''

def two_sum( a, target ):
    found        = False
    i            = 0
    j            = 0
    num_elements = len( a )

    a = sorted( a )
    print( 'sorted data: {0}'.format( a ) )

    for i in range(0, num_elements ):
        if a[ i ] >= target:
            break

        for j in range( i, num_elements ):
            if j == i:
                continue

            s = a[ i ] + a[ j ]
            if s == target:
                found = True
                break
            elif s > target:
                break

        if found == True:
            break

    if found == True:
        print( 'The solution is' )
        print( 'i   : {0}, j   : {1}'.format( i, j ) )
        print( 'a[ {0} ]: {1}, a[ {2} ]: {3}'.format( i, a[i], j, a[j] ) )
    else:
        print( 'This array does not have solution' )


    return found, i, j

# -------------------------------------------------------------------------------
# test
# -------------------------------------------------------------------------------

data   = [ 15, 11, 7,  2 ]
target = 9
found  = False

print( 'original data: {0}'.format( data ) )

found, i, j = two_sum( data, target )
print( ' end.' )


