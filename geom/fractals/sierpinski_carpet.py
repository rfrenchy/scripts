
import numpy                as np
import matplotlib.pyplot    as plt
import square_functions     as square

## constants
CUBE_1  = 3**1      # 3
CUBE_2  = 3**2      # 9
CUBE_N1 = 3**-1     # 0.333

def carpet_side_effects(n, x, y): 
    plt.plot(x, y, 'b')
    plt.savefig('sierpinski_carpet.png')
    # print(pd.DataFrame({'n': n, 'x': x, 'y': y}))

### DONE - Shrink
### TODO - Magnify
def sierpinski_carpet(n = 1, side_effects = carpet_side_effects):
    # generation
    x1, y1  = square.unit_square()      # init
    x2, y2  = x1*CUBE_N1, y1*CUBE_N1    # shrink
    TX      = np.max(x2) - np.min(x2)   # find translate
    x2, y2  = x2+TX, y2+TX              # apply translate

    # side effects e.g. print
    side_effects(n, x1, y1)
    side_effects(n, x2, y2)
    
    # define recursion
    def carpet_recurse(n, x2, y2, TX):
        # return from recursion
        if n <= 0: return

        # shrink
        x2, y2 = x2/CUBE_1, y2/CUBE_1

        # plot and recurse
        def do(x, y):
            side_effects(n, x, y)
            carpet_recurse(n -1, x, y, TX)
        
        # recurse for each carpet segment
        for i in range(CUBE_2):
            if i == 0: do(x2, y2)
            if i == 1: do(x2, y2+TX) 
            if i == 2: do(x2, y2+TX+TX)
            if i == 3: do(x2+TX, y2)
            # if i == 4: do nothing
            if i == 5: do(x2+TX, y2+TX+TX)
            if i == 6: do(x2+TX+TX, y2)
            if i == 7: do(x2+TX+TX, y2+TX)
            if i == 8: do(x2+TX+TX, y2+TX+TX)

    # recurse
    carpet_recurse(n-1, x2, y2, TX)

sierpinski_carpet(3)