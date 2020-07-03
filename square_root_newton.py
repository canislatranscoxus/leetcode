'''

references:
    https://misapuntesyacimientos.wordpress.com/2016/02/20/raz-cuadradada-de-un-numero-utilizando-mtodo-numrico/
    https://en.wikipedia.org/wiki/Newton%27s_method
    https://brilliant.org/wiki/newton-raphson-method/
    http://www.sosmath.com/calculus/diff/der07/der07.html
    http://mathworld.wolfram.com/SquareRootAlgorithms.html

'''


def get_root_newton( m, err ):
    '''

    :param m: Positive Integer
    :param err: Error Degree, accuracy.
    :return: the root square of m.
    '''

    delta = 1.00
    x1 = m

    while delta >= err:
        x2 = 0.5 * ( x1 + (m / x1) )
        delta = x1 - x2
        x1 = x2
        print( 'x2: {}, delta: {}'.format( x2, delta ) )

    square_of_x2 = x2 * x2
    print( 'square of {} is  {}'.format( x2, square_of_x2 ) )

    return x2

# --------------------------------------------------------------------------------------------------------

# a Positive Integer  m
m = 50.0
err = 0.01

r = get_root_newton( m, err )