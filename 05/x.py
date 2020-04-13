s = 'dabalearrozalazorraelabad'

r = s[ : : - 1 ]

if s == r:
    print( 'is palindrome' )

print( 's: {}'.format( s ) )
print( 'r: {}'.format( r ) )


s = 'aaaaaaaaaaaaaa'
ch = s[0]
r = s.replace( ch, '' )
size = len( r )
print ( 'replaced char : ***{}***'.format( r ) )
print ( 'size: {}'.format( size ) )

x1 = 0
x2 = 0
x1, x2 = 11, 22

b1 = x1 > 0
b2 = x1 > 0 and 1
b2 = x1 > 0 and 2

for i in range ( 5 ):
    print( i )

print( 'end' )