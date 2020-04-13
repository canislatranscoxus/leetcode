class GA_params:

    # basic parameters
    max_generations     = 500
    max_population_size = 100
    chromosome_size     =  4
    parents_pool        = 30

    last_generation     =  0

    # -------------------------------------------------------------------------
    # other parameters
    # -------------------------------------------------------------------------

    #string
    s_size  = 12
    s       = 'aaaabckefcef'

    pattern = ''

    subpatterns_seq = (
        ( 'a',  '*' ),
        ( 'bc',  1  ),
        ( '.',  '*' ),
        ( 'ef',  1  ) )